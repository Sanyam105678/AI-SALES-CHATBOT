import streamlit as st
from services.data_loader import load_sales_data, preprocess_data
from services.sales_logic import total_sales, sales_by_group
from services.store_logic import active_stores, active_stores_by_group
from visualization.charts import auto_chart
from llm.query_parser import parse_query_with_llm


st.title("AI Sales Data Chatbot")

DATA_PATH = "data/sales_data.xlsb"

df = preprocess_data(load_sales_data(DATA_PATH))

st.subheader("Quick Business Metrics Test")

st.subheader("Select Filters")

# Dynamic dropdown values
brands = sorted(df['Brand'].dropna().unique().tolist())
years = sorted(df['Year'].dropna().unique().tolist())
months = sorted(df['Month'].dropna().unique().tolist())

# Add "All" option
brands.insert(0, "All")
years.insert(0, "All")
months.insert(0, "All")

selected_brand = st.selectbox("Brand", brands)
selected_year = st.selectbox("Year", years)
# print("###################31",type(selected_year))
selected_month = st.selectbox("Month", months)


brand_filter = None if selected_brand == "All" else selected_brand
year_filter = None if selected_year == "All" else selected_year
month_filter = None if selected_month == "All" else selected_month


common_filters = {
    "year": year_filter,
    "month": month_filter,
    "brand": brand_filter
}



if st.button("Calculate Metrics"):
    
    sales = sales_by_group(
        df,
        group_by="Year",
        **common_filters
    )

    # stores = active_stores_by_group(
    #     df,
    #     group_by="Year",
    #     year=year_filter
    # )

    st.success(f"Total Sales: ")
    st.dataframe(sales)
    # st.success(f"Active Stores: {stores}")



st.subheader("Sales Visualization")

# Dynamic title parts
title_parts = ["Sales Trend"]

if year_filter:
    title_parts.append(f"Year: {year_filter}")

if brand_filter:
    title_parts.append(f"Brand: {brand_filter}")

chart_title = " | ".join(title_parts)


sales_df = sales_by_group(
    df,
    group_by="Month",
    year=year_filter,
    brand=brand_filter
)

if not sales_df.empty:
    fig = auto_chart(
        sales_df,
        x_col="Month",
        y_col="Total_Sales",
        title=chart_title
    )
    st.pyplot(fig)
else:
    st.warning("No data available for selected filters")


st.subheader("Ask a Business Question")

user_query = st.text_input(
    "Type your question (e.g. Show sales of Neo in March 2024)"
)



if st.button("Ask"):
    intent = parse_query_with_llm(user_query)

    metric = intent.get("metric")
    group_by = intent.get("group_by")
    year = intent.get("year")
    month = intent.get("month")
    brand = intent.get("brand")
    chart = intent.get("chart")

    st.subheader("Answer")

    

    # SALES
    if metric == "sales":
        if group_by is not None and isinstance(group_by, str):
            result_df = sales_by_group(
                df,
                group_by=group_by,
                year=year,
                month=month,
                brand=brand
            )

            st.dataframe(result_df)

            if chart and not result_df.empty:
                title_parts = ["Sales"]
                if year:
                    title_parts.append(f"Year: {year}")
                if brand:
                    title_parts.append(f"Brand: {brand}")

                fig = auto_chart(
                    result_df,
                    x_col=group_by,
                    y_col="Total_Sales",
                    title=" | ".join(title_parts)
                )
                st.pyplot(fig)

         # CASE 2: NO GROUP BY → SIMPLE TOTAL
        else:
            st.write("DEBUG → Filters:", year, month, brand)

            filtered_df = df.copy()
            if year:
                filtered_df = filtered_df[filtered_df["Year"] == year]
            if month:
                filtered_df = filtered_df[filtered_df["Month"] == month]
            if brand:
                filtered_df = filtered_df[filtered_df["Brand"].str.lower() == brand.lower()]

            st.write("DEBUG → Rows after filter:", len(filtered_df))

            total = total_sales(
                df,
                year=year,
                month=month,
                brand=brand
            )
            st.success(f"Total Sales: {total}")

    # ACTIVE STORES
    elif metric == "active_stores":
        if group_by:
            result_df = active_stores_by_group(
                df,
                group_by=group_by,
                **filters
            )

            st.dataframe(result_df)

            if chart and not result_df.empty:
                title = f"Active Stores by {group_by}"
                fig = auto_chart(
                    result_df,
                    x_col=group_by,
                    y_col="Active_Stores",
                    title=title
                )
                st.pyplot(fig)

        else:
            total = active_stores(df, **filters)
            st.success(f"Total Active Stores: {total}")

# st.write("Unique Months:", sorted(df["Month"].dropna().unique()))
# st.write("Unique Years:", sorted(df["Year"].dropna().unique()))
# st.write("Unique Brands:", df["Brand"].unique()[:10])



import pandas as pd
from config.settings import SALES_COLUMN, CUSTOMER_COLUMN, BRAND_COLUMN


def active_stores(
    df,
    year=None,
    month=None,
    brand=None
):
    data = df.copy()

    # Step 1: Apply filters
    if year is not None:
        data = data[data["Year"] == year]

    if month is not None:
        data = data[data["Month"] == month]

    if brand is not None:
        data = data[data["Brand"].str.lower() == brand.lower()]

    # Step 2: Customer-level aggregation
    customer_sales = (
        data
        .groupby("Customer")["Value"]
        .sum()
        .reset_index()
    )

    # Step 3: Sales > 0 condition
    active_customers = customer_sales[customer_sales["Value"] > 0]

    # Step 4: Business rule (-1)
    return max(len(active_customers) - 1, 0)


def active_stores_by_group(
    df,
    group_by,
    year=None,
    month=None,
    brand=None
):
    data = df.copy()

    # Step 1: Apply filters
    if year is not None:
        data = data[data["Year"] == year]

    if month is not None:
        data = data[data["Month"] == month]

    if brand is not None:
        data = data[data["Brand"].str.lower() == brand.lower()]

    # Step 2: Customer-level aggregation WITH group
    customer_sales = (
        data
        .groupby([group_by, "Customer"])["Value"]
        .sum()
        .reset_index()
    )

    # Step 3: Sales > 0
    active_customers = customer_sales[customer_sales["Value"] > 0]

    # Step 4: Count customers per group
    result = (
        active_customers
        .groupby(group_by)["Customer"]
        .nunique()
        .reset_index(name="Active_Stores")
    )

    # Step 5: Business rule (-1)
    result["Active_Stores"] = result["Active_Stores"].apply(
        lambda x: max(x - 1, 0)
    )

    return result.sort_values("Active_Stores", ascending=False)

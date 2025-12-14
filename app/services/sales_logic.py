import pandas as pd


from config.settings import SALES_COLUMN, BRAND_COLUMN


def total_sales(
    df,
    year=None,
    month=None,
    brand=None
):
    data = df.copy()

    if year is not None:
        data = data[data["Year"] == year]

    if month is not None:
        data = data[data["Month"] == month]

    if brand is not None:
        data = data[data[BRAND_COLUMN].str.strip().str.lower() == brand.lower()]

    return data[SALES_COLUMN].sum()






from config.settings import SALES_COLUMN, BRAND_COLUMN


def sales_by_group(
    df,
    group_by,
    year=None,
    month=None,
    brand=None
):
    data = df.copy()

    if year is not None:
        data = data[data["Year"] == year]

    if month is not None:
        data = data[data["Month"] == month]

    if brand is not None:
        data = data[data[BRAND_COLUMN].str.strip().str.lower() == brand.lower()]

    result = (
        data
        .groupby(group_by)[SALES_COLUMN]
        .sum()
        .reset_index()
        .rename(columns={SALES_COLUMN: "Total_Sales"})
        .sort_values(by="Total_Sales", ascending=False)
    )

    return result

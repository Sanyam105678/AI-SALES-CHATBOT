import pandas as pd


def active_stores(
    df: pd.DataFrame,
    brand: str = None,
    year: int = None,
    month: int = None
) -> int:
    """
    Calculate total active (unique) stores
    """
    data = df.copy()

    if brand:
        data = data[data['Brand'] == brand]

    if year:
        data = data[data['Year'] == year]

    if month:
        data = data[data['Month'] == month]

    return data['Store_ID'].nunique()


def active_stores_by_group(
    df: pd.DataFrame,
    group_by: str,
    year: int = None
) -> pd.DataFrame:
    """
    Active stores grouped by region / product / brand
    """
    data = df.copy()

    if year:
        data = data[data['Year'] == year]

    result = (
        data.groupby(group_by)['Store_ID']
        .nunique()
        .reset_index(name='Active_Stores')
        .sort_values(by='Active_Stores', ascending=False)
    )

    return result

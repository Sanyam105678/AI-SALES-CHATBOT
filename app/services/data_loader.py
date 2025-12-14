import pandas as pd
import os


def load_sales_data(file_path: str) -> pd.DataFrame:
    """
    Load sales Excel data into Pandas DataFrame
    Supports .xlsx and .xlsb
    """
    file_ext = os.path.splitext(file_path)[1]

    if file_ext == ".xlsb":
        df = pd.read_excel(file_path, engine="pyxlsb", sheet_name=1)
    else:
        df = pd.read_excel(file_path)

    # print("############df",df)
    return df


def preprocess_data(df):
    df = df.copy()

    # Normalize Brand
    if "Brand" in df.columns:
        df["Brand"] = df["Brand"].astype(str).str.strip()
        # print("##########df",df['Brand'].dropna().unique().tolist())

    # Handle Date → Year / Month
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Year"] = df["Date"].dt.year
        df["Month"] = df["Date"].dt.month

    # IF Month is text (December, Dec, etc.)
    elif "Month" in df.columns:
        df["Month"] = (
            pd.to_datetime(df["Month"], errors="coerce", format="%B")
            .dt.month
            .fillna(
                pd.to_datetime(df["Month"], errors="coerce", format="%b").dt.month
            )
        )

    # Ensure Year is numeric
    if "Year" in df.columns:
        df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

    return df


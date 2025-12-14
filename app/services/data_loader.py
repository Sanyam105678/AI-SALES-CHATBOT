import pandas as pd
import os


def load_sales_data(file_path: str) -> pd.DataFrame:
    """
    Load sales Excel data into Pandas DataFrame
    Supports .xlsx and .xlsb
    """
    file_ext = os.path.splitext(file_path)[1]

    if file_ext == ".xlsb":
        df = pd.read_excel(file_path, engine="pyxlsb")
    else:
        df = pd.read_excel(file_path)

    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare data for analysis
    """
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Quarter'] = df['Date'].dt.to_period('Q').astype(str)

    df = df.dropna(how='all')
    return df

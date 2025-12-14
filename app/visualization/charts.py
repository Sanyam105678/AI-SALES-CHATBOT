import matplotlib.pyplot as plt
import pandas as pd


def bar_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str
):
    """
    Generate bar chart
    """
    fig, ax = plt.subplots()

    ax.bar(df[x_col], df[y_col])
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title)

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def line_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str
):
    """
    Generate line chart
    """
    fig, ax = plt.subplots()

    ax.plot(df[x_col], df[y_col], marker='o')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title)

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig



def auto_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str
):
    """
    Automatically choose chart type based on x-axis
    """
    # Time-based → Line chart
    print("#####################x_col",x_col.lower())
    if x_col.lower() in ["year", "month", "quarter"]:
        return line_chart(df, x_col, y_col, title)

    # Otherwise → Bar chart
    return bar_chart(df, x_col, y_col, title)

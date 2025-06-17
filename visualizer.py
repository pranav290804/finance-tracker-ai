import matplotlib.pyplot as plt
import pandas as pd


def plot_category_pie(df):
    spending = df[df["Amount"] < 0]
    summary = spending.groupby("Category")["Amount"].sum().abs()

    plt.figure(figsize=(6, 6))
    plt.pie(summary, labels=summary.index, autopct="%1.1f%%", startangle=140)
    plt.title("Spending by Category")
    plt.tight_layout()
    return plt

import seaborn as sns

def plot_daily_trend(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["DailySpend"] = df["Amount"].where(df["Amount"] < 0, 0).abs()
    daily = df.groupby("Date")["DailySpend"].sum().reset_index()

    plt.figure(figsize=(10, 4))
    sns.lineplot(data=daily, x="Date", y="DailySpend", marker="o")
    plt.title("Daily Spending Trend")
    plt.xlabel("Date")
    plt.ylabel("Amount Spent")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

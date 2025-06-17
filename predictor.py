from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def predict_next_month(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    df["Spend"] = df["Amount"].where(df["Amount"] < 0, 0).abs()

    monthly_spend = df.groupby("Month")["Spend"].sum().reset_index()
    monthly_spend["MonthNum"] = range(1, len(monthly_spend)+1)

    X = monthly_spend["MonthNum"].values.reshape(-1, 1)
    y = monthly_spend["Spend"].values

    model = LinearRegression()
    model.fit(X, y)

    next_month = np.array([[monthly_spend["MonthNum"].max() + 1]])
    predicted = model.predict(next_month)[0]
    return predicted, monthly_spend

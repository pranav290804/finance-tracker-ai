import pandas as pd

def answer_question(df, question):
    question = question.lower()

    # 1. Total spending in category
    if "spend on" in question:
        for category in df["Category"].unique():
            if category.lower() in question:
                total = df[df["Category"] == category]["Amount"].sum()
                return f"You spent ${-total:.2f} on {category}."

    # 2. Total spending this month
    if "spending" in question and "month" in question:
        this_month = df["Date"].max().month
        filtered = df[df["Date"].dt.month == this_month]
        total = filtered[filtered["Amount"] < 0]["Amount"].sum()
        return f"You spent ${-total:.2f} this month."

    # 3. Income last month
    if "earn" in question or "income" in question:
        last_month = df["Date"].max().month - 1
        income = df[(df["Amount"] > 0) & (df["Date"].dt.month == last_month)]["Amount"].sum()
        return f"You earned ${income:.2f} last month."

    # 4. Biggest transaction
    if "biggest" in question or "largest" in question:
        row = df.loc[df["Amount"].abs().idxmax()]
        return f"Your biggest transaction was '{row['Description']}' for ${abs(row['Amount']):.2f} on {row['Date'].date()}."

    # 5. Show all related to keyword
    for keyword in ["amazon", "uber", "netflix", "starbucks"]:
        if keyword in question:
            matches = df[df["Description"].str.lower().str.contains(keyword)]
            if not matches.empty:
                return matches[["Date", "Description", "Amount"]].to_string(index=False)
            return f"No transactions found for '{keyword}'."

    return "Sorry, I couldn't understand your question."

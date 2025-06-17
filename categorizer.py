def categorize_transaction(description):
    mapping = {
        "Starbucks": "Food & Dining",
        "Restaurant": "Food & Dining",
        "Uber": "Transport",
        "Spotify": "Subscriptions",
        "Netflix": "Subscriptions",
        "Amazon": "Shopping",
        "Rent": "Housing",
        "Electricity": "Utilities",
        "Grocery": "Groceries",
        "ATM": "Cash",
        "Gym": "Health & Fitness",
        "PayPal": "Transfers",
        "Insurance": "Insurance",
        "Salary": "Income"
    }

    for keyword, category in mapping.items():
        if keyword.lower() in description.lower():
            return category
    return "Other"

def add_categories(df):
    df["Category"] = df["Description"].apply(categorize_transaction)
    return df

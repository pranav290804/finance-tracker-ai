
# 💸 AI Personal Finance Tracker

An intelligent personal finance dashboard that helps you understand and manage your spending using AI. Upload your bank statement CSV and get smart visualizations, category insights, and natural language responses to your financial questions.

> ⚡ Built with Streamlit · Python · Cohere AI · Pandas · Seaborn

---

## 📊 Features

- **CSV Upload:** Drag-and-drop your bank statement (CSV format)
- **Spending Summary:** Auto-categorizes and summarizes your expenses
- **Visual Insights:**
  - Category-wise pie chart
  - Daily spending trend
- **Ask AI Anything:**
  - “How can I save more?”
  - “Compare spending across months”
  - “What’s my biggest expense category?”
- **AI-Powered:** Uses Cohere’s large language model to interpret financial data

---

## 🚀 Live Demo

👉 [Try the app here](https://finance-tracker-ai-7p5czru6xbsbduxtg47sv4.streamlit.app/)

---

## 🥪 Sample CSV Format

Upload your bank statement in the following format:

```csv
Date,Description,Amount,Category
2024-04-02,Amazon,1200,Shopping
2024-04-05,Rent,15000,Housing
2024-04-10,Starbucks,250,Food
...
```

---

## 🛠️ Tech Stack

- Python 3.10
- [Streamlit](https://streamlit.io/)
- [Cohere AI](https://cohere.com/)
- Pandas, Seaborn, Matplotlib
- GitHub + Streamlit Cloud Deployment

---

## 🔒 Environment Setup

Create a `.streamlit/secrets.toml` file:

```toml
COHERE_API_KEY = "your-cohere-api-key"
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
streamlit run app.py
```

---

## 📌 To-Do / Improvements

- ✅ Add category prediction
- ✅ Add GPT-style Q&A
- ⏳ Export reports
- ⏳ Compare across multiple CSVs
- ⏳ Budget alerts

---

## 🙌 Author

Built by [Pranav](https://github.com/pranav290804)


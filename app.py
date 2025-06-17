import streamlit as st
from parser import load_transactions
from categorizer import add_categories
from visualizer import plot_category_pie
from visualizer import plot_daily_trend
from predictor import predict_next_month
from qa_engine import answer_question
from cohere_qa import ask_cohere





st.title("💸 AI Personal Finance Tracker")

uploaded_file = st.file_uploader("Upload your bank statement CSV")

if uploaded_file:
    df = load_transactions(uploaded_file)
    df = add_categories(df)

    st.subheader("📋 Transactions")
    st.dataframe(df)

    st.subheader("📊 Spending Breakdown")
    fig = plot_category_pie(df)
    st.pyplot(fig)

    st.subheader("📉 Daily Spending Trend")
    trend_fig = plot_daily_trend(df)
    st.pyplot(trend_fig)

    st.subheader("📈 Predicted Next Month Spend")
    predicted, _ = predict_next_month(df)
    st.success(f"Predicted next month’s spending: ${predicted:.2f}")

    

    st.subheader("🤖 Ask AI About Your Finances")

    gpt_question = st.text_input("Ask anything, like 'Compare spending across months'")

    if gpt_question:
        gpt_response = ask_cohere(df, gpt_question)
        st.write(gpt_response)


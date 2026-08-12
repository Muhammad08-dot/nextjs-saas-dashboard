import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Next.js SaaS Enterprise Dashboard", page_icon="🚀", layout="wide")

st.title("🚀 Enterprise SaaS Intelligence & Metrics Dashboard")
st.markdown("Real-time revenue analytics, active user telemetry, server latency, and AI inference token consumption.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Monthly Recurring Revenue (MRR)", "$142,850", "+14.2% MoM")
col2.metric("Active Enterprise Tenants", "342", "+28 this month")
col3.metric("API Latency (p99)", "42ms", "-5ms optimization")
col4.metric("LLM Token Consumption", "14.2M tokens", "$284.50 cost")

st.subheader("Revenue & Growth Trajectory")
chart_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
    "MRR ($K)": [45, 62, 80, 98, 115, 130, 138, 142.8],
    "New Signups": [120, 150, 210, 280, 340, 390, 420, 460]
})
st.area_chart(chart_data.set_index("Month")[["MRR ($K)"]])

st.subheader("Tenant Distribution by Plan")
fig = px.pie(names=["Starter", "Pro", "Enterprise", "Custom Agent"], values=[45, 35, 15, 5])
st.plotly_chart(fig, use_container_width=True)

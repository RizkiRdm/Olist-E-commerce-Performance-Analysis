import pandas as pd
import streamlit as st
import os

DATA_FOLDER = "data"


@st.cache_data
def load_all_data():
    """
    Loads all pre-aggregated CSV files for the dashboard.
    """
    data = {}
    csv_files = {
        "monthly_sales_summary": "dashboard_monthly_sales_summary.csv",
        "daily_patterns": "dashboard_daily_patterns.csv",
        "hourly_patterns": "dashboard_hourly_patterns.csv",
        "order_status_distribution": "dashboard_order_status_distribution.csv",
        "delivery_performance_summary": "dashboard_delivery_performance_summary.csv",
        "delivery_time_distribution": "dashboard_delivery_time_distribution.csv",
        "avg_freight_by_state": "dashboard_avg_freight_by_state.csv",
        "customer_rfm_segments": "dashboard_customer_rfm_segments.csv",
        "rfm_product_category_counts": "dashboard_rfm_product_category_counts.csv",
        "rfm_payment_type_counts": "dashboard_rfm_payment_type_counts.csv",
        "rfm_customer_state_counts": "dashboard_rfm_customer_state_counts.csv",
        "rfm_delivery_performance_summary": "dashboard_rfm_delivery_performance_summary.csv",
        "seller_performance_summary": "dashboard_seller_performance_summary.csv",
    }
    file_exist = True
    for key, filename in csv_files.items():
        file_path = os.path.join(DATA_FOLDER, filename)
        if not os.path.exists(file_path):
            st.error(f"data file not found: {file_path}")
            file_exist = False
            break
        try:
            df = pd.read_csv(file_path)
            # convert date after load the data
            if key == "monthly_sales_summary":
                df["month_year"] = pd.to_datetime(df["month_year"])
            data[key] = df
        except Exception as e:
            st.error(f"Failed load {filename}: {e}")
            file_exist = False
            break

        # if all data not loaded, stop the app
        if not file_exist:
            st.stop()
    return data

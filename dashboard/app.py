import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# import data loader
from src.data_loader import load_all_data

# config streamlit app
st.set_page_config(page_title="Olist E-commerce Performance Dashboard", layout="wide")
st.title("Olist E-commerce Performance Dashboard")
st.markdown("Analysis of Sales, Customers, and Sellers Performance for Olist Brazil")

# rename function
dashboard_data = load_all_data()

# Ekstract data
monthly_sales_summary_df = dashboard_data.get("monthly_sales_summary")
daily_patterns_df = dashboard_data.get("daily_patterns")
hourly_patterns_df = dashboard_data.get("hourly_patterns")
order_status_distribution_df = dashboard_data.get("order_status_distribution")
delivery_performance_summary_df = dashboard_data.get("delivery_performance_summary")
delivery_time_distribution_df = dashboard_data.get("delivery_time_distribution")
avg_freight_by_state_df = dashboard_data.get("avg_freight_by_state")
customer_rfm_segments_df = dashboard_data.get("customer_rfm_segments")
rfm_product_category_counts_df = dashboard_data.get("rfm_product_category_counts")
rfm_payment_type_counts_df = dashboard_data.get("rfm_payment_type_counts")
rfm_customer_state_counts_df = dashboard_data.get("rfm_customer_state_counts")
rfm_delivery_performance_summary_df = dashboard_data.get(
    "rfm_delivery_performance_summary"
)
seller_performance_summary_df = dashboard_data.get("seller_performance_summary")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Executive Summary",
        "Sales & Order Performance",
        "Customer Insights (RFM)",
        "Seller Performance",
    ]
)

# conten tab 1: Executive summary / Overview
with tab1:
    st.header("Executive summary")
    st.text("Key Metrics of business performance")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        total_revenue = monthly_sales_summary_df["total_revenue"].sum()
        st.metric(label="Total Revenue", value=f"R$ {total_revenue}")
    with col2:
        total_orders = monthly_sales_summary_df["total_orders"].sum()
        st.metric(label="Total Orders", value=f"{total_orders:,}")
    with col3:
        avg_order_value = monthly_sales_summary_df["avg_order_value"].mean()
        st.metric(label="Avarage Order", value=f"R$ {avg_order_value:,.2f}")
    with col4:
        total_unique_customers = customer_rfm_segments_df[
            "customer_unique_id"
        ].nunique()
        st.metric(label="Total Customer", value=f"{total_unique_customers:,}")
    with col5:
        total_unique_sellers = seller_performance_summary_df["seller_id"].nunique()
        st.metric(label="Total Seller", value=f"{total_unique_sellers:,}")
    with col6:
        on_time_early_pct = (
            delivery_performance_summary_df[
                delivery_performance_summary_df["delivery_performance_category"].isin(
                    ["Early", "On-Time"]
                )
            ]["percentage"].sum()
            * 100
        )
        st.metric(label="On-Time/Faster Shipping", value=f"{total_unique_sellers:,}")

    st.subheader("Trend Performance")

    # monthly total revenue trend
    fig_revenue_trend = px.line(
        monthly_sales_summary_df,
        x="month_year",
        y="total_revenue",
        title="Trend Total Revenue Monthly Product",
        labels={"total_revenue": "Total Revenue (R$)", "month_year": "Month"},
        markers=True,
    )
    fig_revenue_trend.update_layout(hovermode="x unified")
    st.plotly_chart(fig_revenue_trend, use_container_width=True)

    # monthly total order trend
    fig_revenue_trend = px.line(
        monthly_sales_summary_df,
        x="month_year",
        y="total_orders",
        title="Trend Total Orders Monthly Product",
        labels={"total_orders": "Number of Orders", "month_year": "Month"},
        markers=True,
    )
    fig_revenue_trend.update_layout(hovermode="x unified")
    st.plotly_chart(fig_revenue_trend, use_container_width=True)

# tab 2: Sales and order performance
with tab2:
    st.header("sales and Order Performance")
    st.text("Detail about Sales Pattern, Order Status, and Delivery efficiency")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.subheader("Daily Order Pattern")
        fig_daily_order = px.bar(
            daily_patterns_df,
            x="day_of_week",
            y="total_orders",
            title="Number of Order per Day in a Week",
            labels={"day_of_week": "Day", "total_orders": "Number of Order"},
        )
        st.plotly_chart(fig_daily_order, use_container_width=True)
    with col_s2:
        st.subheader("Hourly Order Pattern")
        fig_daily_order = px.bar(
            hourly_patterns_df,
            x="hour_of_day",
            y="total_orders",
            title="Number of Order per hour",
            labels={"hour_of_day": "Hour", "total_orders": "Number of Order"},
        )
        st.plotly_chart(fig_daily_order, use_container_width=True)

    st.subheader("Status & Order Quality")
    col_s3, col_s4 = st.columns(2)
    with col_s3:
        order_status_distribution_df = order_status_distribution_df.sort_values(
            by="percentage", ascending=True
        )

        fig_order_status = px.bar(
            order_status_distribution_df,
            x="percentage",
            y="order_status",
            title="Distribution Order Status",
            text="percentage",
            labels={
                "order_status": "Order Status",
                "percentage": "Percentage (%)",
            },
            orientation="h",
        )

        fig_order_status.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside",
        )

        fig_order_status.update_layout(
            xaxis_range=[
                0,
                order_status_distribution_df["percentage"].max() * 1.1,
            ],
            uniformtext_minsize=8,
            uniformtext_mode="hide",
            yaxis={"categoryorder": "total ascending"},
        )
        st.plotly_chart(fig_order_status, use_container_width=True)

    with col_s4:
        fig_delivery_performance = px.bar(
            delivery_performance_summary_df,
            x="delivery_performance_category",
            y="percentage",
            title="Distribution Delivery Performance",
            labels={
                "delivery_performance_category": "Order Category",
                "percentage": "Percentage (%)",
            },
        )
        st.plotly_chart(fig_delivery_performance, use_container_width=True)

    st.subheader("Delivery Time Distribution")
    fig_delivery_time_hist = px.histogram(
        delivery_time_distribution_df,
        x="total_delivery_time",
        nbins=50,
        title="Distribution Total Time Delivery (Day)",
        labels={"total_delivery_time": "Time Delivery (Day)"},
    )
    st.plotly_chart(fig_delivery_time_hist, use_container_width=True)

    st.subheader("Logistics Costs per Region")
    fig_freight_by_state = px.bar(
        avg_freight_by_state_df.head(10),
        x="avg_freight_value",
        y="customer_state",
        orientation="h",
        title="Top 10 Average Shipping Costs by Customer State",
        labels={
            "avg_freight_value": "Average Shipping Cost (R$)",
            "customer_state": "Customer's State",
        },
    )
    fig_freight_by_state.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_freight_by_state, use_container_width=True)

# tab3: customer insights (RFM)
with tab3:
    st.header("Customer Insight (RFM)")
    st.text("Deep understanding of customer segmentation and customer behavior")

    st.subheader("Summary Segment RFM")

    col_c1, col_c2 = st.columns(2)

    with col_c1:
        rfm_segment_counts = (
            customer_rfm_segments_df["RFM_segment"].value_counts().reset_index()
        )
        rfm_segment_counts.columns = [
            "RFM_segment",
            "customer_count",
        ]

        fig_rfm_segments = px.bar(
            rfm_segment_counts,
            x="RFM_segment",
            y="customer_count",
            title="Number of Customers per RFM Segment",
            labels={
                "RFM_segment": "RFM Segment",
                "customer_count": "Number of Customers",
            },
        )
        st.plotly_chart(fig_rfm_segments, use_container_width=True)

    with col_c2:
        avg_rfm_scores = (
            customer_rfm_segments_df.groupby("RFM_segment")[
                ["Recency", "Frequency", "Monetary"]
            ]
            .mean()
            .reset_index()
        )
        fig_avg_rfm_scores = px.bar(
            avg_rfm_scores.melt(
                id_vars="RFM_segment",
                var_name="RFM Metric",
                value_name="Avarage Value",
            ),
            x="RFM_segment",
            y="Avarage Value",
            color="RFM Metric",
            barmode="group",
            title="Avarage Recency, Frequency, and Monetary per Segment",
            labels={
                "RFM_segment": "RFM Segment",
                "Avarage Value": "Avarage Value",
            },
        )
        st.plotly_chart(fig_avg_rfm_scores, use_container_width=True)

    st.subheader("Characteristic the Segment")

    selected_rfm_segment = st.selectbox(
        "Chose Segment to see the detail RFM Segment",
        options=rfm_product_category_counts_df["RFM_segment"].unique().tolist(),
    )
    if selected_rfm_segment:
        col_c3, col_c4, col_c5 = st.columns(3)

        with col_c3:
            st.markdown(f"**Top product Category for {selected_rfm_segment}**")

            filtered_category_products = rfm_product_category_counts_df[
                rfm_product_category_counts_df["RFM_segment"] == selected_rfm_segment
            ].nlargest(5, "order_id")
            fig_detail_product_categories = px.bar(
                filtered_category_products,
                x="order_id",
                y="product_category_name",
                orientation="h",
                labels={
                    "order_id": "Order Quantity",
                    "product_category_name": "Product Category",
                },
            )
            fig_detail_product_categories.update_layout(
                yaxis={"categoryorder": "total ascending"}
            )
            st.plotly_chart(fig_detail_product_categories, use_container_width=True)

        with col_c4:
            st.markdown(f"**Top Payment type for segment {selected_rfm_segment}**")

            filtered_payment_types = rfm_payment_type_counts_df[
                rfm_payment_type_counts_df["RFM_segment"] == selected_rfm_segment
            ].nlargest(5, "order_id")
            fig_detail_payment_types = px.bar(
                filtered_payment_types,
                x="order_id",
                y="payment_type",
                orientation="h",
                labels={
                    "order_id": "Order Quantity",
                    "payment_type": "payment Type",
                },
            )
            fig_detail_payment_types.update_layout(
                yaxis={"categoryorder": "total ascending"}
            )
            st.plotly_chart(fig_detail_payment_types, use_container_width=True)

        with col_c5:
            st.markdown(f"**Top Customer State for segment {selected_rfm_segment}**")

            filtered_customer_states = rfm_customer_state_counts_df[
                rfm_customer_state_counts_df["RFM_segment"] == selected_rfm_segment
            ].nlargest(5, "order_id")
            fig_detail_customer_states = px.bar(
                filtered_customer_states,
                x="order_id",
                y="customer_state",
                orientation="h",
                labels={
                    "order_id": "Order Quantity",
                    "customer_state": "payment Type",
                },
            )
            fig_detail_customer_states.update_layout(
                yaxis={"categoryorder": "total ascending"}
            )
            st.plotly_chart(fig_detail_customer_states, use_container_width=True)

    st.subheader("Delivery Performance per Segment")
    fig_rfm_delivery_performace = px.bar(
        rfm_delivery_performance_summary_df.melt(
            id_vars="RFM_segment", var_name="Metric", value_name="Value"
        ),
        x="RFM_segment",
        y="Value",
        color="Metric",
        barmode="group",
        title="Average Time Delivery & Performance VS. Estimate per Segment",
        labels={"Value": "Average Day"},
    )
    st.plotly_chart(fig_rfm_delivery_performace, use_container_width=True)

# tab4: seller Performance
with tab4:
    st.header("Seller Performance")
    st.text(
        "Analysis about Contribution and Eficiency Seller to Sell Their Product in E-commerce"
    )

    st.subheader("Seller Contributions")

    col_cell_1, col_cell_2 = st.columns(2)

    with col_cell_1:
        top_seller_revenue = seller_performance_summary_df.nlargest(10, "total_revenue")
        fig_top_seller_revenue = px.bar(
            top_seller_revenue,
            x="total_revenue",
            y="seller_id",
            orientation="h",
            title="Top 10 Seller With Highest Sales",
            labels={"total_revenue": "Total Revenue", "seller_id": "Seller ID"},
        )
        fig_top_seller_revenue.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig_top_seller_revenue, use_container_width=True)

    with col_cell_2:
        top_seller_orders = seller_performance_summary_df.nlargest(10, "total_orders")
        fig_top_seller_orders = px.bar(
            top_seller_orders,
            x="total_orders",
            y="seller_id",
            orientation="h",
            title="Top 10 Seller with Highest Number of Orders",
            labels={"total_orders": "Total Revenue", "seller_id": "Seller ID"},
        )
        fig_top_seller_orders.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig_top_seller_orders, use_container_width=True)

    st.subheader("Seller Shipping Efficiency")
    col_cell_3, col_cell_4 = st.columns(2)

    with col_cell_3:
        fig_orders_vs_delivery = px.scatter(
            seller_performance_summary_df,
            x="total_orders",
            y="avg_delivery_time",
            size="total_revenue",
            hover_name="seller_id",
            title="Total Orders VS. Average Shipping Time per Seller",
            labels={
                "total_orders": "Total Orders",
                "avg_delivery_time": "AVG Shipping Time",
                "total_revenue": "Total Revenue",
                "seller_id": "Seller ID",
            },
            color_discrete_sequence=["#1f77b4"],
        )
        st.plotly_chart(fig_orders_vs_delivery, use_container_width=True)

    with col_cell_4:
        fig_orders_vs_estimate = px.scatter(
            seller_performance_summary_df,
            x="total_orders",
            y="avg_delivery_vs_estimate",
            size="total_revenue",
            hover_name="seller_id",
            title="Total Orders VS. Average Shipping Time VS. Estimate per Seller",
            labels={
                "total_orders": "Total Orders",
                "avg_delivery_vs_estimate": "AVG Shipping Time (VS Estimate)",
                "total_revenue": "Total Revenue",
                "seller_id": "Seller ID",
            },
            color_discrete_sequence=["#ff7f0e", "#1f77b4"],
        )
        st.plotly_chart(fig_orders_vs_estimate, use_container_width=True)

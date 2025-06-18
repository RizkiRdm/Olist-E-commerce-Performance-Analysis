# Olist E-commerce Performance & Strategic Insights Dashboard

## 1. Project Overview

This project delivers a comprehensive, interactive dashboard designed to analyze the historical performance of Olist, a Brazilian e-commerce platform. Beyond standard performance metrics, this analysis specifically leverages the context of Olist's **subsequent insolvency due to high operational debt** to extract crucial strategic insights and valuable lessons for the e-commerce industry.

The dashboard transforms raw transactional data into actionable intelligence, providing stakeholders with a clear view of sales trends, customer behavior, order fulfillment efficiency, and seller performance. It aims to support data-driven decision-making and identify areas for operational optimization and strategic re-evaluation.

## 2. Problem Statement

Olist's operational history, culminating in its insolvency, underscores a critical need for robust data analytics to understand core business dynamics. The challenge was to systematically analyze a large e-commerce dataset to:
* Identify underlying sales patterns and anomalies.
* Evaluate customer value and purchasing behavior (e.g., prevalence of one-time buyers).
* Assess operational efficiencies, particularly in order fulfillment and logistics.
* Pinpoint contributing factors to operational burden (e.g., high logistics costs, revenue leakage from suboptimal sales days).
* Derive actionable insights and cautionary lessons for sustainable e-commerce growth.

## 3. Data Source

The project utilizes the **Olist E-commerce Public Dataset**, available on Kaggle. This dataset provides information on 100,000 orders placed at Olist stores in Brazil from 2016 to 2018, encompassing various dimensions such as order status, customer and seller locations, product categories, payment methods, and review scores.

## 4. Methodology & Architecture

The project is structured with a strong emphasis on modularity, ensuring clear separation of concerns between data processing, data loading, and the user interface.

### 4.1. Project Structure

### 4.2. Data Processing & Analysis Pipeline

1.  **Raw Data Ingestion:** Initial loading of various Olist CSV files.
2.  **Data Cleaning & Preprocessing:** Handling missing values, correcting data types, converting timestamps, and addressing inconsistencies.
3.  **Feature Engineering:** Creating new metrics essential for analysis, such as `total_revenue`, `delivery_time`, `avg_delivery_vs_estimate`, and RFM scores.
4.  **Aggregation & Summarization:** Data is aggregated into various summary DataFrames (e.g., monthly sales, daily/hourly patterns, RFM segments, seller performance) to optimize dashboard loading times.
5.  **Data Export:** Summarized DataFrames are saved as Parquet/CSV files in the `data/processed/` directory.

### 4.3. Key Analytical Techniques

* **Time-Series Analysis:** Analyzing sales and order trends on monthly, daily, and hourly bases.
* **RFM (Recency, Frequency, Monetary) Analysis:** Segmenting customers based on their purchasing behavior to identify high-value, loyal, and at-risk customers.
* **Delivery Performance Metrics:** Calculating actual delivery times versus estimated times to assess logistical efficiency.
* **Seller Performance Metrics:** Evaluating sellers based on total revenue, total orders, and delivery punctuality.
* **Geographic & Category Analysis:** Understanding performance distribution across customer states and product categories.

## 5. Dashboard Features & Key Insights

The interactive dashboard is built using Streamlit and Plotly, providing a multi-tabbed interface for different analytical perspectives.

![Executive Summary Tab](assets/post_2.jpg)

### 5.1. Executive Summary

* **KPI Cards:** Displays crucial overall metrics such as Total Revenue, Total Orders, Average Order Value, Unique Customers, Unique Sellers, and On-time/Early Delivery Percentage.
* **Trend Analysis:** Visualizes monthly trends in total revenue and unique orders, offering insights into growth patterns and significant events (e.g., the sharp decline in Sept 2018 due to insolvency).

### 5.2. Sales & Order Performance

* **Daily & Hourly Order Patterns:** Reveals peak operational times (e.g., weekends and specific hours like 9 AM - 3 PM).
* **Order Status Distribution:** Provides a breakdown of order statuses, highlighting the high percentage of delivered orders (98.22%).
* **Delivery Performance & Time Distribution:** Visualizes the proportion of early, on-time, and late deliveries (86% delivered ahead of schedule), alongside the overall distribution of delivery durations.
* **Logistics Costs by Region:** Identifies regions with higher average freight values (e.g., RO, RR, AP).

### 5.3. Customer Insights (RFM)

* **RFM Segment Distribution:** Shows the proportion of customers in different RFM segments. Critically, **over 99% of Olist's customers were identified as one-time buyers**, indicating a significant challenge in customer retention.
* **Average RFM Scores per Segment:** Compares average Recency, Frequency, and Monetary values across segments. The **"Single Buyers (Moderate R & High M)" segment exhibited the highest average Monetary value (nearly R$600)**, suggesting high-value one-off transactions.
* **Segment Characteristics:** Allows exploration of top product categories, payment types, and customer states for selected RFM segments. `beleza_saude` was found to be popular among `Champions`.
* **Delivery Performance by RFM Segment:** Demonstrates consistent early delivery across all customer segments.

### 5.4. Seller Performance

* **Top Sellers by Revenue & Order Volume:** Ranks sellers based on their contribution to total revenue and number of orders, highlighting "star sellers" who excel in both metrics. For instance, top sellers contributed significantly (e.g., ~R$20,000 revenue from `4869f7a5dfa277a7dca6462dcf3b52b2`, >150 orders from `4a3ca9315b744ce9f8e9374361493884`).
* **Seller Delivery Efficiency:** Scatter plots illustrate the relationship between total orders, revenue, and average delivery times (vs. estimate), revealing that the **majority of sellers deliver orders ahead of their estimated dates**.

### Interactive Filters:
The dashboard includes dynamic filters in the sidebar for:
* **Date Range (Month/Year):** To analyze trends over specific periods.

## 6. Technologies Used

* **Python:** Programming language
* **Pandas:** Data manipulation and analysis
* **Streamlit:** Building interactive web applications/dashboards
* **Plotly Express:** Creating interactive and visually appealing charts
* **NumPy:** Numerical operations

## 7. Installation & Setup

Follow these steps to get the project up and running on your local machine.

### 7.1. Prerequisites

* Python 3.8+
* pip (Python package installer)

### 7.2. Clone the Repository

```bash
git clone [https://github.com/your-username/olist-ecommerce-dashboard.git](https://github.com/your-username/olist-ecommerce-dashboard.git)
cd olist-ecommerce-dashboard
````

_(Replace `your-username` with your actual GitHub username)_

### 7.3. Install Dependencies

Install all required Python packages:

Bash

```
pip install -r requirements.txt
```

### 7.4. Prepare the Data

You will need to download the raw Olist E-commerce Public Dataset from Kaggle.

- Download the dataset from [Kaggle - Olist E-commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
- Place all the downloaded `.csv` files into the `data/raw/` directory within your project.

Then, run the data preparation script to clean, transform, and aggregate the data. This script will create the necessary processed CSVs in the `data/processed/` folder.

Bash

```
python -m src.data_preparator
```

### 7.5. Run the Dashboard

Once the data is prepared, you can launch the Streamlit dashboard:

Bash

```
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

## 8. Future Enhancements

- **Enhanced Customer State Filtering:** Integrate `customer_state` filter more deeply across all relevant dashboards (e.g., Sales trends by state) after ensuring `customer_state` is available in all relevant aggregated dataframes.
- **Advanced Analytics:** Implement predictive models (e.g., sales forecasting, customer churn prediction).
- **Deployment:** Deploy the dashboard to a cloud platform (e.g., Streamlit Community Cloud, Heroku, AWS EC2) for public access.

## 9. Author

- **[Rizki Romdhoni]** - [LinkedIn Profile](https://www.linkedin.com/in/rizki-romdhoni/)

## 10. License

This project is open-sourced under the [MIT License](https://opensource.org/licenses/MIT).

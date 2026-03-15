## Digital Marketing Performance Auditor

## Project Overview
This interactive Streamlit application provides a self-service "Digital Marketing Performance Auditor" as a KPIs health-check and visualization tools for digital marketing campaign data. It allows marketing staff and analysts to perform rapid Exploratory Data Analysis (EDA) and visualize KPIs performance without writing code.

## Features
- **Dynamic File Upload**: Supports custom CSV campaign data.
- **Flexible Filtering**: Automatically identifies categorical columns to allow users to optionally filter insights by Campaign ID, Ad Group, Region, and other categories.
- **Multivariate Visualizations**:
    - **Histograms**: View distributions of individual KPI with dynamic titles.
    - **Pairplot Grids**: Analyze correlations between multiple metrics simultaneously for segmented insights.
- **Automated Statistics**: Instant generation of descriptive statistics (min, max, mean, std, etc.) for selected metrics.

## Tools Used 
- **Python**: Core application logic.
- **Streamlit**: Web interface and interactive UI components.
- **Pandas**: Data manipulation and categorical filtering.
- **Seaborn & Matplotlib**: Advanced data visualization and plotting.

## How to Run
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
4. Launch the app: python -m streamlit run app.py

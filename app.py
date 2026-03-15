import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Adjust the Title as core theme of your Interactive App.
st.title("Digital Marketing Performance Auditor")

# Requirement: Prompting the User to upload CSV file.
uploaded_file = st.file_uploader("Please upload your Campaign data in CSV format:", type="csv")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    
    st.sidebar.header("Audit Settings")

    # Optional: Allow user to pick ANY categorical column to filter by.
    filter_columns = df.select_dtypes(include=['object']).columns.tolist()
    if filter_columns:
        column_to_filter = st.sidebar.selectbox("Filter by (Optional):", ["None"] + filter_columns)
        if column_to_filter != "None":
            unique_values = df[column_to_filter].dropna().unique().tolist()
            selected_value = st.sidebar.selectbox(f"Select {column_to_filter}:", unique_values)
            df = df[df[column_to_filter] == selected_value]

    # Get numeric columns for analysis
    numeric_cols = df.select_dtypes("number").columns.tolist()

    # Input 1: Prompting the User to select their desired KPIs for analysis.
    selected_kpis = st.sidebar.multiselect(
        "Select KPIs for analysis:", 
        options=numeric_cols,
        default=numeric_cols[:2] if len(numeric_cols) >= 2 else numeric_cols
    )

    # Input 2: prompting the User to select their desired Plot types.
    plot_kind = st.sidebar.radio("Select type of Plot:", ["Histogram", "Pairplot"])

    # Output 1: Visualized Plots.
    st.subheader("KPIs Performance Analysis")
    
    if len(selected_kpis) > 0:
        if plot_kind == "Histogram":
            # Create individual histograms for each selected KPI.
            for kpi in selected_kpis:
                fig, ax = plt.subplots()
                sns.histplot(df[kpi], kde=True, ax=ax, color="skyblue")
                # Dynamic title for each histogram.
                ax.set_title(f"Distribution of {kpi}") 
                st.pyplot(fig)
        
        else:
            # Create Pairplot Grid for multi-KPIs analysis.
            status_message = st.empty() 
            status_message.write("⏳ Generating pairplot grid... please wait.")
            fig = sns.pairplot(df[selected_kpis], diag_kind="kde")
            # Dynamic title using the list of selected KPIs.
            fig.fig.suptitle(f"Influence Analysis: {', '.join(selected_kpis)}", y=1.02)
            status_message.empty()
            st.pyplot(fig)
    else:
        st.warning("Please select at least 01 KPI to visualize.")

    # Output 2: Summary Statistics.
    st.subheader("Campaign Health Check")
    st.write(df[selected_kpis].describe())

else:
    st.info("Please upload your Campaign data in CSV format to begin the audit.")
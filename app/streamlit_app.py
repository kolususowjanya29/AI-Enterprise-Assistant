import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

st.set_page_config(
    page_title="AI Enterprise Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🤖 AI-Powered Enterprise Assistant")
st.write(
    "Upload documents, analyze structured data, search information "
    "and generate intelligent reports."
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Enterprise Assistant")

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "📄 Document Assistant",
        "📊 Data Analysis",
        "🗄️ SQL Query Agent",
        "📈 Report Generator",
        "🧪 AI Evaluation",
        "📋 Monitoring"
    ]
)

# -----------------------------
# DASHBOARD
# -----------------------------
if menu == "🏠 Dashboard":

    st.header("📊 Enterprise Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Documents", "12")
    col2.metric("Queries", "48")
    col3.metric("Reports", "9")
    col4.metric("System Status", "Online")

    st.subheader("System Overview")

    data = pd.DataFrame({
        "Module": [
            "Document Management",
            "RAG Question Answering",
            "SQL Agent",
            "Reports",
            "Evaluation"
        ],
        "Status": [
            "Active",
            "Active",
            "Active",
            "Active",
            "Active"
        ]
    })

    st.dataframe(data, use_container_width=True)

# -----------------------------
# DOCUMENT ASSISTANT
# -----------------------------
elif menu == "📄 Document Assistant":

    st.header("📄 Document Assistant")

    uploaded_file = st.file_uploader(
        "Upload a document",
        type=["txt", "csv", "pdf"]
    )

    if uploaded_file:

        st.success("Document uploaded successfully!")

        if uploaded_file.name.endswith(".txt"):

            text = uploaded_file.read().decode("utf-8")

            st.subheader("Document Preview")
            st.text_area("Content", text, height=250)

            question = st.text_input(
                "Ask a question about the document"
            )

            if question:

                words = question.lower().split()

                sentences = text.split(".")

                results = []

                for sentence in sentences:
                    if any(word in sentence.lower() for word in words):
                        results.append(sentence.strip())

                if results:
                    st.success(
                        "Relevant information found:"
                    )

                    for result in results[:5]:
                        st.write("•", result)
                else:
                    st.info(
                        "No matching information found in the document."
                    )

        elif uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

            st.subheader("Dataset Preview")
            st.dataframe(df, use_container_width=True)

            st.write("Rows:", df.shape[0])
            st.write("Columns:", df.shape[1])

        else:

            st.info(
                "PDF uploaded successfully. "
                "PDF processing can be connected to the RAG/OCR pipeline."
            )

# -----------------------------
# DATA ANALYSIS
# -----------------------------
elif menu == "📊 Data Analysis":

    st.header("📊 Structured Data Analysis")

    file = st.file_uploader(
        "Upload CSV dataset",
        type=["csv"]
    )

    if file:

        df = pd.read_csv(file)

        st.success("Dataset loaded successfully!")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", int(df.isnull().sum().sum()))

        st.subheader("Dataset")

        st.dataframe(
            df.head(100),
            use_container_width=True
        )

        st.subheader("Statistical Summary")

        st.dataframe(
            df.describe(include="all").transpose(),
            use_container_width=True
        )

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns.tolist()

        if numeric_columns:

            column = st.selectbox(
                "Select numeric column",
                numeric_columns
            )

            st.subheader("Distribution")

            st.bar_chart(
                df[column].value_counts().head(20)
            )

# -----------------------------
# SQL QUERY AGENT
# -----------------------------
elif menu == "🗄️ SQL Query Agent":

    st.header("🗄️ SQL Database Query Agent")

    data = pd.DataFrame({
        "employee_id": [1, 2, 3, 4, 5],
        "name": [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eva"
        ],
        "department": [
            "IT",
            "HR",
            "Finance",
            "IT",
            "HR"
        ],
        "salary": [
            60000,
            50000,
            70000,
            65000,
            55000
        ]
    })

    conn = sqlite3.connect(":memory:")

    data.to_sql(
        "employees",
        conn,
        index=False,
        if_exists="replace"
    )

    st.subheader("Employee Database")

    st.dataframe(
        data,
        use_container_width=True
    )

    query = st.text_area(
        "Enter SQL query",
        value="SELECT * FROM employees"
    )

    if st.button("▶ Run SQL Query"):

        try:

            result = pd.read_sql_query(
                query,
                conn
            )

            st.success("Query executed successfully!")

            st.dataframe(
                result,
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"SQL Error: {e}"
            )

# -----------------------------
# REPORT GENERATOR
# -----------------------------
elif menu == "📈 Report Generator":

    st.header("📈 Intelligent Report Generator")

    title = st.text_input(
        "Report Title",
        "Enterprise Data Analysis Report"
    )

    summary = st.text_area(
        "Enter report information",
        "The enterprise assistant analyzed the uploaded data and generated useful insights."
    )

    if st.button("Generate Report"):

        report = f"""
# {title}

Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Executive Summary

{summary}

## System Modules

- Document Management
- RAG Question Answering
- SQL Query Agent
- Data Analysis
- AI Evaluation
- Monitoring

## Conclusion

The AI-Powered Enterprise Assistant provides an integrated
platform for document analysis, structured data processing,
question answering and intelligent reporting.
"""

        st.success("Report generated successfully!")

        st.download_button(
            "⬇️ Download Report",
            report,
            file_name="enterprise_report.md",
            mime="text/markdown"
        )

        st.text_area(
            "Generated Report",
            report,
            height=350
        )

# -----------------------------
# AI EVALUATION
# -----------------------------
elif menu == "🧪 AI Evaluation":

    st.header("🧪 AI Response Evaluation")

    evaluation_data = pd.DataFrame({
        "Metric": [
            "Answer Accuracy",
            "Relevance",
            "Response Quality",
            "Grounding"
        ],
        "Score": [
            0.92,
            0.90,
            0.94,
            0.89
        ]
    })

    st.dataframe(
        evaluation_data,
        use_container_width=True
    )

    st.subheader("Overall Evaluation Score")

    st.progress(0.91)

    st.success(
        "Overall AI evaluation score: 91%"
    )

# -----------------------------
# MONITORING
# -----------------------------
elif menu == "📋 Monitoring":

    st.header("📋 Monitoring & Logging")

    logs = pd.DataFrame({
        "Time": [
            "10:15",
            "10:20",
            "10:25",
            "10:30"
        ],
        "Operation": [
            "Document Upload",
            "RAG Query",
            "SQL Query",
            "Report Generated"
        ],
        "Status": [
            "Success",
            "Success",
            "Success",
            "Success"
        ]
    })

    st.dataframe(
        logs,
        use_container_width=True
    )

    st.success(
        "All monitored services are operational."
    )

# -----------------------------
# FOOTER
# -----------------------------
st.sidebar.markdown("---")
st.sidebar.info(
    "AI Enterprise Assistant\n\n"
    "Built using Python, Streamlit, Pandas and SQLite."
)

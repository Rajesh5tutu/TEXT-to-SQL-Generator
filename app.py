from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

# Configure Gemini API once, cache the model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@st.cache_resource
def get_gemini_model():
    return genai.GenerativeModel(model_name="gemini-2.0-flash")

# Cache your SQLite connection for the lifetime of the app
@st.cache_resource
def get_db_connection(db_path: str):
    # check_same_thread=False allows reuse across Streamlit threads
    return sqlite3.connect(db_path, check_same_thread=False)

# Memoize SQL queries (keyed by the SQL string + db_path)
@st.cache_data
def read_sql_query(sql: str, db_path: str) -> pd.DataFrame:
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [c[0] for c in cur.description]
    # no need to commit on SELECT
    return pd.DataFrame(rows, columns=cols)

def get_gemini_response(question: str, prompt: str) -> str:
    model = get_gemini_model()
    response = model.generate_content([prompt, question])
    return response.text.strip()

# Prompt stays identical
prompt = """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.

Example 1 - How many entries of records are present?
SELECT COUNT(*) FROM STUDENT;

Example 2 - Tell me all the students studying in Data Science class?
SELECT * FROM STUDENT WHERE CLASS="Data Science";

Return only the SQL query without explanation or markdown.
"""

# Page config
st.set_page_config(page_title="SQL Genie", page_icon="🧞", layout="wide")

# Theme toggle defaults
if "theme" not in st.session_state:
    st.session_state.theme = "light"

c1, c2, c3 = st.columns([8, 1, 1])
with c2:
    if st.button("🌞", use_container_width=True):
        st.session_state.theme = "light"
with c3:
    if st.button("🌙", use_container_width=True):
        st.session_state.theme = "dark"

# Single CSS injection
if st.session_state.theme == "dark":
    css = """
    <style>
      .stApp { background-color: #0e1117; color: #fff; font-family: 'Segoe UI'; }
      .container { max-width: 700px; margin: auto; padding: 20px; }
      .card { background: #1e1e1e; padding:20px; border-radius:12px; box-shadow:0 0 10px #222; margin-bottom:20px; }
      .stTextInput label { color:#fff !important; font-weight:600; }
      .stTextInput > div > input { background:#2c2c2c; color:#fff; border:1px solid #555; padding:10px; border-radius:8px; }
      .stButton > button { background:#4a4a4a; color:#fff; padding:6px 16px; border-radius:6px; font-weight:600; }
      .stCode, .stDataFrame { background:#1e1e1e; color:#fff; border-radius:8px; padding:12px; }
      div[data-testid="stDownloadButton"] > button { background:#4a4a4a; color:#fff; border:1px solid #888; border-radius:8px; padding:10px 20px; }
    </style>
    """
else:
    css = """
    <style>
      .stApp { background:#fff; color:#000; font-family:'Segoe UI'; }
      .container { max-width:700px; margin:auto; padding:20px; }
      .card { background:#f9f9f9; padding:20px; border-radius:12px; box-shadow:0 0 10px #ccc; margin-bottom:20px; }
      .stTextInput label { color:#000 !important; font-weight:600; }
      .stTextInput > div > input { background:#fff; color:#000; border:1px solid #ccc; padding:10px; border-radius:8px; }
      .stButton > button { background:#e0e0e0; color:#000; padding:6px 16px; border-radius:6px; font-weight:600; }
      .stCode, .stDataFrame { background:#f5f5f5; color:#000; border-radius:8px; padding:12px; }
      div[data-testid="stDownloadButton"] > button { background:#e0e0e0; color:#000; border:1px solid #ccc; border-radius:8px; padding:10px 20px; }
    </style>
    """
st.markdown(css, unsafe_allow_html=True)

# App content
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<h2 style='margin-bottom:0;'>🧞 SQL Genie</h2>", unsafe_allow_html=True)
st.markdown("Ask questions about your STUDENT database and get instant SQL queries.")

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 💬 Ask Your Question")
question = st.text_input("Enter your question:")
submit = st.button("✨ Generate SQL")
st.markdown("</div>", unsafe_allow_html=True)

if submit and question:
    with st.spinner("Generating SQL and querying database..."):
        try:
            sql_query = get_gemini_response(question, prompt)
            df = read_sql_query(sql_query, "student.db")

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("#### 🧾 Generated SQL Query")
            st.code(sql_query, language="sql")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            if not df.empty:
                st.markdown("#### 📊 Query Results")
                st.dataframe(df, use_container_width=False)

                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    "📥 Download Results as CSV",
                    data=csv,
                    file_name="query_results.csv",
                    mime="text/csv",
                )
            else:
                st.warning("No results found or query returned nothing.")
            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("</div>", unsafe_allow_html=True)
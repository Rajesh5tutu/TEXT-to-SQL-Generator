## TEXT-to-SQL-Generator
A fast, theme-adaptive Text-to-SQL generator with compact UI cards, intuitive controls, and production-ready UX. Built for seamless query generation from natural language — no SQL expertise required.

### Features
- Natural-language to SQL conversion using Google Gemini (gemini-2.0-flash)
- Instant query execution against a local SQLite database
- Interactive Streamlit interface with light/dark theme toggle
- Compact, card-based layout for inputs, generated SQL, and results
- Cached Gemini model and SQLite connection for snappy performance
- Downloadable query results as CSV
- Error handling and user feedback on empty or invalid queries

### Technologies Used
- Programming Language: Python 3.x
- Web Framework: Streamlit
- AI / ML API: google-generativeai (Gemini 2.0-flash)
- Database: SQLite (sqlite3)
- Data Processing: pandas
- Environment Configuration: python-dotenv
- Styling: Custom CSS injected into Streamlit
- Version Control: Git / GitHub

## Getting Started
Follow these steps to run the SQL Genie locally on your machine.

### Prerequisites
- Python 3.7 or higher
- A Google Cloud API key with Generative AI access
- Git and pip installed on your system

### Installation
- Clone the repository
>> https://github.com/Rajesh5tutu/TEXT-to-SQL-Generator.git

>>cd text-to-sql-generator

- Create and activate a virtual environment
>> python -m venv .venv
>> source .venv/bin/activate      # macOS/Linux
>>.venv\Scripts\activate         # Windows

- Install dependencies
>> pip install -r requirements.txt

- Configure environment variables
>> Copy .env.example to .env
>> Add your Google API key in .env:
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

- Initialize the SQLite database
>> python sql.py

- Run the Streamlit app
>> streamlit run app.py





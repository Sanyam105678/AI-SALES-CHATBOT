# AI-SALES-CHATBOT
# AI Chatbot for Sales & Active Stores Analysis

## 📌 Project Overview

This project is a **Python-based AI Chatbot** that answers **business questions** related to:
- **Sales**
- **Active Stores (Unique Customers with Sales > 0)**

The chatbot understands **natural language queries** and dynamically:
- Applies business filters (Year, Month, Brand, Product)
- Performs accurate calculations using Pandas
- Displays results as **numbers, tables, and charts**

The solution is validated against **Excel pivot logic** to ensure correctness.

---

## 🚀 Key Features

- Natural language query handling (Chatbot-style)
- Sales analysis:
  - Total sales
  - Sales by Year / Month / Brand / Region
  - Trend visualizations
- Active Stores analysis:
  - Active store = **Unique Customer with total sales > 0**
  - Monthly & Yearly active stores
  - Business rule applied: **Final count = Active Stores − 1**
- Comparison queries:
  - This year vs last year (YoY)
- Automatic chart selection:
  - Line charts for time-based data
  - Bar charts for categorical data
- Clean, modular, and production-ready architecture

---

## 🧠 Business Logic Definitions

### Sales
- Calculated as the **sum of sales value**
- Filters applied before aggregation

### Active Stores
- **Each unique customer name = one active store**
- Condition: **Total sales > 0**
- Calculated at customer level (not row level)
- Final business rule:



---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Pandas, NumPy** – Data processing
- **Matplotlib** – Data visualization
- **Streamlit** – UI & chatbot interface
- **OpenPyXL / PyXLSB** – Excel reading
- **Rule-based NLP (LLM-ready)** – Intent parsing

---

## 📂 Project Structure

```bash
ai-sales-chatbot/
│
├── app/
│ ├── main.py # Streamlit entry point
│ │
│ ├── services/
│ │ ├── data_loader.py # Excel loading & preprocessing
│ │ ├── sales_logic.py # Sales calculations
│ │ └── store_logic.py # Active store calculations
│ │
│ ├── llm/
│ │ └── query_parser.py # Natural language intent parser
│ │
│ ├── visualization/
│ │ └── charts.py # Bar & line chart logic
│ │
│ └── config/
│ └── settings.py # Column name configuration
│
├── data/
│ └── sales_data.xlsx # Input dataset
│
├── requirements.txt
└── README.md
```


---

## ⚙️ Setup Instructions (Step-by-Step)

### 1️⃣ Clone or Download the Project

```bash
git clone <repository-url>
cd ai-sales-chatbot
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Dataset
```bash
data/sales_data.xlsx
```

### 5️⃣ Run the Application
```bash
streamlit run app/main.py
```
- Open Browser 
```bash
http://localhost:8501
```





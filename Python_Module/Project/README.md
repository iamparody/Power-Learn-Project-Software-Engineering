# 📄 CORD-19 Data Explorer

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red)
![WordCloud](https://img.shields.io/badge/WordCloud-NLP-purple)

---

## 🧩 Problem Statement
The COVID-19 Open Research Dataset (CORD-19) contains over a million scholarly articles on COVID-19 and related coronaviruses.  
The challenge is to **clean, analyze, and visualize this large dataset** to extract meaningful insights about research trends, top journals, and frequently discussed topics.

---

## 🛠️ Our Approach
1. **Data Cleaning**
   - Remove duplicates and invalid entries
   - Handle missing values in key columns (`title`, `abstract`, `authors`, `journal`, `publish_time`)
   - Convert dates to `datetime` format

2. **Data Preparation**
   - Extract publication year from `publish_time`
   - Compute abstract word counts
   - Filter realistic publication years (2019 onwards)

3. **Analysis**
   - Count papers by publication year
   - Identify top journals publishing COVID-19 research
   - Find the most frequent words in paper titles

4. **Visualization**
   - Line chart for publications over time
   - Bar chart of top journals
   - Word cloud of paper titles
   - Distribution of papers by source

5. **Interactive Streamlit App**
   - Slider to filter by publication year
   - Display visualizations dynamically
   - Show a sample of the dataset

---

## 🏃 Steps to Run

### 1. Clone Repository / Download Files
Ensure you have the following files in your working directory:
- `cord19_clean_metadata.csv` (cleaned dataset)
- `app.py` (Streamlit app)

### 2. Install Required Libraries
```bash
pip install pandas matplotlib wordcloud streamlit


Run Streamlit App

streamlit run app.py
The app will open in your default browser.

### If using Colab, use pyngrok to expose the app:

!pip install pyngrok
from pyngrok import ngrok
public_url = ngrok.connect(addr="8501", proto="http")
!streamlit run app.py &
print(public_url)
📊 Features
Interactive year slider to filter papers

Line chart: Publications per year

Bar chart: Top journals

Word cloud: Most common words in titles

Sample table: Preview paper metadata including title, authors, journal, DOI, and URL

📂 Project Structure
bash
Copy code
├── app.py                  # Streamlit application
├── cord19_clean_metadata.csv  # Cleaned CORD-19 metadata
├── README.md               # Project documentation
✨ Insights & Reflections
Most papers published in 2020–2022, with clear peaks corresponding to COVID-19 waves.

Top journals include major medical and virology publications.

Common keywords in titles include: covid, sars, vaccine, patients.

Challenges:

Large dataset handling

Missing publication dates and DOIs

Cleaning text for NLP tasks

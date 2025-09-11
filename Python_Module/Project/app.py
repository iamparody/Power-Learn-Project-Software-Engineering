# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ------------------------
# Load cleaned dataset
# ------------------------
df_clean = pd.read_csv("cord19_clean_metadata.csv")

# Convert publish_time to datetime
df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')

# Extract publish year
df_clean['publish_year'] = df_clean['publish_time'].dt.year

# Filter realistic COVID-19 years
df_clean = df_clean[df_clean['publish_year'] >= 2019]

# Fill missing values
df_clean['authors'] = df_clean['authors'].fillna('Unknown')
df_clean['journal'] = df_clean['journal'].fillna('Unknown')
df_clean['abstract'] = df_clean['abstract'].fillna('No abstract')

# ------------------------
# Streamlit Layout
# ------------------------
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers interactively")

# ------------------------
# Interactive year range slider
# ------------------------
min_year = int(df_clean['publish_year'].min())
max_year = int(df_clean['publish_year'].max())
year_range = st.slider("Select publication year range", min_year, max_year, (2020, 2021))

# Filter data
df_filtered = df_clean[(df_clean['publish_year'] >= year_range[0]) &
                       (df_clean['publish_year'] <= year_range[1])]

# ------------------------
# Publications over time
# ------------------------
papers_per_year = df_filtered.groupby('publish_year').size()

st.subheader("Publications Over Time")
st.line_chart(papers_per_year)

# ------------------------
# Top journals
# ------------------------
top_journals = df_filtered['journal'].value_counts().head(10)

st.subheader("Top 10 Journals")
st.bar_chart(top_journals)

# ------------------------
# Word cloud for titles
# ------------------------
st.subheader("Word Cloud of Paper Titles")
all_titles_filtered = " ".join(df_filtered['title'].astype(str)).lower()
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles_filtered)
st.image(wordcloud.to_array(), use_column_width=True)

# ------------------------
# Display sample of data
# ------------------------
st.subheader("Sample of Papers")
st.dataframe(df_filtered[['title', 'authors', 'journal', 'publish_year', 'doi', 'url']].head(20))

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

df = load_data()

# Clean data
df.dropna(subset=['age'], inplace=True)

# Streamlit interface
st.title('Titanic Survival Analysis')

# Sidebar filters
st.sidebar.header('Filters')
pclass = st.sidebar.selectbox("Select Class", df['class'].unique())
sex = st.sidebar.selectbox("Select Gender", df['sex'].unique())

# Filter data
filtered_df = df[(df['class'] == pclass) & (df['sex'] == sex)]

# Display survival rate by gender
survival_rate = filtered_df['survived'].mean()
st.write(f"Survival Rate for {sex} in Class {pclass}: {survival_rate:.2%}")

# Display detailed statistics
st.subheader('Statistics for Filtered Data')
st.write(filtered_df.describe())

# Visualization
st.subheader('Survival Rate by Gender')
sns.set(style="whitegrid")
plt.figure(figsize=(8, 4))
sns.barplot(x='sex', y='survived', data=filtered_df, ci=None)
plt.title(f'Survival Rate for {sex} in Class {pclass}')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
st.pyplot(plt)

# Additional visualizations
st.subheader('Age Distribution of Survivors')
plt.figure(figsize=(10, 6))
sns.histplot(data=filtered_df, x='age', hue='survived', multiple='stack', bins=30)
plt.title('Age Distribution of Survivors and Non-Survivors')
plt.xlabel('Age')
plt.ylabel('Count')
st.pyplot(plt)

# Add conclusion section
st.sidebar.subheader('Conclusion')
st.sidebar.write("""
The survival rate can vary significantly based on class and gender. 
This analysis can help us understand the factors that influenced survival during the Titanic disaster.
""")

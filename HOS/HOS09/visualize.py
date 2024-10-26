# 1.	Importing Libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 2.	Function to Load Data from SQLite
def load_data():
    conn = sqlite3.connect('data_warehouse.db')
    df = pd.read_sql_query('SELECT product, SUM(quantity) AS total_quantity, SUM(price * quantity) AS total_revenue FROM sales GROUP BY product', conn)
    conn.close()
    return df

# 3.	Streamlit Interface
st.title('Sales Data Warehouse Analysis')

# 4.	Load Data
data = load_data()

# 5.	Display the Data
st.subheader('Sales Data Summary')
st.write(data)

# 6.	Bar Chart Visualization
st.subheader('Total Quantity Sold by Product')
fig, ax = plt.subplots()
data.plot(x='product', kind='bar', ax=ax, legend=False)
plt.title('Total Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity')
plt.xticks(rotation=45)

# 7.	Display the Plot in Streamlit
st.pyplot(fig)

# 8.	Display Additional Information
st.sidebar.subheader('Analysis Options')
selected_product = st.sidebar.selectbox('Select Product:', data['product'].unique())

# 9.	Filtered Data for the Selected Product
filtered_data = data[data['product'] == selected_product]
st.sidebar.write(filtered_data)


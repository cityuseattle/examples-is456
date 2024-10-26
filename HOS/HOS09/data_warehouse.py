import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database (or create it)
conn = sqlite3.connect('data_warehouse.db')
cursor = conn.cursor()

# Create a sample table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    date TEXT NOT NULL
)
''')

# Insert sample data
sales_data = [
    ('Widget A', 10, 2.5, '2024-01-01'),
    ('Widget B', 5, 5.0, '2024-01-02'),
    ('Widget A', 3, 2.5, '2024-01-03'),
    ('Widget C', 7, 7.0, '2024-01-04'),
    ('Widget B', 4, 5.0, '2024-01-05'),
]

cursor.executemany('INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)', sales_data)
conn.commit()

# Query data for analysis
df = pd.read_sql_query('SELECT product, SUM(quantity) AS total_quantity, SUM(price * quantity) AS total_revenue FROM sales GROUP BY product', conn)

# Display the DataFrame
print(df)

# Visualization
df.plot(x='product', kind='bar', legend=False)
plt.title('Total Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()

# Close the connection
conn.close()

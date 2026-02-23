import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("\n--- EXPENSE TRACKER ANALYSIS ---\n")


total_spending = df["Amount"].sum()
print("Total Monthly Spending: ₹", total_spending)


category_spending = df.groupby("Category")["Amount"].sum()
print("\nSpending by Category:\n")
print(category_spending)

highest_category = category_spending.idxmax()
print("\nHighest Spending Category:", highest_category)


daily_average = df["Amount"].mean()
print("\nAverage Expense per Transaction: ₹", round(daily_average, 2))


monthly_income = 25000
savings = monthly_income - total_spending
print("\nMonthly Income: ₹", monthly_income)
print("Estimated Savings: ₹", savings)


amounts = np.array(df["Amount"])
print("\n--- NumPy Statistics ---")
print("Standard Deviation:", round(np.std(amounts), 2))
print("Maximum Expense:", np.max(amounts))
print("Minimum Expense:", np.min(amounts))


sorted_expenses = df.sort_values(by="Amount", ascending=False)
print("\nTop 5 Highest Expenses:\n")
print(sorted_expenses.head())

print("\n--- Analysis Completed Successfully ---")

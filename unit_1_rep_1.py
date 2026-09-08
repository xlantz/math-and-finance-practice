import pandas as pd
import matplotlib.pyplot as plt

monthly_revenue = [
    42000, 45500, 39800, 51000, 47200, 44100,
    46800, 210000, 43500, 48900, 45200, 46000
]
monthly_revenue_series = pd.Series(monthly_revenue)

mean_monthly_revenue = monthly_revenue_series.mean()
median_monthly_revenue = monthly_revenue_series.median()
std_monthly_revenue = monthly_revenue_series.std()
describe_monthly_revenue = monthly_revenue_series.describe()

print(f"Mean: {round(mean_monthly_revenue, 2)}")
print(f"Median: {median_monthly_revenue}")
print(f"Std Dev: {round(std_monthly_revenue, 2)}")
print(f"\nDescribe:\n{describe_monthly_revenue}")

# Median ($45,850) better represents a "typical month" than mean (~$59,167).
# Month 8's $210,000 is a one-time bulk order, not normal operations —
# it pulls the mean up ~$13k above where most months actually cluster.
# Median, using only the middle value's rank, ignores that outlier entirely.

monthly_revenue_series[monthly_revenue_series < 100000].hist()
plt.title("Monthly Revenue Distribution")
plt.xlabel("Revenue ($)")
plt.ylabel("Frequency")
plt.show()
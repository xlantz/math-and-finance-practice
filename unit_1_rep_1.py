import pandas as pd

import math

monthly_revenue = [
    42000, 45500, 39800, 51000, 47200, 44100,
    46800, 210000, 43500, 48900, 45200, 46000
]

monthly_revenue_series = pd.Series(monthly_revenue)

mean_monthly_revenue = monthly_revenue_series.mean()

median_monthly_revenue = monthly_revenue_series.median()

mode_monthly_revenue = monthly_revenue_series.mode()

std_monthly_revenue = monthly_revenue_series.std()

describe_monthly_revenue = monthly_revenue_series.describe()

check_monthly_revenue = monthly_revenue_series.hist()

print(f"Mean: {round(mean_monthly_revenue,2)}, \nMedian:{median_monthly_revenue}, \nMode:{mode_monthly_revenue}, \nStd:{std_monthly_revenue}, \nDesc:{describe_monthly_revenue}, \nHist:{check_monthly_revenue}")
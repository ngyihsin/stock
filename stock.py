import numpy as np
import pandas as pd

# Set investment targets and corresponding interest rates
targets = ['GOF', 'PDI', 'US Treasury bonds', 'BBB grade company bonds']
interest_rates = [0.1274, 0.1348, 0.0396, 0.06]

# Define function to calculate investment allocation based on risk level
def calculate_allocation(total_investment, risk_level):
    # Define risk levels and corresponding allocation ratios
    risk_levels = [1, 2, 3, 4, 5]
    allocation_ratios = [[0.4, 0.4, 0.1, 0.1],
                         [0.35, 0.35, 0.15, 0.15],
                         [0.3, 0.3, 0.2, 0.2],
                         [0.2, 0.2, 0.3, 0.3],
                         [0.1, 0.1, 0.4, 0.4]]

    # Find the allocation ratio for the given risk level
    allocation_ratio = allocation_ratios[risk_level-1]

    # Calculate the investment amount for each target based on the allocation ratio
    investment_amounts = np.multiply(total_investment, allocation_ratio)

    # Calculate the annual income for each investment
    annual_incomes = np.multiply(investment_amounts, interest_rates)

    # Round the investment amounts and annual incomes to two decimal places
    investment_amounts = np.round(investment_amounts, 2)
    annual_incomes = np.round(annual_incomes, 2)

    # Return a dictionary of the investment targets and their corresponding investment amounts and annual incomes
    investment_allocation = dict(zip(targets, zip(investment_amounts, annual_incomes)))
    return investment_allocation

# Example usage: allocate 15 million NT dollars across five risk levels to generate an annual income of 1.2 million NT dollars
total_investment = 15000000
annual_income = 1200000
all_investments = []

for risk_level in range(1, 6):
    real_income = 0
    investment_allocation = calculate_allocation(total_investment, risk_level)
    level_investments = {"Risk Level": risk_level, "Total Investment (NTD)": total_investment, "Annual Income (NTD)": annual_income}
    for target in investment_allocation:
        investment_amount, annual_income = investment_allocation[target]
        level_investments[f"{target} (NTD)"] = investment_amount
        level_investments[f"{target} Annual Income (NTD)"] = annual_income
        real_income += annual_income 
    level_investments["Real Annual Income"] = real_income
    all_investments.append(level_investments)

df = pd.DataFrame(all_investments)
df = df.set_index("Risk Level")
df.index.name = None

# Export the dataframe to an Excel file
df.to_excel('investment_allocation.xlsx', sheet_name='Investment Allocation')

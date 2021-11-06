# Loading required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path_of_matches_file = './data/matches.csv'
path_of_deliveries_file = './data/deliveries.csv'

# Reading CSV files
matches = pd.read_csv(path_of_matches_file)
deliveries = pd.read_csv(path_of_deliveries_file)

# Total runs by each team
total_runs_by_each_team = deliveries.groupby(
    'batting_team')[['total_runs']].sum()
sns.set_style("darkgrid")
plt.figure(figsize=(18,6))
plt.title("Total runs by each team.")
sns.barplot(y=total_runs_by_each_team.index,
            x=total_runs_by_each_team.total_runs)
plt.yticks(rotation=35)
plt.savefig('./output/problem_1.png')

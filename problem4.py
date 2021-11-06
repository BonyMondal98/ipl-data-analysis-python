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

# Stacked chart of matches played by team by season
stacked_chart_of_mathces_by_team_by_season = matches.groupby(
    ['season', 'team1'])['id'].count().unstack().fillna(0)
stacked_chart_of_mathces_by_team_by_season.plot(kind='bar', stacked=True)
plt.title("Mathches played by team by season.")
plt.savefig('./output/problem_4.png')

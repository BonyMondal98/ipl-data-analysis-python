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

# Top batsman for Royal Challengers Bangalore
games_played_by_royal_challengers = deliveries[deliveries['batting_team']
                                               == "Royal Challengers Bangalore"]
batsman_name_and_runs = games_played_by_royal_challengers.groupby(
    'batsman')[['batsman_runs']].sum().head(5)
sns.set_style("darkgrid")
plt.figure(figsize=(12, 6))
plt.title("Top batsman from Royal Challengers Bangalore.")
sns.barplot(y=batsman_name_and_runs.index,
            x=batsman_name_and_runs.batsman_runs)
plt.savefig('./output/problem_2.png')

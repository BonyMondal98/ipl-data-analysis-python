# Loading required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path_of_matches_file = './data/matches.csv'
path_of_deliveries_file = './data/deliveries.csv'
path_of_umpires_file='./data/umpires.csv'

# Reading CSV files
matches = pd.read_csv(path_of_matches_file)
deliveries = pd.read_csv(path_of_deliveries_file)
umpires=pd.read_csv(path_of_umpires_file)

# Manipulating dataset for counting nationality not India
umpire_is_not_indian=umpires[umpires['Nationality']!="India"]
number_of_umpires=umpire_is_not_indian.groupby('Nationality')[['Umpire']].count()

# plotting dataset
sns.set_style("darkgrid")
plt.title("Numbers of Umpires from different countries.")
plt.figure(figsize=(12, 6))
sns.barplot(y=number_of_umpires.index,
            x=number_of_umpires.Umpire)
plt.yticks(rotation=50)
plt.savefig('./output/problem_3.png')
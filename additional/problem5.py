import csv
import matplotlib.pyplot as plt
import seaborn as sns

data=dict()
matches=open('./data/matches.csv', 'r')
deliveries=open('./data/deliveries.csv', 'r')

my_matches = csv.reader(matches, delimiter=",")
my_deliveries = csv.reader(deliveries, delimiter=",")
 
matches_id_in_2016=[]
for match in my_matches:
    if match[1]=="2016":
        matches_id_in_2016.append(match[0])

for deliver in my_deliveries:
    for id in matches_id_in_2016:
        if deliver[0]==id and deliver[16]!=0:
            if deliver[3] in data:
                data[deliver[3]]+=int(deliver[16])
            else:
                data[deliver[3]]=int(deliver[16])
# Plot for extra runs runs conceded in the year 2016
sns.set_style("darkgrid")
plt.figure(figsize=(12, 7))
plt.title("Extra runs conceded per team in the year 2016")
plt.xlabel("Teams in the year 2016")
plt.ylabel("Extra runs per team")
plt.bar(*zip(*data.items()))
plt.xticks(rotation=10)
plt.savefig("./output/problem_5.png")
matches.close()
deliveries.close()
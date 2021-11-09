import csv
import operator
import matplotlib.pyplot as plt
import seaborn as sns

runs_by_player=dict()

balls_by_player=dict()

values_of_runs_by_player=[]

values_of_balls_by_player=[]

names_of_players=[]

cache=[]

pair_of_names_values=[]

result_dictionary_for_plot=dict()

# Reading files without pandas module
matches=open('./data/matches.csv', 'r')
deliveries=open('./data/deliveries.csv', 'r')

my_matches = csv.reader(matches, delimiter=",")
my_deliveries = csv.reader(deliveries, delimiter=",")


# Top 10 Lowest Economy Rate of Bowlers in 2015
matches_id_in_2015=[]
for match in my_matches:
    if match[1]=="2015":
        matches_id_in_2015.append(match[0])

for deliver in my_deliveries:
    for id in matches_id_in_2015:
        if deliver[0]==id:
            if deliver[8] in runs_by_player:
                runs_by_player[deliver[8]]+=int(deliver[17])
            else:
                runs_by_player[deliver[8]]=int(deliver[17])
            if deliver[8] in balls_by_player:
                balls_by_player[deliver[8]]+=1
            else:
                balls_by_player[deliver[8]]=1
            if int(deliver[13])>0 or int(deliver[10])>0:
                balls_by_player[deliver[8]]-=1

for key,value in runs_by_player.items():
    names_of_players.append(key)
    values_of_runs_by_player.append(value)
for key,value in balls_by_player.items():
    values_of_balls_by_player.append(value)

for i in range(len(values_of_balls_by_player)):
    cache.append("{:.2f}".format(values_of_runs_by_player[i]/(values_of_balls_by_player[i]/6)))

for i in range(len(names_of_players)):
    pair_of_names_values.append([names_of_players[i],cache[i]])

for i in pair_of_names_values:
    if i[0] not in result_dictionary_for_plot:
        result_dictionary_for_plot[i[0]]=i[1]

top_10_economical_bowlers=sorted((float(y),x) for x,y in result_dictionary_for_plot.items())
top_10_economical_bowlers_dict=dict()
top_10_economical_bowlers_slice=slice(0,10)
for i in top_10_economical_bowlers[top_10_economical_bowlers_slice]:
    if i[1] not in top_10_economical_bowlers_dict:
        top_10_economical_bowlers_dict[i[1]]=i[0]

# plot for top 10 economical bowlers
sns.set_style("darkgrid")
plt.figure(figsize=(12, 7))
plt.title("Extra runs conceded per team in the year 2016")
plt.xlabel("Bowlers")
plt.ylabel("Economy")
plt.bar(*zip(*top_10_economical_bowlers_dict.items()))
plt.xticks(rotation=-10)
plt.savefig("./output/problem_6.png")
matches.close()
deliveries.close()




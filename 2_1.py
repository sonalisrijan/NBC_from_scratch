import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 

value = sys.argv[1]
dating = pd.read_csv(value)

# dating = pd.read_csv("./dating.csv")
# print (dating.columns)

females = dating[dating.gender == 0]
list_women = []
# print (len(females)) # 3309 females

males = dating[dating.gender == 1]
list_men = []
# print (len(males))

preference_scores_of_participant = ['attractive_important', 'sincere_important', 'intelligence_important','funny_important', 'ambition_important', 'shared_interests_important']
for attribute in preference_scores_of_participant:  
    print ("In women, the mean %s is %.2f" %(attribute, females[attribute].mean()))
    list_women.append(females[attribute].mean())
    print ("In men, the mean %s is %.2f" %(attribute, males[attribute].mean()))
    list_men.append(males[attribute].mean())

# print (list_women)
# print (list_men)
barWidth = 0.25
r1 = np.arange(len(list_women))
r2 = [x + barWidth for x in r1]

plt.bar(r1, list_women, color='#FF69B4', width=barWidth, edgecolor='white', label='women')
plt.bar(r2, list_men, color='#0000A0', width=barWidth, edgecolor='white', label='men')
plt.xticks([r + barWidth for r in range(len(list_women))], ['attractive', 'sincere', 'intelligence','funny', 'ambition', 'shared_interests'])
plt.xlabel('Attributes')
plt.ylabel('Mean values')
plt.legend(loc='upper right')
plt.savefig('./Q2_1.png')
plt.show()

# Answer: Here, it's seen that men find attractiveness to be the most important factor in their romantic partners. 
# Women find intelligence to be the most desirable trait in their romantic partners. 
# Also, men do not feel ambition of partner is an important factor in deciding partners. 
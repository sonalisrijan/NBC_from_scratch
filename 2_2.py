import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 

attribute = sys.argv[1]
attribute_value = sys.argv[2]

dating = pd.read_csv("./dating.csv")

# Part a.  
col = dating[attribute]
# print (col)
vals = list(col)
# print (vals)
unique_vals = set(vals)
# print (unique_vals)
# print (len(unique_vals))
print ("The number of distinct values for the attribute " + str(attribute) + " is " + str(len(unique_vals)))

# print (dating[attribute])

# Part b.
numer = dating[(dating[attribute] == float(attribute_value)) & (dating.decision == 1)]
# print (len(numer))

denom = dating[dating[attribute] == float(attribute_value)] 
# print (denom)
# print (len(denom))

success_rate = len(numer)/len(denom)
# print (success_rate)
print ("Success rate for people with attribute %s equal to %d is %.2f"  %(attribute, float(attribute_value), success_rate))

# -----------
# Part c and d.
rating_from_participant = {'attractive_partner':[], 'sincere_partner':[], 'intelligence_parter':[],'funny_partner':[], 'ambition_partner':[], 'shared_interests_partner':[]}
for attribute in rating_from_participant:
    col = dating[attribute] # a dataframe
    vals = list(col)
    unique_vals = list(set(vals)) # all distinct values for given attribute
    
    rating_from_participant[attribute] = unique_vals

# print (rating_from_participant) 
print ("\n")# dict with key: value = attribute:[unique values]
for key in rating_from_participant:
    x = []
    y = []
#     print (key)
#     print (key, rating_from_participant[key])
    for value in rating_from_participant[key]:
        x.append(value)
#         print (value)
        denom = dating[dating[key] == value] 
#         print (len(denom))
        numer = dating[(dating[key] == value) & (dating.decision == 1)]
#         print (len(numer))
        success_rate = len(numer)/len(denom)
        y.append(success_rate)
        print ("Success rate for people with attribute %s equal to %.2f is %.2f" %(key, value, success_rate))
    # print (x,y)
    
    plt.scatter(x, y, alpha=0.5)
    plt.title('Scatter plot for attribute: ' + str(key))
    plt.xlabel(str(key))
    plt.ylabel('success rate')
    plt.savefig('./Q2_2_'+str(key)+'.png')
    plt.show()
    print ("------")
# Observation from these plots: Most desirable trait (one with maximum slope) and least important trait for success



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

value = sys.argv[1]
out_filename = sys.argv[2]

continuous_dating_min_max = {'age': (18,58), 'age_o': (18,58),
       'importance_same_race':(0,10), 'importance_same_religion':(0,10), 
       'pref_o_attractive':(0,1), 'pref_o_sincere':(0,1), 'pref_o_intelligence':(0,1),
       'pref_o_funny':(0,1), 'pref_o_ambitious':(0,1), 'pref_o_shared_interests':(0,1),
       'attractive_important':(0,1), 'sincere_important':(0,1), 'intelligence_important':(0,1),
       'funny_important':(0,1), 'ambition_important':(0,1), 'shared_interests_important':(0,1),
       'attractive':(0,10), 'sincere':(0,10), 'intelligence':(0,10), 'funny':(0,10), 'ambition':(0,10),
       'attractive_partner':(0,10), 'sincere_partner':(0,10), 'intelligence_parter':(0,10),
       'funny_partner':(0,10), 'ambition_partner':(0,10), 'shared_interests_partner':(0,10),
       'sports':(0,10), 'tvsports':(0,10), 'exercise':(0,10), 'dining':(0,10), 'museums':(0,10), 'art':(0,10), 'hiking':(0,10),
       'gaming':(0,14), 'clubbing':(0,10), 'reading':(0,13), 'tv':(0,10), 'theater':(0,10), 'movies':(0,10), 'concerts':(0,10),
        'music':(0,10), 'shopping':(0,10), 'yoga':(0,10), 'interests_correlate':(-1,1),'expected_happy_with_sd_people':(0,10),
        'like':(0,10)}


def discretize(num_bins):
    
    dating = pd.read_csv(value)
    
    continuous_dating_min_max = {'age': (18,58), 'age_o': (18,58),
           'importance_same_race':(0,10), 'importance_same_religion':(0,10), 
           'pref_o_attractive':(0,1), 'pref_o_sincere':(0,1), 'pref_o_intelligence':(0,1),
           'pref_o_funny':(0,1), 'pref_o_ambitious':(0,1), 'pref_o_shared_interests':(0,1),
           'attractive_important':(0,1), 'sincere_important':(0,1), 'intelligence_important':(0,1),
           'funny_important':(0,1), 'ambition_important':(0,1), 'shared_interests_important':(0,1),
           'attractive':(0,10), 'sincere':(0,10), 'intelligence':(0,10), 'funny':(0,10), 'ambition':(0,10),
           'attractive_partner':(0,10), 'sincere_partner':(0,10), 'intelligence_parter':(0,10),
           'funny_partner':(0,10), 'ambition_partner':(0,10), 'shared_interests_partner':(0,10),
           'sports':(0,10), 'tvsports':(0,10), 'exercise':(0,10), 'dining':(0,10), 'museums':(0,10), 'art':(0,10), 'hiking':(0,10),
           'gaming':(0,14), 'clubbing':(0,10), 'reading':(0,13), 'tv':(0,10), 'theater':(0,10), 'movies':(0,10), 'concerts':(0,10),
            'music':(0,10), 'shopping':(0,10), 'yoga':(0,10), 'interests_correlate':(-1,1),'expected_happy_with_sd_people':(0,10),
            'like':(0,10)}

    def get_interval(mini, maxi, n):
        list1 = []
        #return a list of tuple of n bins
        increment = (maxi - mini)/n 
        for a in range (0,n):   # for a in range (0,n+1):
#             print (mini)
            list1.append(mini)
            mini = mini+increment
        list1.append(float(maxi))
#         print (list1)
        return list1

    def bin_column(attribute, num_bins):   # This function does binning for specified attribute in dataframe
        a = continuous_dating_min_max[attribute] # a = tuple(min, max) , ie, the value of key in the dictionary
        mini = a[0]
        maxi = a[1]
        intervals = get_interval(mini, maxi, num_bins) # using the previous get_interval function, the interval for each bin
        labels_list = np.arange(num_bins)
        print (labels_list)
        # print (intervals)
        dating[attribute] = pd.cut(dating[attribute], intervals, labels = labels_list, include_lowest = True) 

    for attribute in continuous_dating_min_max.keys():
        bin_column(attribute, num_bins)
    #     # print (str(attribute), intervals)
    #     print (str(attribute) + ":" + str(dating[attribute].value_counts().tolist()))
        # sort_index().
    return dating

binned_dating = discretize(5)

for attribute in continuous_dating_min_max.keys():
    # bin_column(attribute, num_bins)
    # print (str(attribute), intervals)
    print (str(attribute) + ":" + str(binned_dating[attribute].value_counts().tolist()))
    # sort_index().


binned_dating.to_csv(out_filename, index = False)
# print (binned_dating.to_csv)





import pandas as pd
import re 
import sys

value = sys.argv[1]
dating = pd.read_csv(value)

## Q1-i
race_apos = dating[dating.race.str.contains('\'')]
a = len(race_apos)
race_o_apos = dating[dating.race_o.str.contains('\'')]
b = len(race_o_apos)
field_apos = dating[dating.field.str.contains('\'')]
c = len(field_apos)
dating["race"] = dating["race"].replace({'\'': ''}, regex = True)
dating["race_o"] = dating["race_o"].replace({'\'': ''}, regex = True)
dating["field"] = dating["field"].replace({'\'': ''}, regex = True)
print ("Quotes removed from " + str(a+b+c)+ " cells")


## Q1-ii
field_upper = dating[dating.field.str.contains('[A-Z]')]
dating["field"] = dating["field"].apply(lambda x: x.lower()) # converting to lowercase
print ("Standardized %d cells to lower case." %(len(field_upper)))


## Q1-iii
dating = dating.sort_values(by=['gender'])
dating['gender'] = dating.gender.map({'female': 0, 'male': 1})
print ("Value assigned for male in column gender: " + str(1))

list_of_races = dating.race.unique()
dating = dating.sort_values(by=['race'])
dating['race'] = dating.race.map({'Asian/Pacific Islander/Asian-American':0, 'Black/African American':1, 'European/Caucasian-American':2, 'Latino/Hispanic American':3, 'Other':4 })
print ("Value assigned for European/Caucasian-American in column race: " + str(2))

dating = dating.sort_values(by=['race_o'])
dating['race_o'] = dating.race_o.map({'Asian/Pacific Islander/Asian-American':0, 'Black/African American':1, 'European/Caucasian-American':2, 'Latino/Hispanic American':3, 'Other':4 })
print ("Value assigned for Latino/Hispanic American in column race_o:" + str(3))

dating = dating.sort_values(by=['field']) 
list_of_fields = dating.field.unique() 
dict_fields = { list_of_fields[i] : i  for i in range(0, len(list_of_fields) ) } # Making a sorted dictionary with field_name:value
dating['field'] = dating.field.map(dict_fields) 
print ("Value assigned for law in column field: " + str(dict_fields["law"]))

## Q1-iv
preference_scores_of_partner = ['pref_o_attractive', 'pref_o_sincere', 'pref_o_intelligence', 'pref_o_funny', 'pref_o_ambitious', 'pref_o_shared_interests']
total = sum(dating[j] for j in preference_scores_of_partner) # sum of all these attributes for one person
dating['sum_partner'] = total # created a separate column named total for total of preference_scores_of_partner
# print (dating.pref_o_sincere)
for a in preference_scores_of_partner: # attribute in list
    dating[a] = dating[a]/dating.sum_partner
    mean_of_partner_attribute = dating[a].mean()
    print ("Mean of %s : %.2f" %(a, mean_of_partner_attribute))
    # print ("Mean of " + str(a)+ ": "+ str(round(mean_of_partner_attribute, 2)))

preference_scores_of_participant = ['attractive_important', 'sincere_important', 'intelligence_important','funny_important', 'ambition_important', 'shared_interests_important']
sum_participant = sum(dating[k] for k in preference_scores_of_participant) # sum of all these attributes for one person
dating['total'] = sum_participant # created a separate column named total for total of preference_scores_of_participant
for j in preference_scores_of_participant: # attribute in list
    dating[j] = dating[j]/dating.total
    mean_of_attribute = dating[j].mean()
    print ("Mean of " + str(j)+ ": "+ str(round(mean_of_attribute, 2)))

dating = dating.drop(['sum_partner', 'total'], axis = 1)
dating.to_csv(r"./dating.csv", index = None, header = True)
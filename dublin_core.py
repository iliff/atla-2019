# will start with basic script and then show problem with subjects
# data in ist9077
import pandas as pd
from dcxml import simpledc

# df is a name or variable that we use to store a DataFrame
# we read rows of csv file and make a DataFrame named df
df = pd.read_csv('dc_sample.csv')

# what does the data look like? Do we need to do anything to it?
# How can we stop code after looking at data?

# empty values are read in as NaN, which can be difficult to work with
# so, we take all empty values and make them an empty string
df = df.fillna('')


list_of_dicts = df.to_dict(orient='records')

for dictionary in list_of_dicts:
    '''
    new_dict = {key: [value] for key, value in dictionary.items()}
    '''
    new_dict = {} # we don't need this
    for key, value in dictionary.items(): # can't we just say dictionary here? 
        if key == 'subjects':
            list_values = value.split(',')
        else:
            list_values = [value]

        new_dict[key] = list_values # dictionary[key] = [value]
    xml = simpledc.tostring(new_dict)
    fn = new_dict['identifiers'][0]

    with open('xml/' + fn + '.xml', mode='w', encoding='utf8') as fp:
        fp.write(xml)

dc_dict = {}
        
# either need 2 for loops here, 1 to loop through rows and one to 
# loop through each column of each row. 
# in one sense, line 18 saves this step by propagating the the column names
# into each row as keys

# i think pandas has an interitems option that may save a loop. 
# as long as we can get column name and value from each item.
for index, column, value in df.iteritmes():
    dc_dict[column] = [value]
    
# still need to break on row cause we need a single dictionary per row
# this is what to_dict does in 1 line
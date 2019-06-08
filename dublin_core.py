#!/usr/bin/env python
​
import pandas as pd
from dcxml import simpledc
​
# df is a name or variable that we use to store a DataFrame
# we read rows of csv file and make a DataFrame named df
df = pd.read_csv('dc_sample.csv')

# what does the data look like? Do we need to do anything to it?
# How can we stop code after looking at data?

​# empty values are read in as NaN, which can be difficult to work with
# so, we take all empty values and make them an empty string
df = df.fillna('')
​

list_of_dicts = df.to_dict(orient='records')
​
for dictionary in list_of_dicts:
    '''
    new_dict = {key: [value] for key, value in dictionary.items()}
    '''
    new_dict = {}
    for key, value in dictionary.items():
        list_values = [value]
        new_dict[key] = list_values
    xml = simpledc.tostring(new_dict)
    fn = new_dict['identifiers'][0]
​
    with open(fn + '.xml', mode='w', encoding='utf8') as fp:
        fp.write(xml)
​
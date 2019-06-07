#!/usr/bin/env python
​
import pandas as pd
from dcxml import simpledc
​
df = pd.read_csv('https://raw.githubusercontent.com/msaxton/atla2019_workshop/master/dc_sample.csv')
​
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
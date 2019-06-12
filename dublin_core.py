# will start with basic script and then show problem with subjects
# data in ist9077
import pandas as pd
from dcxml import simpledc
import os

os.makedirs("xml", exist_ok=True)
# df is a name or variable that we use to store a DataFrame
# we read rows of csv file and make a DataFrame named df
df = pd.read_csv('dc_sample.csv')

# what does the data look like? Do we need to do anything to it?
# How can we stop code after looking at data?

# empty values are read in as NaN, which can be difficult to work with
# so, we take all empty values and make them an empty string
df = df.fillna('')

# Let's look at ist0977.xml, what do we notice about the subject item?
# How might we address this?
# Let's look at all the rows that have a comma in subject
# What do we learn?
# How might we address the larger issue?
# Could we fix the data in the file using python?

list_of_dicts = df.to_dict(orient='records')

for dictionary in list_of_dicts:
    for key, value in dictionary.items():
        dictionary[key] = [value]

    xml = simpledc.tostring(dictionary)
    fn = dictionary['identifiers'][0]

    with open('xml/' + fn + '.xml', mode='w', encoding='utf8') as fp:
        fp.write(xml)
#!/usr/bin/env python3
'''Taking the code we wrote, this is creating a script that we can call from the command line to create the xml files
per record. The main purpose of this is to see the structure of a python script that can be reused.'''

import sys
import pandas as pd
from dcxml import simpledc
# pip install xlrd


def dictionary2xml(dictionary):
    '''takes a dictionary and creates an xml string from the object, and the file name'''
    new_dict = {}
    for key, value in dictionary.items():
        list_value = [value]
        new_dict[key] = list_value
    xml = simpledc.tostring(new_dict)
    file_name = dictionary['identifiers']
    return xml, file_name


def main():
    '''The main function will hand the file input and output for the script'''
    import_file = sys.argv[1]
    df = pd.read_excel(import_file)
    df = df.fillna('')
    list_of_dicts = df.to_dict(orient='records')
    for dictionary in list_of_dicts:
        xml, file_name = dictionary2xml(dictionary)
        with open(file_name + '.xml', mode='w', encoding='utf8') as fp:
            fp.write(xml)


if __name__ == '__main__':
    '''Python tries to limit the boiler plate type code, and this is some of the limited boiler plate we have. 
    The main purpose for this code is that if the script is imported into another script the main function will not 
    be called.'''
    main()

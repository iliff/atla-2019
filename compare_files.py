import pandas as pd

# load data
ebooks1_df = pd.read_csv('https://raw.githubusercontent.com/msaxton/atla2019_workshop/master/ebooks1.csv')
ebooks2_df = pd.read_csv('https://raw.githubusercontent.com/msaxton/atla2019_workshop/master/ebooks2.csv')

# prepare data
ebooks2_df['ISBN'] = ebooks2_df['ISBN'].str.replace('-', '')  # remove dashes from ebooks2 data
ebooks2_df['ISBN'] = ebooks2_df['ISBN'].astype('float64')  # change the datatype to match ebooks1 data

# transform data
ebooks2_unique_df = ebooks2_df.loc[~ebooks2_df['ISBN'].isin(ebooks1_df['ISBN'])]
ebooks2_duplicate_df = ebooks2_df.loc[ebooks2_df['ISBN'].isin(ebooks1_df['ISBN'])]

# How could we write the duplicate line with pd.merge?

# inspect results
# ebooks2_df.to_csv('/home/ubuntu/Downloads/ebooks2-unique.csv')
print(ebooks2_unique_df.shape)
print(ebooks2_unique_df)
# add a break then use run with debug to view full dataframes

# Advanced Matching

from fuzzywuzzy import fuzz
title_dict_list = ebooks1_df[['ISBN', 'Title']].to_dict(orient='record')
title_dict = {}
for title in title_dict_list:
  title_dict[title['ISBN']] = title


def title_matcher(row, title_dict_list, title_dict):
  matches = []
  try:
    title_match = title_dict[row['ISBN']]
    return title_match['Title']
  except KeyError:
    pass
  for title in title_dict_list:
    fuzzratio = fuzz.ratio(row['Title'].lower(), title['Title'].lower())
    if fuzzratio > 90:
      matches.append((title['ISBN'], title['Title']))
  titles = '; '.join(m[1] for m in matches)
  return titles

ebooks2_df['Title_Match'] = ebooks2_df.apply(lambda x: title_matcher(x, title_dict_list, title_dict), axis=1)  #, axis=1)

match_df = ebooks2_df[ebooks2_df['Title_Match'] != '']

match_df[['Title', 'Title_Match', 'ISBN']]

duplicate[['Title_x', 'Title_y']]

ebooks2_df.iloc[10]

# Finding the duplicate
ebooks1_df[ebooks1_df['Title'].str.contains('Christian Theology')]


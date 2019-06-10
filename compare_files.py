import pandas as pd

ebooks1_df = pd.read_csv('https://raw.githubusercontent.com/msaxton/atla2019_workshop/master/ebooks1.csv')
ebooks2_df = pd.read_csv('https://raw.githubusercontent.com/msaxton/atla2019_workshop/master/ebooks2.csv')

ebooks1_df['ISBN'].dtypes == ebooks2_df['ISBN'].dtypes

ebooks2_df['ISBN'] = ebooks2_df['ISBN'].str.replace('-', '')  # remove dashes from ebooks2 data
ebooks2_df['ISBN'] = ebooks2_df['ISBN'].astype('float64')  # change the datatype to match ebooks1 data

ebooks2_unique_df = ebooks2_df.loc[~ebooks2_df['ISBN'].isin(ebooks1_df['ISBN'])]
ebooks2_duplicate_df = ebooks2_df.loc[ebooks2_df['ISBN'].isin(ebooks1_df['ISBN'])]
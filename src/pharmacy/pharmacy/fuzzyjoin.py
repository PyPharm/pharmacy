__version__ = '0.3.2'

# pip install fuzzywuzzy[speedup]   to
from thefuzz import fuzz, process
import pandas as pd
from pathlib import Path

parent_dir = Path.cwd().parent
example_a = parent_dir / 'examples\example a.xlsx'


def find_best_matches(df_orig
                      , df2
                      , match_col
                      , match_col_comparator = None   # optionally the name of the column in the comparator table
                      , threshold=80
                      , scorer=fuzz.token_set_ratio    # options: ratio, partial_ratio, token_sort_ratio, token_set_ratio
                      #, cols_to_keep = None        # TODO: create this feature
                      ):
    # ---------------------------------------------------------------------------------------------------------------
    # Setup
    best_matches = []
    assert type(df_orig) == pd.DataFrame
    assert type(df2) == pd.DataFrame

    #TODO: add a "use up" mode where each match in the comparator table can only be used up by its best match in the
    #    original table

    # if no comparator column is named, look for the same name as the original.
    if not match_col_comparator:
        match_col_comparator = match_col
    df_merge = df_orig.copy()
    df_matches = pd.DataFrame()

    # ---------------------------------------------------------------------------------------------------------------
    # Match
    # begin the match
    for index_o, row_o in df_orig.iterrows():

        # Change column names on comparator
        name_o = row_o[match_col]

        best_match, score, idx = process.extractOne(name_o, df2[match_col_comparator], scorer=scorer)

        if   score >= threshold:
            new_row = pd.Series(data={'orig_index': index_o, 'match_score':score})
            #new_row['orig_index'] = index_o
            new_row = pd.concat( [new_row , df2.loc[idx].copy()])
            print(new_row)

            df_matches = df_matches._append(new_row, ignore_index=True)


    df_matches.set_index('orig_index', inplace=True)

    df_merge = df_orig.merge(df_matches
                             , how='left'
                             , left_index=True
                             , right_on='orig_index'
                             , suffixes=('','_y'))
    print(df_merge)

    # Convert the columns with NaN values back to their original data types
    # from ChatGPT - not sure about this yet.
    #df_merge['value_right'] = df_merge['value_right'].combine_first(df_merge['value_left'])
    #merged_df.drop(['value_left'], axis=1, inplace=True)
    #merged_df.rename(columns={'value_right': 'value'}, inplace=True)


    # TODO: fix data types from merged-in columns after the merge.  Adding NaN damages the types.

    # after all the matches are done, concat the resulting matches dataframe
    return df_merge     # best_matches

if __name__ == "__main__":
    df1 = pd.read_excel(example_a, sheet_name='data 1')
    df2 = pd.read_excel(example_a, sheet_name='data 2')
    # Example usage


    best_matches = find_best_matches(df1, df2, match_col='name' , threshold=90)

    print(best_matches)


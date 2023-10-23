__version__ = '0.2.8'

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
                      , threshold=0
                      , scorer=fuzz.token_set_ratio    # options: ratio, partial_ratio, token_sort_ratio, token_set_ratio
                      , cols_to_keep = None):
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
    df_matches = df_orig.copy()


    # ---------------------------------------------------------------------------------------------------------------
    # Match
    # begin the match
    for index_o, row_o in df_orig.iterrows():

        name_o = row_o[match_col]

        best_match, score, idx = process.extractOne(name_o, df2[match_col_comparator], scorer=scorer)
        print(best_match)

        if  True:   # score >= threshold:
            best_matches.append((row_o, df2[df2[match_col_comparator] == best_match].iloc[0]))

            # deposit data from the match into the copy of the original.
            df_matches.loc[idx, 'test'] = best_match
            df_matches.loc[idx, 'match_score'] = score

    return df_matches     # best_matches

if __name__ == "__main__":
    df1 = pd.read_excel(example_a, sheet_name='data 1')
    df2 = pd.read_excel(example_a, sheet_name='data 2')
    # Example usage


    best_matches = find_best_matches(df1, df2, match_col='name' , threshold=90)

    print(best_matches)


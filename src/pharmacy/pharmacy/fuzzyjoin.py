__version__ = '0.2.0'

# pip install fuzzywuzzy[speedup]   to
from fuzzywuzzy import fuzz, process
import pandas as pd
from pathlib import Path

parent_dir = Path.cwd().parent
example_a = parent_dir / 'examples\example a.xlsx'


def find_best_matches(df_orig
                      , df2
                      , match_col
                      , match_col_comparator = None   # optionally the name of the column in the comparator table
                      , threshold=90):
    best_matches = []

    # if no comparator column is named, look for the same name as the original.
    if not match_col_comparator:
        match_col_comparator = match_col
    df_matches = df_orig.copy()

    for index_o, row_o in df_orig.iterrows():
        name_o = row_o[match_col]

        best_match, score, _ = process.extractOne(name_o, df2[match_col_comparator], scorer=fuzz.token_sort_ratio)
        print(best_match)
        if score >= threshold:
            best_matches.append((row_o, df2[df2[match_col_comparator] == best_match].iloc[0]))
            #df_matches.loc[]

    return best_matches

if __name__ == "__main__":
    df1 = pd.read_excel(example_a, sheet_name='data 1')
    df2 = pd.read_excel(example_a, sheet_name='data 2')
    # Example usage


    best_matches = find_best_matches(df1, df2, match_col='name' , threshold=90)

    print(best_matches)


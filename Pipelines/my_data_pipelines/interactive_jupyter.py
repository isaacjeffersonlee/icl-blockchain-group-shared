# Custom wrapper functions
import pandas as pd
from ipywidgets import interact
import ipywidgets as widgets
import textwrap

def scroll_df(df: pd.DataFrame) -> None:
    """
    Print out information for each row interactively.

    Args:
        df (pd.DataFrame): DataFrame to get row data from
    """
    # Instantiate our wrapper object
    # so that we can break long lines when printing strings.
    tw = textwrap.TextWrapper(width=60)

    def print_row_info(row_idx: int, sort_by: str) -> None:
        # Assuming already sorted by 'Index'
        if sort_by != 'Index': 
            sorted_df = df.sort_values(by=sort_by)
        else:
            sorted_df = df.copy()  # Make sure we're not modifying or original dataframe.
        # Get the row corresponding to row_idx
        row = sorted_df.iloc[row_idx]
        # Print information
        print(f"Index: {sorted_df.index[row_idx]}")
        print("-------------------------------------------------")
        print("")
        for col in sorted_df.columns:
            obj = row[col]
            if type(obj) == str:
                print(col + ':')
                for line in tw.wrap(obj):
                    print(line)
                    print("")
            else:
                print(f"{col}: {obj}")
                print("")

    col_list = list(df.columns)
    col_list.append('Index')
    interact(print_row_info,
             row_idx=widgets.IntSlider(min=0, max=df.shape[0]-1, step=1, value=0),
             sort_by=widgets.Dropdown(options=col_list, description='Sort by', value='Index'))

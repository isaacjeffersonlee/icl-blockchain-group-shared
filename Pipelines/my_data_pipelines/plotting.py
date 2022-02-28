import seaborn as sns

def my_seaborn_defaults():
    """Set the default style of seaborn."""
    sns.set()
    sns.set_context("poster")
    palette = 'crest'
    sns.set_palette(palette)
    cont_col = ['#6CB190', '#1D2562'] # when we need two contrasting colours
    sns.color_palette(palette, as_cmap=True)

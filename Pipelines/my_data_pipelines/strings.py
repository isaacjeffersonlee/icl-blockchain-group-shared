def remove_non_alpha(s: str) -> str:
    """
    Remove all characters that are not alphanumeric or spaces.

    Args:
        s (str): String to clean.

    Returns:
        str: cleaned string.
    """
    clean_txt = ''
    for char in s:
        if char.isalnum() or char == ' ':
            clean_txt += char

    return clean_txt

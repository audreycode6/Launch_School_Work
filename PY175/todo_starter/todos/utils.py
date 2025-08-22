MAX_TITLE_LEN = 100


def error_for_title_length(title):
    if not 1 <= len(title) <= MAX_TITLE_LEN:
        return "The title must be between 1 and 100 characters."
    return None

def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    return error_for_title_length(title)


import re


TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes))?'
)


def get_minutes(dom_element):
    try:
        tstring = dom_element.get_text()
        matched = TIME_REGEX.search(tstring)
        minutes = int(matched.groupdict().get('minutes') or 0)
        minutes += 60 * int(matched.groupdict().get('hours') or 0)
        return minutes
    except AttributeError:  # if dom_element not found or no matched
        return 0


def normalize_string(string):
    return string.replace(
        '\xa0', ' ').replace(  # &nbsp;
        '\n', ' ').replace(
        '  ', ' ').strip()

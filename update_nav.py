"""
Updates the navigation in the HTML files
"""
import os

from bs4 import BeautifulSoup

# HIERARCHY
HIERARCHY = {
    "widgets": {
        "label": [],
        "frame": [],
        "button": []
    },
    "geometry": {
        "pack": [],
        "grid": [],
        "place": []
    }
}

PRIMARY_KEYS = HIERARCHY.keys()

NAV_LEVELS = ["primary", "secondary", "tertiary"]

SOUP = BeautifulSoup()

# Returns <nav id="primary">...</nav> tag
def get_primary_nav(tokens):
    first_token = tokens[0] if len(tokens) > 0 else None
    nav = SOUP.new_tag("nav", id="primary")
    for key in PRIMARY_KEYS:
        link = SOUP.new_tag("a", href=f"/{key}/{key}.html")
        link.string = key.capitalize()
        if key == first_token:
            link["class"] = "active"
        nav.append(link)

    return nav

# Returns <nav id="secondary">...</nav> tag
def get_secondary_nav(tokens):
    first_token = tokens[0]
    second_token = tokens[1] if len(tokens) > 1 else None
    secondary_keys = HIERARCHY[first_token].keys()

    nav = SOUP.new_tag("nav", id="secondary")
    for key in secondary_keys:
        link = SOUP.new_tag("a", href=f"/{first_token}/{key}/{key}.html")
        link.string = key.capitalize()
        if key == second_token:
            link["class"] = "active"
        nav.append(link)

    return nav

# Returns <nav id="tertiary">...</nav> tag
def get_tertiary_nav(tokens):
    first_token = tokens[0]
    second_token = tokens[1]
    third_token = tokens[2] if len(tokens) > 2 else None

    nav = SOUP.new_tag("nav", id="tertiary")
    tertiary_keys = HIERARCHY[first_token][second_token]
    for key in tertiary_keys:
        link = SOUP.new_tag("a", href=f"/{first_token}/{second_token}/{key}/{key}.html")
        link.string = key.capitalize()
        if key == third_token:
            link["class"] = "active"
        nav.append(link)

    return nav


# Returns <div id="navigation">...</div> tag
def get_nav(html_file):
    # Get rid of leading dot and trailing html file name
    tokens = html_file.split("/")[1: -1]
    nav_levels = len(tokens)

    div = SOUP.new_tag("div", id="navigation")
    div.append(get_primary_nav(tokens))

    if nav_levels >= 1:
        div.append(get_secondary_nav(tokens))
    if nav_levels == 2:
        div.append(get_tertiary_nav(tokens))

    return div

# Main
for root, _, files in os.walk("."):
    # filter to html files
    html_files = [os.path.join(root, f) for f in files if f.endswith(".html")]

    # Loop over HTML files
    for html_file in html_files:
            # Make soup from html 
            html_soup = BeautifulSoup(open(html_file, "r"), features="html.parser")

            # Create the nav from the file path
            new_div = get_nav(html_file).prettify()

            # Page should have an existing div<id="navigation"> tag
            existing_nav = html_soup.find("div", id="navigation")
            assert existing_nav is not None

            existing_nav.replaceWith(new_div)

            print(html_soup)



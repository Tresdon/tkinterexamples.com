"""
Updates the navigation in the HTML files
"""

import os

hierarchy = {
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


for root, _, files in os.walk("."):
    for file in files:
        full_path = os.path.join(root, file)
        tokens = full_path.split("/")[1: -1]
        if file.endswith(".html"):
            print(full_path, tokens)
            print(tokens))


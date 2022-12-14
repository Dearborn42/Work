import json

def reset():
    """Function that wipes json data"""
    # take all text from template.txt and put it into people.txt
    with open("template.txt", "r") as file:
        template = file.read()
        with open("people.json", "w") as file:
            file.write(template)
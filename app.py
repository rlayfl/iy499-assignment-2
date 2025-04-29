# Richard Lay-Flurrie
# Text-based game for IY499 Introduction to Programming Assignment 2

import time

def print_text_slowly(text, delay=0.02):
    """Prints text slowly to the console."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end

    time.sleep(1)

def read_story_from_json_file(file_path):
    """Reads the story from a JSON file."""
    import json
    with open(file_path, 'r') as file:
        story = json.load(file)
    return story

def main():

    story = read_story_from_json_file("story.json")

    print_text_slowly(story['chapters'][0]['title'])

    for paragraph in story['chapters'][0]['paragraphs']:
        print_text_slowly(paragraph)

if __name__ == "__main__":
    main()
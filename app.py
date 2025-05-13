# Richard Lay-Flurrie
# Text-based game for IY499 Introduction to Programming Assignment 2

import time

def print_text_slowly(text, delay=0.020):
    """Prints text slowly to the console."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

    time.sleep(1)

def read_story_from_json_file(file_path):
    """Reads the story from a JSON file."""
    import json
    with open(file_path, 'r') as file:
        story = json.load(file)
    return story

def read_state_from_json_file(file_path):
    """Reads the state from a JSON file."""
    import json
    with open(file_path, 'r') as file:
        state = json.load(file)
    return state

def get_soldiers_from_json_file(file_path):
    """Reads the soldiers from a JSON file."""
    import json
    with open(file_path, 'r') as file:
        soldiers = json.load(file)
    return soldiers

def get_event_types_from_json_file(file_path):
    """Reads the events from a JSON file."""
    import json
    with open(file_path, 'r') as file:
        events = json.load(file)
    return events

def get_youngest_soldier(soldiers):
        """Returns the soldier with the lowest age."""
        return min(soldiers, key=lambda soldier: soldier['age'])

def get_amount_of_soldiers(soldiers):
    """Returns the amount of soldiers."""
    return len(soldiers)

def game_running():

    while True:

        state = read_state_from_json_file("state.json") # Get the state from the JSON file.
        print_text_slowly(f"Current state: {state['weather']["condition"]}")

        event_types = get_event_types_from_json_file("event_types.json") # Get events from the JSON file.

        soldiers = get_soldiers_from_json_file("soldiers.json")

        youngest_soldier = get_youngest_soldier(soldiers)
        print_text_slowly(f"Youngest soldier: {youngest_soldier['name']} (Age: {youngest_soldier['age']})")

        # Get a random number between 1 and 5. This will be the number of events to happen.

        # Events will be available based on previous events.

        

def main():

   game_running()
        
if __name__ == "__main__":
    main()
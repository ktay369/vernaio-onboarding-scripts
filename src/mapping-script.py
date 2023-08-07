import json
import uuid
import os

# Get the directory of the current script
# script_dir = os.path.dirname(os.path.abspath(__file__))
# print(script_dir)

# Read the input JSON file
input_file_path = '../input/metadata.json'
output_file_path = 'mapping.json'

# Check if the output file already exists
if os.path.exists(output_file_path):
    raise Exception(f"Output file '{output_file_path}' already exists. Script processing terminated.")


with open(input_file_path, 'r') as input_file:
    json_data = json.load(input_file)

# Create a new list to hold the new entries
new_entries = {}

# Loop through each entry in the JSON and add a new key-value pair
# for entry in json_data:
#     user_id = entry['id']
#     uuid = str(uuid.uuid4())
#     entry[user_id] = uuid

# Loop through each entry in the input JSON data
for entry in json_data["signals"]:
    try:
        # Attempt to get the user_id from the entry
        user_id = entry["id"]
    except KeyError:
        # Handle the case where "id" field is missing in the entry
        raise Exception("Error: 'id' field not found in an entry.")

    # Generate a new UUID
    unique = uuid.uuid4()

    # Add a new key-value pair to the new_entries dictionary
    new_entries[user_id] = str(unique)

# Write the new entries to a separate JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(new_entries, output_file, indent=4)

print(f"Modified JSON written to {output_file_path}")
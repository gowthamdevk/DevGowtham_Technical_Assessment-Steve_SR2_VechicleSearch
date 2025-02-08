import re

def extract_vehicle_numbers(filepath):
    """Extracts vehicle registration numbers from the provided text.
    This regex assumes registrations are of the form:
      - 1-2 uppercase letters
      - 1-2 digits
      - optional whitespace
      - 1-3 uppercase letters"""
    # Read the file content
    content = read_file(filepath)
    pattern = r'\b[A-Z]{1,2}\d{1,2}\s?[A-Z]{1,3}\b'
    return re.findall(pattern, content)

"""Read teh file from the data folder"""
def read_file(filepath):
    """Reads the entire file content and returns it as a string."""
    with open(filepath, 'r') as file:
        return file.read()
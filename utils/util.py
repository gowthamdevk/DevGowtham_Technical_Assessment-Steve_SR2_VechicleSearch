from pathlib import Path

import yaml


def config():
    """
    Load configuration settings from the config.yaml file.

    :return: Dictionary containing configuration settings
    """
    path = Path(__file__).parent / "../config.yaml"  # Define the path to the config file
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)  # Load YAML configuration
        return data
    finally:
        config_file.close()  # Ensure the file is closed properly

def find_vehicle_by_reg(reg_number, expected_vehicle_list):
    """
    Search for a vehicle in the expected data by registration number.

    :param reg_number: The vehicle registration number to search for.
    :param expected_vehicle_list: A list of expected vehicle objects containing registration details.
    :return: The vehicle object if found, otherwise None.
    """
    # Normalize the registration number by removing spaces and converting it to uppercase
    reg_number = reg_number.replace(" ", "").strip().upper()

    # Iterate through the list of expected vehicles
    for vehicle in expected_vehicle_list:
        # Normalize and compare the stored vehicle registration number with the input reg_number
        if vehicle.variant_reg.replace(" ", "").strip().upper() == reg_number:
            return vehicle  # Return the matching vehicle object

    return None  # Return None if no matching vehicle is found

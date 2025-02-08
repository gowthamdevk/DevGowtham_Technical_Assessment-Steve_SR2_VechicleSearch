import csv

# Define a class to represent a vehicle
class Vehicle:
    def __init__(self, variant_reg, make_model, year):
        self.variant_reg = variant_reg
        self.make_model = make_model
        self.year = int(year)  # Convert year to an integer

    def __repr__(self):
        return f"Vehicle(variant_reg='{self.variant_reg}', make_model='{self.make_model}', year={self.year})"

def read_vehicle_data(filepath):
    vehicles = []
    with open(filepath, 'r', newline='') as csvfile:
        # Create a CSV reader that uses the first row as keys
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Create a Vehicle object from each row
            vehicle = Vehicle(
                variant_reg=row['VARIANT_REG'],
                make_model=row['MAKE_MODEL'],
                year=row['YEAR']
            )
            vehicles.append(vehicle)
    return vehicles
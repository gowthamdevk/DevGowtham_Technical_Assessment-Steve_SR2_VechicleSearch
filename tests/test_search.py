# coding=utf-8
from pathlib import Path

import pytest
from selenium.common import TimeoutException

from pages.search_page import SearchPage
from tests.base_test import BaseTest
from utils.vehicle_output_parser import read_vehicle_data
from utils.vehicle_input_parser import extract_vehicle_numbers
from utils.util import find_vehicle_by_reg


class TestSearch(BaseTest):
    """
    A test class for verifying vehicle search functionality using Selenium and data-driven testing.
    """

    @pytest.fixture(autouse=True)
    def load_pages(self):
        """
        Initialize the Search Page object and load test data.
        This method loads expected vehicle data and input vehicle registration numbers.
        """
        self.page = SearchPage(self.driver, self.wait)

        # Define file paths for expected vehicle data and input vehicle numbers
        output_filepath = Path(__file__).parent / "../data/car_output - V5.txt"
        input_filepath = Path(__file__).parent / "../data/car_input - V5.txt"

        # Load vehicle data from the provided files
        self.expected_vehicle_list = read_vehicle_data(output_filepath)
        self.vehicle_numbers = extract_vehicle_numbers(input_filepath)

    def test_search(self):
        """
        Test vehicle search functionality using multiple registration numbers.
        It verifies if the vehicle details match the expected data.
        """
        global message
        failed_cases = []  # List to store failed searches for better reporting
        passed_count = 0   # Counter to track passed test cases

        for registration in self.vehicle_numbers:
            try:
                # Navigate to the search page and perform a search
                self.page.go_to_search_page()
                print(f"Searching for: {registration}")
                self.page.make_a_search(registration)

                # Retrieve search results
                make_model = self.page.get_model()
                year = self.page.get_year()

                # Validate the retrieved data against expected data
                expected_vehicle = find_vehicle_by_reg(registration, self.expected_vehicle_list)
                assert expected_vehicle is not None, "The vehicle reg is not found in the expected output list!"
                assert expected_vehicle.make_model == make_model, "The make and model mismatch error"
                assert str(expected_vehicle.year) == year, "The year mismatch error"

                passed_count += 1  # Increment pass count if no assertion error occurs

            except TimeoutException as e:
                # Handle timeout exceptions (e.g., if registration is not found)
                if self.page.is_reg_not_found_error_thrown():
                    message = "Entered registration number is not correct!"
                    failed_cases.append((registration, message))
                    print(f"❌ Failed for {registration}: {message}")
                else:
                    failed_cases.append((registration, str(e)))
                    print(f"❌ Failed for {registration}: {str(e)}")
            except Exception as e:
                # Handle unexpected errors
                failed_cases.append((registration, str(e)))
                print(f"❌ Failed for {registration}: {str(e)}")

        total_cases = len(self.vehicle_numbers)  # Total number of searches performed

        # Final assertion for test summary
        if failed_cases:
            # Print and log failed cases along with counts
            fail_message = "\n".join([f"{reg}: {err}" for reg, err in failed_cases])
            pytest.fail(f"🚨 {len(failed_cases)} search(es) failed, ✅ {passed_count} passed out of {total_cases}:\n{fail_message}")
        else:
            # If no failures, print a success message
            print(f"✅ All {total_cases} searches passed successfully!")

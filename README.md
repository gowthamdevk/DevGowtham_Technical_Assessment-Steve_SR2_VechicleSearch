# Vehicle-search
# Requirements
* Python 3.12.3
* pip (24.0) and setuptools
* Recommended IDE used is pycharm
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Installation
**_Run below steps only if the .venv is not created in your Project Folder_**

Assuming python, pip and venv are installed correctly:

1. Go to the project root directory
2. Create a virtual environment: 
   - (UBUNTU): `python3 -m venv .venv`
   - (WINDOWS): `py -m venv venv`
3. Activate the virtual environment executing the following script: 
   - (UBUNTU): `source .venv/bin/activate`
   - (WINDOWS): `.\venv\Scripts\activate`
4. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`


# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -v --html=results/report.html`

# Configuration

By default, tests will be executed in Chrome (normal mode). Preferences can be changed in "/data/config.yaml" file

# Results

To check the report, open the '/results/report.html' file once the execution has finished.

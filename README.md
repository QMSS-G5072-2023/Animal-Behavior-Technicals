# Animal Behavior Technicals

This package is designed to study data from the movebank organisation. Movebank is coordinated by the Max Planck Institute of Animal Behavior, the North Carolina Museum of Natural Sciences, and the University of Konstanz and studies movements of animals, different attributes and has a lot of instruments to measure these observations. This package aims to make the techncalities of these instruments easier to work with.

# Installation

This package can be installed using the following: 

```pip install -i https://test.pypi.org/simple/ animal-behavior-technicals==0.1.0```
Following this the package needs to be imported:

```import animal_behavior_technicals```

To access specific functions within the package, make sure you understand the file structure properly.
for example, to know the sensor type, it can be imported from the directory animal_behavior_technicals. (Located in a file called utils)

```from animal_behavior_technicals.utils import get_sensor_type```

# Usage

To download data from the API, first an account needs to be created on movebank. Movebank has a lot of public and private data. TO access private data, a request needs to be sent to the owner.Follow these steps:
```
# Input your Movebank username
username = input("Enter your Movebank username: your_username")

# Use getpass to securely input the password
password = getpass("Enter your Movebank password: *****")

# URL for obtaining the access token
url = "https://www.movebank.org/movebank/service/direct-read?service=request-token"

# Set up the authentication
auth = (username, password)

# Make the request
response = requests.get(url, auth=auth)

# Check the response status
if response.status_code == 200:
    # Request was successful
    access_token = response.text
    print("Access Token:", access_token)
else:
    # Request failed
    print("Error:", response.status_code, response.text)
```
If you are not able to get an access token, an error message will display on the screen. Check your username and password again.
Once you get your access token, use it to access and download the data
```
# Replace '<API-TOKEN>' with the actual access token obtained from the previous step
api_token = 'd4a8b25b-3c3d-4fa6-9787-60bcab8c94b6'

# URL for requesting data
url = f"https://www.movebank.org/movebank/service/direct-read?entity_type=event&study_id=2911040&attributes=all&api-token={api_token}"

# Make the request
response = requests.get(url)

# Check the response status
if response.status_code == 200:
    # Request was successful
    # You can process the data here or save it to a file, for example, CSV
    with open('data-token.csv', 'wb') as file:
        file.write(response.content)
    print("Data successfully retrieved and saved to data-token.csv")
else:
    # Request failed
    print("Error:", response.status_code, response.text)
```
# Codebook
To access the codebook, visit the following link. It will provide a description of each variable and its encodings

```https://www.movebank.org/cms/movebank-content/movebank-attribute-dictionary```

# Tests 
Run the test file test_utils in the tests directory in animal_behavior_technicals.
A result with all tests passes should look like this 
```============================================================== test session starts ==============================================================
platform win32 -- Python 3.7.4, pytest-7.4.3, pluggy-1.2.0
rootdir: C:\Users\arush\animal_behavior_technicals
configfile: setup.cfg
plugins: anyio-3.7.1
collected 8 items

tests\test_animal_behavior_technicals.py ..                                                                                                [ 25%]
tests\test_utils.py ......                                                                                                                 [100%]

=============================================================== 8 passed in 0.11s ===============================================================
```
# Contributing
You are welcome to contribute to this project. Please make sure to abide by the code of conduct of this package and Movebank.

# Python version
This package requires a python version of 3.7 or higher but does not have any dependencies. However Requests will be required to access the API.

# Contact 
arushisaranath@gmail.com 
# License
This package has been created by Arushi Gautam Saranath. (username- arushisaranath) and is licensed under the terms of the MIT license.

# Credits
This  package has been created using Cookiecutter and the gh:audreyr/cookiecutter-pypackage template. Data has been retrieved from movebank.

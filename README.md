# plivo-Temp

## Description

Test case and relevant API support needed to test billing functionality


## Files

libraries > Contains the Libraries to be used by test cases

  \plivoAPI.py > Contains APIs for interaction with plivo cloud

  \rest_utils.py > Contains utils for executing REST CRUD operations

test_scripts > Contains test Scripts

  \conftest.py > py.test file with initial setup for py.test

  \test_Plivo > Automated test Case


## Example Test Run

To be executed from test_scripts folder

py.test test_Plivo.py --auth_id="MAMDA3OTQ5NGI1OWE4NG" --auth_token="NWY4NmQzZGNhYWM2YTFiMmJmZDRjMTgwMmRlMmZj" --seed=76922 --country_iso="US" -s  


import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "T8d5ESrkveg48hjitA2nFz2W74WSAjA1A0R1mtbH"
query_params = {"api_key": api_key, "earth_date": "2023-01-05"}
response = requests.get(endpoint, params=query_params)
response
response.json()
{'photos': {'id': 754118,
   'sol': 2809,
   'camera': {'id': 20,
    'name': 'FHAZ',
    'rover_id': 5,
    'full_name': 'Front Hazard Avoidance Camera'},
   'img_src': 'https://mars.nasa.gov/msl-raw-images/...JPG',
   'earth_date': '2023-01-05',
   'rover': {'id': 5,
    'name': 'Curiosity',
    'landing_date': '2012-08-06',
    'launch_date': '2011-11-26',
    'status': 'active'}},
}

photos = response.json()["photos"]
print(f"Found {len(photos)} photos")
photos[4]["img_src"]
'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02809/opgs/edr/rcam/RRB_646869036EDR_F0810628RHAZ00337M_.JPG'
print()
import requests

url = "https://coronavirus-map.p.rapidapi.com/api/v1/regions"

headers = {
    'x-rapidapi-key': "5cd812677amsha305995d67d37f3p1f3edcjsn46eaa6ae5983",
    'x-rapidapi-host': "coronavirus-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

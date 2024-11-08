import http.client

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "dc742b2619msh18622996d919c7fp148b94jsnff34cbfd9239"
    }

conn.request("GET", "/odds?season=2019&bet=1&bookmaker=6&fixture=157140&league=39", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

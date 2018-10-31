
import requests


resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
print(type(countries))
for c in countries:
    print("%-55s %-20s %d" % (c["name"], c["capital"], c["population"]))




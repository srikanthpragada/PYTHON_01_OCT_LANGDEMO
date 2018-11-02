import requests

resp = requests.get(r"https://restcountries.eu/rest/v2/all")
countries = resp.json()


def get_country_name(code):
    for c in countries:
        if c["alpha3Code"] == code:
           return c["name"]

    return None


def print_information(c):
    print("Name : " + c["name"])
    print("Capital : " + c["capital"])
    print("Population : " + str(c["population"]))
    print("Sharing borders with :")

    for code in c["borders"]:
        print(get_country_name(code))


while True:
    code = input("\nEnter country code [end to stop] :")
    if code == "end":
        break

    # Look for country code in the list
    for c in countries:
         if c["alpha2Code"] == code:
             print_information(c)
             break
    else:
       print("Sorry! Country not found!")

import requests


def fetch_data(option):
    data = []
    try:
        url = f"https://swapi.mimo.dev/api/{option}/"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(len(data))
    except requests.HTTPError as e:
        print(e)
        return None
    return data


option = input("What do you want? ")
option = option.replace(" ", "")
option = option.lower()
data = fetch_data(option)

if data:
    for key in data:
        print(key["name"])
else:
    print("Unable to download data")

import json

f = open("behandling/countries.json", "r") # OBS: Spør om du får feilmelding her
land = json.loads(f.read())

# Iterer gjennom alle landene i landet
for l in land:
    print(l["name"]["common"])
    print(l["region"])
    
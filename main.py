from star_wars_api import StarWarsApi

api_client = StarWarsApi()

planet = api_client.get_planet(1)
print(f"Planet name: {planet.name}")
print(f"rotation_period: {planet.rotation_period}")

people = api_client.get_people(1)
print(f"People name: {people.name}")
print(f"height: {people.height}")

starship = api_client.get_starship(1)
print(f"Starships name: {starship.name}")
print(f"model: {starship.model}")



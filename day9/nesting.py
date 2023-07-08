# nesting dictionary in a dictionary:

travel_log = {
    "france": {"cities_visited": ["paris", "lily", "harry"], "total_visits": 12},
    "germany": {
        "cities_visited": ["berlin", "hamburg", "stuttgart"],
        "total_visits": 5,
    },
}

# nesting a dictionary in a list:

travel_log = [
    {
        "country": "france",
        "cities_visited": ["paris", "lily", "harry"],
        "total_visits": 12,
    },
    {
        "country": "germany",
        "cities_visited": ["berlin", "hamburg", "stuttgart"],
        "total_visits": 5,
    },
]

# challenge:

travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]
# 🚨 Do NOT change the code above


# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(visited, times, cities):
    new_country = {}  # creating an empty dictionary:
    new_country["country"] = visited
    new_country["visits"] = times
    new_country["cities"] = cities

    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

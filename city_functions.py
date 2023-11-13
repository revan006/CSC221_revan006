def format_city_country(city, country, population=None):
    full_location = f"{city.title()}, {country.title()}"
    if population:
        full_location += f" - population {population}"
    return full_location


def get_place_name(city, country, population=''):
    if population:
        full_name = city + ', ' + country
        name = full_name.title() + ' - population ' + str(population)
        return name
    else:
        full_name = city + ', ' + country
        return full_name.title()

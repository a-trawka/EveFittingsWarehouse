import itertools
import operator

import bs4
import requests


def flatten(it):
    # TODO; case when sequence contains both iterable and not iterable
    flattened = list(itertools.chain(*it))
    if any(isinstance(element, (list, tuple)) for element in flattened):
        return flatten(flattened)
    return flattened


SHIPS_URL = 'https://wiki.eveuniversity.org/Ships'

response = requests.get(SHIPS_URL)
soup = bs4.BeautifulSoup(response.text, 'lxml')

ships_matrix = soup.find('div', {'class': 'ships-matrix'})
ships_tables = ships_matrix \
    .table \
    .find_all('tr')[1] \
    .find_all('table')

std_ships = ships_tables[:13]
pirate_ships = ships_tables[13]
se_ships = ships_tables[14]

faction_ships = [
    ship_type.tr.find_all('th', {'class': 'racialcol centertext'})
    for ship_type in std_ships
]

a_elements = [
    [th.find_all('a') for th in faction_ths]
    for faction_ths in faction_ships
]

flat_elements = flatten(a_elements)

urls = list(
    map(operator.itemgetter('href'), flat_elements)
)
# print(all(isinstance(url, str) for url in urls))

# TODO: fill database

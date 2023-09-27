import requests
import pprint as pp


class RickAndMortyAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return response.json().get('results', [])
        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
        except requests.exceptions.ConnectionError as err:
            print(f"Error Connecting: {err}")
        except requests.exceptions.Timeout as err:
            print(f"Timeout Error: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")
        return []

    def get_characters(self, **filters):
        params = filters
        response = requests.get(self.api_url, params=params)
        return self._handle_response(response)


api_url = 'https://rickandmortyapi.com/api/character/'
api = RickAndMortyAPI(api_url)

# name: filter by the given name.
# status: filter by the given status (alive, dead or unknown).
# species: filter by the given species (Human, Alien ??? ).
# gender: filter by the given gender (female, male, genderless or unknown).

characters = api.get_characters(name='Rick', status='Dead')
pp.pprint(characters)

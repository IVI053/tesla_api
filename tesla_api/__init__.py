from datetime import datetime, timedelta
import requests

from .vehicle import Vehicle
from .tokenmanager import TokenManager

import tesla_api.constant as const


class TeslaApiClient:
    def __init__(self):
        self._tm = TokenManager()

    def _get_headers(self):
        return {'Authorization': 'Bearer {}'.format(self._tm.getAT())}

    def get(self, endpoint):
        response = requests.get('{}/{}'.format(const.API_URL, endpoint), headers=self._get_headers())
        response_json = response.json()

        if 'error' in response_json:
            raise ApiError(response_json['error'])

        return response_json['response']

    def post(self, endpoint, data = {}):
        response = requests.post('{}/{}'.format(const.API_URL, endpoint), headers=self._get_headers(), data=data)
        response_json = response.json()

        if 'error' in response_json:
            raise ApiError(response_json['error'])

        return response_json['response']

    def list_vehicles(self):
        return [Vehicle(self, vehicle) for vehicle in self.get('vehicles')]

class ApiError(Exception):
    def __init__(self, error):
        super().__init__('Tesla API call failed: {}'.format(error))

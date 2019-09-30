from datetime import datetime, timedelta
import requests
import json

import tesla_api.constant as const

class TokenManager:
    def __init__(self, pwmgr):
        self._pwmgr = pwmgr
        try:
            with open('token.json') as jsonfile:
                self._token = json.load(jsonfile)
        except FileNotFoundError:
            self._token = None


    def _get_new_token(self):
        request_data = {
            'grant_type': 'password',
            'client_id': const.CLIENT_ID,
            'client_secret': const.CLIENT_SECRET,
            'email': self._pwmgr.get_account(),
            'password': self._pwmgr.get_password()
        }

        response = requests.post(const.TOKEN_URL, data=request_data)
        response_json = response.json()

        if 'response' in response_json:
            raise AuthenticationError(response_json['response'])
        else:
            self._token = response_json
            self._save()
            print('Token received and saved')


    def _refresh_token(self, refresh_token):
        request_data = {
            'grant_type': 'refresh_token',
            'client_id': const.CLIENT_ID,
            'client_secret': const.CLIENT_SECRET,
            'refresh_token': refresh_token,
        }

        response = requests.post(const.TOKEN_URL, data=request_data)
        response_json = response.json()

        if 'response' in response_json:
            raise AuthenticationError(response_json['response'])

        self._token = response_json
        self._save()

    def _authenticate(self):
        if not self._token:
            self._get_new_token()

        expiry_time = timedelta(seconds=self._token['expires_in'])
        expiration_date = datetime.fromtimestamp(self._token['created_at']) + expiry_time

        if datetime.utcnow() >= expiration_date:
            self._refresh_token(self._token['refresh_token'])

    def _save(self):
        with open('token.json','w') as jsonfile:
            json.dump(self._token,jsonfile,indent=2)

    def getAT(self):
        self._authenticate()
        return self._token['access_token']


class AuthenticationError(Exception):
    def __init__(self, error):
        super().__init__('Authentication to the Tesla API failed: {}'.format(error))

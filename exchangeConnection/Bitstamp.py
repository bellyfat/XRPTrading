import hashlib
import hmac
import time

import requests
import yaml


class Bitstamp:
    """Bitstamp Connection class."""

    def __init__(self, config):
        self.config = config

    def load_config(self):
        with open(self.config, 'r') as envCfg:
            env_cfg = yaml.load(envCfg)
        return env_cfg

    def get_customer_id(self):
        env_cfg = self.load_config()
        return env_cfg['authentication']['customerId']

    def get_api_secret(self):
        env_cfg = self.load_config()
        return env_cfg['authentication']['apiSecret']

    def get_api_key(self):
        env_cfg = self.load_config()
        return env_cfg['authentication']['apiKey']

    def get_nonce(self):
        return str(int(time.time()) * 1000)

    def get_signature(self, customer_id, api_key, nounce):
        message = nounce + customer_id + api_key
        signature = hmac.new(
            self.get_api_secret().encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest().upper()
        return signature

    def request(self, endpoint, authenticate=False, **kwargs):
        """Generate a request to the API."""
        verb = 'POST' if authenticate else 'GET'
        return super(Bitstamp, self).request(verb, endpoint, authenticate=authenticate, **kwargs)

    def get_currency_pair_balance(self):
        currency_pair_balance_api_endpoint = 'https://www.bitstamp.net/api/v2/balance/'
        nonce = self.get_nonce()
        PARAMS = {'key': self.get_api_key(),
                  'signature': self.get_signature(self.get_customer_id(), self.get_api_key(), nonce),
                  'nonce': nonce
                  }
        req_return = requests.post(currency_pair_balance_api_endpoint, data=PARAMS)
        req_return_json = req_return.json()
        return req_return_json

import logging
import urllib
from abc import ABC, abstractmethod

import requests


class ApiClient(ABC):
    def __init__(self, api_name, url):
        self.url = url
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.api_name = api_name

    @abstractmethod
    def normalize_url(self, endpoint):
        pass

    @abstractmethod
    def get_headers(self):
        pass

    def prepare_kwargs(self, method, endpoint, files, params):
        if params is None:
            params = {}

        headers = self.get_headers()

        kwargs = {
            "url": self.normalize_url(endpoint),
            "headers": headers,
        }

        if method in ["POST"]:
            if files is not None and len(files) > 0:
                kwargs["files"] = files
            else:
                kwargs["json"] = params
        elif method in ["PUT"]:
            kwargs["params"] = params
        else:
            if params:
                kwargs["url"] = kwargs["url"] + "?" + urllib.parse.urlencode(params)
            else:
                kwargs["url"] = kwargs["url"]
        return kwargs

    def request(self, method, endpoint, params=None, response_status_pass=None, files=None):
        if response_status_pass is None:
            response_status_pass = []
        kwargs = self.prepare_kwargs(method=method, endpoint=endpoint, params=params, files=files)

        try:
            self.logger.info(f"""{self.api_name}. Request URL: {kwargs["url"]}""")
            self.logger.info(f"kwargs={kwargs}")

            response = requests.request(method, **kwargs)

            self.logger.info(f"{self.api_name}. Response status: {response.status_code}")

            if response.status_code not in response_status_pass:
                response.raise_for_status()

            return response

        except requests.exceptions.HTTPError as errh:
            self.logger.error(f"{self.api_name}. HTTP Error occurred: {errh}")
            if response.json():
                self.logger.error(f"Details: {response.json()}")
            raise

        except requests.exceptions.ConnectionError as errc:
            self.logger.error(f"{self.api_name}. Error Connecting: {errc}")
            raise

        except requests.exceptions.Timeout as errt:
            self.logger.error(f"{self.api_name}. Timeout Error: {errt}")
            raise

        except requests.exceptions.RequestException as err:
            self.logger.error(f"{self.api_name}. Something went wrong: {err}")
            raise


class BackApiClient(ApiClient):
    """
    Client for Wwslalom API
    """

    def __init__(self, url, token=None):
        super().__init__(
            url=url, api_name="WwslalomApiClient"
        )
        self.token = token

    def set_token(self, token):
        self.token = token
        print(f"self.token={self.token}")

    def normalize_url(self, endpoint):
        return self.url + endpoint

    def get_headers(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        self.logger.info(f"headers={headers}")
        return headers

    def post_register(self, email, password):
        self.logger.info(f"Request register user: {email}")
        params = dict(email=email, password=password)
        return self.request(method="POST", endpoint="/auth/register", params=params, response_status_pass=[400, 422])

    def post_login(self, email, password):
        self.logger.info(f"Request login user: {email}")
        files = dict(username=(None, email),
                     password=(None, password),
                     grant_type=(None, None),
                     client_id=(None, None),
                     client_secret=(None, None))
        res = self.request(method="POST", endpoint="/auth/jwt/login", files=files, response_status_pass=[400])
        if res.status_code == 200:
            self.set_token(res.json()["access_token"])
        return res

    def get_my_profile(self):
        self.logger.info("Request get my profile}")
        return self.request(method="GET", endpoint="/users/me", response_status_pass=[401])

    def post_verify_token(self, token):
        self.logger.info("Request post verify token}")
        params = {"token": token}
        return self.request(method="POST", endpoint="/auth/verify", params=params)

    def post_forgot_password(self, email):
        self.logger.info("Request post verify token}")
        params = dict(email=email)
        return self.request(method="POST", endpoint="/auth/forgot-password", params=params)

    # def get_pipeline_state_data(self, **kwargs):
    #     self.logger.info(f"Request get pipeline state data with params: {kwargs}")
    #     return self.request(method="GET", endpoint="pipeline_state", params=kwargs)
    #
    # def save_pipeline_state_data(self, **kwargs):
    #     self.logger.info(f"Request save pipeline state data with params: {kwargs}")
    #     return self.request(method="POST", endpoint="pipeline_state", params=kwargs)
    #
    # def set_pipeline_state_last_processed_date(self, **kwargs):
    #     self.logger.info(f"Request set pipeline state last processed date with params: {kwargs}")
    #     return self.request(
    #         method="PUT", endpoint="pipeline_state/last_date_processed", params=kwargs
    #     )
    #
    # def get_pipeline_state_last_date_processed(self):
    #     self.logger.info("Request get pipeline state last processed date")
    #     return self.request(method="GET", endpoint="pipeline_state/last_date_processed")
    #
    # def get_all_parameters(self):
    #     self.logger.info("Request get all parameters")
    #     return self.request(method="GET", endpoint="parameters")
    #
    # def get_parameter(self, param_name):
    #     self.logger.info(f"Request get parameter: {param_name}")
    #     return self.request(method="GET", endpoint=f"parameters/{param_name}")
    #
    # def set_parameter(self, param_name, param_value):
    #     self.logger.info(f"Request set parameter: {param_name}={param_value}")
    #     kwargs = dict(param_value=param_value)
    #     return self.request(
    #         method="PUT", endpoint=f"parameters/{param_name}", params=kwargs
    #     )

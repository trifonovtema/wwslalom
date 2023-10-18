from utils.backend_client import BackApiClient
import pickle
import os


class Auth2Manager():
    def __init__(self, auth2_url, client_storage_prefix, page):
        self.client_storage_prefix = client_storage_prefix
        self.page = page
        self.back_api_client = BackApiClient(url=auth2_url, token=self.load_token())

    def register_user_with_email_password(self, email, password):
        user = self.back_api_client.post_register(
            email=email,
            password=password).json()
        if "id" in user:
            return self.login_user(email, password)
        return user  # TODO

    def login_user(self, email, password):
        res = self.back_api_client.post_login(email, password)
        match res.status_code:
            case 400:
                return {"error": f"""Error :{res.json()["detail"]}"""}
            case 200:
                token = res.json()["access_token"]
                self.store_session(token)
                return {"access_token": token}
            case _:
                return {"error": f"""Error :{res.json()["detail"]}"""}

    def load_token(self):
        if self.page.client_storage.contains_key(self.client_storage_prefix + "token") is True:
            return self.page.client_storage.get(self.client_storage_prefix + "token")
        else:
            return None

    def authenticate_token(self):
        if self.back_api_client.token is not None:
            res = self.back_api_client.get_my_profile()
            if res.status_code == 200:
                return res.json()["id"]
        token = self.load_token()
        if token is not None:
            if self.back_api_client.token != token:
                self.back_api_client.set_token(token)
                res = self.back_api_client.get_my_profile()
                if res.status_code == 200:
                    return res.json()["id"]
                else:
                    return {"error": f"""Error: {res.json()["detail"]}"""}
        else:
            return {"error": "Not authenticated"}

    def is_authenticated(self):
        res = self.authenticate_token()
        if "error" in res:
            return False
        else:
            return True

    def store_session(self, token):
        self.page.client_storage.set(self.client_storage_prefix + "token", token)

    def get_name(self):
        token = self.load_token()
        self.back_api_client.set_token(token)
        res = self.back_api_client.get_my_profile()
        return res.json()["email"]

    def forgot_password(self, email):
        res = self.back_api_client.post_forgot_password(email)
        print(res.json())

    def logout(self):
        self.back_api_client.set_token(None)
        self.page.client_storage.remove(self.client_storage_prefix + "token")


def reset_password(email):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! reset_password")
    pass
    # try:
    #     auth.send_password_reset_email(email)
    #     return not None
    # except:
    #     return None


#
#


def revoke_token(token):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! revoke_token")
    # result = firebase_auth.revoke_refresh_tokens(authenticate_token(token))
    # if os.path.exists('token.pickle'):
    #     os.remove('token.pickle')

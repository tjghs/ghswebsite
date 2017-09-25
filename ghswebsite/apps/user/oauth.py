from social_core.backends.oauth import BaseOAuth2


class IonOAuth(BaseOAuth2):
    """Ion OAuth authentication backend"""
    name = 'ion'
    AUTHORIZATION_URL = 'https://ion.tjhsst.edu/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://ion.tjhsst.edu/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    SCOPE_SEPARATOR = ','
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token', True),
        ('expires_in', 'expires')
    ]

    def get_scope(self):
        return ["read"]

    def get_user_details(self, response):
        profile = self.get_json('https://ion.tjhsst.edu/api/profile',
                                params={'access_token': response['access_token']})

        # fields used to populate/update User model
        return {
            'username': profile['ion_username'],
            'full_name': profile['full_name'],
            'id': profile['id'],
            'email': profile['tj_email'],
            'staff': False
        }

    def get_user_id(self, details, response):
        print("call get_user_id")
        print(details['id'])
        return details['id']

from .client import Client


class ContentField(Client):
    """ContentField"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'content/'

    def get(self, keys=None, params=None):
        if not params:
            params = {}
        params['keys'] = ','.join(keys)
        return self.api_get(params=params)

    def get(self, slug, fields=None, params=None):
        if not params:
            params = {}
        if fields:
            for field in fields:
                key = "fields.{}".format(field)
                params[key] = fields[field]

        return self.api_get(slug, params=params)
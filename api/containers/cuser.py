from api.containers.base import Container


class CUser(Container):
    keys = [
        'uuid',
        'name',
        'email'
    ]

    def __init__(self, user):
        self['uuid'] = user.uuid
        self['name'] = user.name
        self['email'] = user.email






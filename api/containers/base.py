
class Container(dict):
    keys = None

    def __init__(self, values, keys=None):
        if keys:
            self.keys = keys
        if self.keys is None:
            raise Exception("invalid keys")
        for x in self.keys:
            self[x] = values[x]

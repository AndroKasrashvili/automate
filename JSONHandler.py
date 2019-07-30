from json import JSONEncoder, JSONDecoder


class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, list):
            return [i.__dict__ for i in o]
        return o.__dict__


class MyJSONDecoder(JSONDecoder):
    def default(self, o):
        return o.__dict__


from json import JSONEncoder


class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, list):
            return [i.__dict__ for i in o]
        return o.__dict__



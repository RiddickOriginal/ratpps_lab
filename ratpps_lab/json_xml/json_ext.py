import json
class JsonEncodeDecode:
    def json_encode(self):
        self.__dict__ = JsonEncodeDecode.map_dict_json(self.__dict__, False)
        return json.dumps(self.__dict__)

    @staticmethod
    def json_decode(attr_str):
        if not (type(attr_str) is str): raise TypeError("attr_str must be valid JSON string")
        attr = json.loads(attr_str)
        return JsonEncodeDecode.map_dict_json(attr, True)

    @staticmethod
    def map_dict_json(dictionary: dict, decode: bool):
        for key, val in dictionary.items():
            try:
                if decode:
                    dictionary[key] = val.json_decode()
                else:
                    dictionary[key] = val.json_encode()
            except:
                pass
        return dictionary

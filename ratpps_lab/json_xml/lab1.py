from json_ext import JsonEncodeDecode
from xml_ext import XmlEncodeDecode

class Screen(JsonEncodeDecode, XmlEncodeDecode):
    
    class Matrix(JsonEncodeDecode, XmlEncodeDecode):
        def __init__(self, m_type: str, ping: int):
            type_check = type(m_type) != str
            ping_check = type(ping) not in (str, int)
            if any((type_check, ping_check)):
                raise TypeError("check constructor parametrs type")
            
            self.m_type = m_type
            self.ping = ping
        def __str__(self):
            return "{0} matrix with ping {1} ms".format(self.m_type, self.ping)
        
        @staticmethod
        def instance_from_json(attr_str):
            if type(attr_str) != str: raise TypeError("attr_str must be valid JSON string")
            attr = JsonEncodeDecode.json_decode(attr_str)
            return Screen.Matrix(attr['m_type'], attr['ping'])
        
        @staticmethod
        def instance_from_dict(attr_dict: dict):
            if type(attr_dict) != dict: raise TypeError("attr_dict must be dict of attributes")
            return Screen.Matrix(attr_dict['m_type'], attr_dict['ping'])
    
    def __init__(self, brand: str, model: str, matrix: Matrix, width_resolution: int = 1920, height_resolution: int = 1080, used: bool = False):
        brand_check = type(brand) != str
        model_check = type(model) != str
        matrix_check = type(matrix) != self.Matrix
        width_check = type(width_resolution) not in (str, int)
        height_check = type(height_resolution) not in (str, int)
        used_check = type(used) != bool
        if any((brand_check, model_check, matrix_check, width_check, height_check, used_check)):
            raise TypeError("check constructor parametrs type")
        
        self.resolution = int(width_resolution), int(height_resolution)
        self.brand = brand
        self.model = model
        self.used = used
        self.matrix = matrix

    def __str__(self):
        return "{0} {1}: {2}x{3} ({4}). {5}".format(self.brand, self.model,
                                               self.resolution[0], self.resolution[1],
                                                    'used' if self.used else 'new', self.matrix)

    @staticmethod
    def instance_from_dict(attr_dict: dict):
        lower_dict = {}
        for key, val in attr_dict.items():
            lower_dict.setdefault(key.lower(), val)
        if lower_dict['used'] == 'False': lower_dict['used'] = False
        if lower_dict['used'] == 'True': lower_dict['used'] = True
        return Screen(lower_dict['brand'], lower_dict['model'], lower_dict['matrix'],
                      lower_dict['resolution'][0], lower_dict['resolution'][1], lower_dict['used'])

    @staticmethod
    def json_decode(attr_str: str):
        attr = JsonEncodeDecode.json_decode(attr_str)
        attr['matrix'] = Screen.Matrix.instance_from_json(attr['matrix'])
        return attr
    
    @staticmethod
    def instance_from_json(attr_json):
        attr = Screen.json_decode(attr_json)
        return Screen(attr['brand'], attr['model'], attr['matrix'],
                      attr['resolution'][0], attr['resolution'][1], attr['used'])

    @staticmethod
    def instance_from_xml(elem_tree):
        attr = Screen.xml_decoder(elem_tree)
        attr['Matrix'] = Screen.Matrix.instance_from_dict(attr['Matrix'])
        attr['resolution'] = attr['resolution'].replace('(','').replace(')', '').replace(' ', '').split(',')
        attr['resolution'] = list(map(int, attr['resolution']))
        return Screen.instance_from_dict(attr)


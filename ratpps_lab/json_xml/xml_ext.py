import xml.etree.ElementTree as ET

class XmlEncodeDecode:
    def xml_encode(self):
        root = ET.Element(self.__class__.__name__)
        for key, val in self.__dict__.items():
            try:
                val = val.xml_encode()
                root.append(val)
            except:
                elem = ET.SubElement(root, key)
                elem.text = str(val)
        return root

    @staticmethod
    def xml_decoder(xml_element):
        if not (type(xml_element) is ET.Element):
            raise TypeError("xml_element_list must be ElementTree.Element")
        
        attrs = dict()
        for elem in list(xml_element):
            if elem.text is None:
                decoded_list = XmlEncodeDecode.xml_decoder(elem)
                attrs.setdefault(elem.tag, decoded_list)
            else:
                attrs.setdefault(elem.tag, elem.text)
        return attrs
    
    @staticmethod
    def xml_write(xml_element: ET.Element, file_name: str):
        ET.ElementTree(xml_element).write(file_name)

    @staticmethod
    def xml_read(file_name: str):
        return ET.ElementTree().parse(file_name)

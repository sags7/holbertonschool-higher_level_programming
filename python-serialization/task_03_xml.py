#!/usr/bin/python3
"""
this exercise explores serialization using 
XML as an alternative to JSON
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """saves a python dictionary as XML"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """deserializes an XML file and returns it as a python dict"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for elem in root:
        dictionary[elem.tag] = try_convert_type(elem.text)

    return dictionary


def try_convert_type(element):
    """Tries to convert a string to int, float, or boolean; falls back to string"""
    try:
        return int(element)
    except ValueError:
        pass

    try:
        return float(element)
    except ValueError:
        pass

    if element.lower() == "true":
        return True
    elif element.lower() == "false":
        return False

    return element

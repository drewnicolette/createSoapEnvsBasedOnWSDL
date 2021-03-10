import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader

def load_template():
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('template.xml')
    return template

def getNamespace(tree,filename):
    tree = ET.parse(filename)
    #tree = ET.parse('xml_sample.wsdl')
    #a=tree.findall('*/element')
    root = tree.getroot()
    target_namespace  = root.attrib["targetNamespace"]
    return target_namespace

def getOperations(tree):
    lst = []
    for elem in tree.iter():
    #    if (elem.tag.endswith("element")) and ("name" in elem.attrib) and (len(elem.attrib) == 1):
        if (elem.tag.endswith("element")) and ("name" in elem.attrib):
            elem_values = list(elem.attrib.values())[0]
            if "Response" in elem_values:
                lst.append(elem_values.split("Response")[0])
    return lst

if __name__ == "__main__":
    tree = ET.parse('xml_sample.wsdl')
    root = tree.getroot()
    loaded_template = load_template()
    target_namespace = getNamespace(tree,"xml_sample.wsdl")
    lst_of_operations = getOperations(tree)
    for operation in lst_of_operations:
        output = loaded_template.render(t_namespace=target_namespace, operation=operation)
        print("\n")
        print(output)
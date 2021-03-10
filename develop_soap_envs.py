from zeep.plugins import HistoryPlugin
from zeep import Client, Settings
from lxml import etree
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
import operator
import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

#wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
#wsdl_url = "http://www.dneonline.com/calculator.asmx?wsdl"
full_path_to_wsdl = "/Users/drewnicolette/xml/xml_sample.wsdl"
wsdl_url = f"file://{full_path_to_wsdl}"

def load_template():
    try:
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template('template.xml')
        return template
    except:
        print("OS error: {0}".format(err))

def getNamespace(tree,filename):
    try:
        root = tree.getroot()
        target_namespace  = root.attrib["targetNamespace"]
        return target_namespace
    except:
        print("OS error: {0}".format(err))

def getOperations(tree):
    try:
        lst = []
        for elem in tree.iter():
            if (elem.tag.endswith("element")) and ("name" in elem.attrib):
                elem_values = list(elem.attrib.values())[0]
                if "Response" in elem_values:
                    lst.append(elem_values.split("Response")[0])
        return lst
    except:
        print("OS error: {0}".format(err))

# -- this parses the WSDL to get the methods along with their inputs and outputs
def get_methods_and_data_types(wsdl_url):
    try:
        client = Client(wsdl=wsdl_url)
        for service in client.wsdl.services.values():
            #print("service:", service.name)
            for port in service.ports.values():
                operations = sorted(
                    port.binding._operations.values(),
                    key=operator.attrgetter('name'))
            dict1 = {}
            for operation in operations:
                #print("method :", operation.name)
                x = operation.input.signature()
                y = x.split(",")
                data_types = []
                for i in y:
                    j = i.split(":")[0]
                    data_types.append(j.strip())
                dict1[operation.name] = data_types
                #print("  input :", operation.input.signature())
                #print("  output:", operation.output.signature())
        return dict1
    except:
        print("OS error: {0}".format(err))

def getEverythingAboutWSDL(wsdl_url):
    try:
        client = Client(wsdl=wsdl_url)
        for service in client.wsdl.services.values():
            print("\n")
            print("service:", service.name)
            for port in service.ports.values():
                operations = sorted(
                    port.binding._operations.values(),
                    key=operator.attrgetter('name'))
            for operation in operations:
                print("method :", operation.name)
                print("  input :", operation.input.signature())
                print("  output:", operation.output.signature())
    except:
        print("OS error: {0}".format(err))

if __name__ == '__main__':
    '''
    #This is my calling my custom code to generate SOAP Requests and Output them to another file called output.xml
    tree = ET.parse(full_path_to_wsdl)
    loaded_template = load_template()
    target_namespace = getNamespace(tree,full_path_to_wsdl)
    methods_and_dt = get_methods_and_data_types(wsdl_url)
    with open("output.xml","w") as f:
        for key,values in methods_and_dt.items():
            output = loaded_template.render(t_namespace=target_namespace, operation=key, dtypes=values)
            f.write(output)
            f.write("\n")
            f.write("\n")
    '''
    #This is getting the soap message delivered to endpoint
    settings = Settings(strict=False, xml_huge_tree=True)
    #wsdl_url = "https://cs.au.dk/~amoeller/WWW/webservices/wsdlexample.html"
    wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
    client = Client(wsdl_url, settings=settings)
    getEverythingAboutWSDL(wsdl_url)
    node = client.create_message(client.service,"ListOfContinentsByCode")
    print(etree.tostring(node, pretty_print=True).decode())
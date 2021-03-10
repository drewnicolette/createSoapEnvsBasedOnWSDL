from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
#res = es.index(index="test-index", id=1, body=doc)
#print(res['result'])

#Returns all the documents for specific index along with certain paths
print(es.search(index='test-index', filter_path=['hits.hits._source', 'hits.hits._type']))

#Creates documents and puts them into specific index
#test = es.create(index='test-index', id=2, body={"drew":"test"})
from elasticsearch import Elasticsearch
#pip install elasticsearch-dsl
client = Elasticsearch("<ELK_HOST>", http_auth=("<USERNAME>","<PASSWORD>"))

response = client.search(
    index="index-2022.02.23",
    query= {
        "bool": {
            "must": [
                {
                    "query_string": {
                        "query": "_id: \"u8inKH8B3SM-0hX2jMxK\""
                    }
                },
                {
                    "range": {
                        "@timestamp": {
                            "gte": "now-15m"
                        }
                    }
                }
            ]
        }
    }
)

for hit in response['hits']['hits']:
    print("Beat Hostname: ",hit['_source']['beat']['hostname'],"\nSource Hostname: ",hit['_source']['host']['os']['name'])

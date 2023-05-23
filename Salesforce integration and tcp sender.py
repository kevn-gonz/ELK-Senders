import requests
import socket
import json

#Auth Parameters
params = {
    "grant_type": "password",
    "client_id": "<CLIENT_ID>", # aka Consumer Key
    "client_secret": "<CLIENT_SECRET>", # aka Consumer Secret
    "username": "<USERNAME>",
    "password": "<PASSWORD>"
}
#Send request to get access token
r = requests.post("https://<HOST>.my.salesforce.com/services/oauth2/token", params=params)
access_token = r.json().get("access_token")
instance_url = r.json().get("instance_url")
#Using the access token to auth and get data
def sf_api_call(action, parameters = {}, method = 'get', data = {}):
    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer %s' % access_token
    }
    if method == 'get':
        r = requests.request(method, instance_url+action, headers=headers, params=parameters, timeout=30)
    else:
        raise ValueError('Method should be GET')
    print('Debug: API %s call: %s' % (method, r.url) )
    if r.status_code > 300:
        raise Exception('API error when calling %s : %s' % (r.url, r.content))
    else:
        return r.json()

#Logstash connection
TCP_IP = '<LOGSTASH_SERVER_IP_HOSTNAME>'
TCP_PORT = 5069
data = json.dumps(sf_api_call('/services/data/v55.0/query/', {
    'q': 'select Action,CreatedById,CreatedDate,Display,Id,ResponsibleNamespacePrefix,Section,CreatedBy.name FROM SetupAuditTrail WHERE CreatedDate = LAST_N_WEEKS:1'
}))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((TCP_IP, TCP_PORT))
    sock.sendall(bytes(data,encoding="utf-8"))
except Exception as e:
    print("Error:", e)
    exit(2)
finally:
    sock.close()

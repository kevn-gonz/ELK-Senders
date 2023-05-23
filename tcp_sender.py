import socket

#TCP_IP = '172.18.18.118'
#TCP_PORT = 6699
TCP_IP = '<LOGSTASH_HOST>'
TCP_PORT = 5069
BUFFER_SIZE = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Creating test json object
jsonData = '{\"message\":\"Kevin working on this\",\"field1\":\"123\",\"field2\":123,\"tags\":[\"foo_123\",\"bar\"]}'

s.connect((TCP_IP, TCP_PORT))
byte_json = jsonData.encode('utf-8')
s.send(byte_json)
s.close()


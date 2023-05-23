import socket

TCP_IP = '<LOGSTASH_HOST>'
TCP_PORT = 5069
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Creating test json object
jsonData = '{\"logger\":{\"process\":{\"pid\":340,\"thread\":{\"id\":9984}},\"event_id\":\"4627\",\"api\":\"kevin-test-container\",\"provider_name\":\"Microsoft-Windows-Security-Auditing\",\"task\":\"GroupMembership\",\"opcode\":\"Info\",\"event_data\":{\"SubjectDomainName\":\"KK\",\"SubjectUserSid\":\"S-1-5-18\",\"TargetDomainName\":\"NTAUTHORITY\",\"TargetLogoKKd\":\"0x3e7\",\"GroupMembership\":\"%{S-1-5-32-544}%{S-1-1-0}%{S-1-5-11}%{S-1-16-16384}\",\"TargetUserName\":\"SYSTEM\",\"EventIdx\":\"1\",\"EventCountTotal\":\"1\",\"SubjectLogoKKd\":\"0x3e7\",\"LogonType\":\"5\",\"SubjectUserName\":\"kevin-LENOVO$\",\"TargetUserSid\":\"S-1-5-18\"},\"keywords\":[\"AuditSuccess\"],\"computer_name\":\"kevin-lenovo\",\"provider_guid\":\"{54849625-5478-4994-a5ba-3e3b0328c3}\",\"channel\":\"Security\",\"record_id\":115039,\"activity_id\":\"{cb261f99-b52c-0004-ef1f-26cb2cb5d701}\"},\"event\":{\"kind\":\"event\",\"provider\":\"Microsoft-Windows-Security-Auditing\",\"outcome\":\"success\",\"action\":\"GroupMembership\",\"created\":\"2021-09-30T19:24:57.121Z\",\"code\":\"4627\"},\"log\":{\"level\":\"information\"},\"message\":\"Group membership information.Subject:Security ID:S-1-5-18Account Name:kevin-LENOVO$Account Domain:KKLogon ID:0x3E7Logon Type:5New Logon:Security ID:S-1-5-18Account Name:SYSTEMAccount Domain:NT AUTHORITYLogon ID:0x3E7Event in sequence:1 of 1Group Membership:%{S-1-5-32-544}%{S-1-1-0}%{S-1-5-11}%{S-1-16-16384}The subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.The logon type field indicates the kind of logon that occurred. The most common types are 2 (interactive) and 3 (network).The New Logon fields indicate the account for whom the new logon was created, i.e. the account that was logged on.This event is generated when the Audit Group Membership subcategory is configured.  The Logon ID field can be used to correlate this event with the corresponding user logon event as well as to any other security audit events generated during this logon session.\",\"host\":{\"name\":\"kevin-lenovo\"},\"ecs\":{\"version\":\"1.10.0\"}}'

s.connect((TCP_IP, TCP_PORT))
byte_json = jsonData.encode('utf-8')
s.send(byte_json)
s.close()
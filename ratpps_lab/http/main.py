from client import TolltechClient

client = TolltechClient()
client.create_all([{'Key': 'k1', 'Value': 'v1'}, {'Key': 'k2', 'Value': 'v2'}, {'Key': 'k3', 'Value': 'v3'}])
print(client.select(['k1', 'k2', 'k3']))

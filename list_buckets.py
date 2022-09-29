from http import client
import boto3

#client = boto3.client("s3")
#response = client.list_buckets()
#print(response)
#print(response['Buckets'][0]['Name'])

client = boto3.client('ec2')
response_vpc = client.describe_vpcs()
response_subnets = client.describe_subnets()
for vpc in response_vpc['Vpcs']:
    print(vpc)
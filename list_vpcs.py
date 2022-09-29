# - Write a boto3 script that prints out all VPCs and Subnets
# in your lab account.
# - Then for each resource found (VPC and subnets), 
# attach a new AWS tag "Project: Talent-Academy" 
# where tag key is "Project" and tag value is "Talent-Academy"

import boto3
client =boto3.client('ec2',region_name='eu-central-1')
vpcs = client.describe_vpcs()
print(vpcs)
subnets = client.describe_subnets()
print(subnets)

for vpc in vpcs['Vpcs']:
    vpc_id = vpc.get('VpcId',[])
    client.create_tags(
        Resources = [vpc_id],
        Tags = [
            {
                'Key':'Project',
                'Value':'Talent-Academy'
            },
        ]
    )

for subnet in subnets['Subnets']:
    subnet_id = vpc.get('SubnetId',[])
    client.create_tags(
        Resources = [subnet_id],
        Tags = [
            {
                'Key':'Project',
                'Value':'Talent-Academy'
            },
        ]
    )

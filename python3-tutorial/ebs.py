import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')
volumes = ec2.volumes.all() # If you want to list out all volumes
#volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['in-use']}]) # if you want to list out only attached volumes
i = 0
for v in volumes:
	i = i + 1
	print (v.id)

print ("total volume count = ", i)
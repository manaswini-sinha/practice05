import boto3
client = boto3.client('ec2')
response = client.run_instances(
ImageId='ami-0e0e417dfa2028266',
        InstanceType='t2.micro',
        KeyName='pro',
        MaxCount=1,
        MinCount=1

)

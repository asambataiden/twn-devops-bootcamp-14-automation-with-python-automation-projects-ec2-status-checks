import boto3

boto3_session = boto3.Session(
    profile_name="asambataiden-dev"
)

ec2_client_frankfurt = boto3_session.client('ec2', region_name="eu-central-1")
ec2_resource_frankfurt = boto3_session.resource('ec2', region_name="eu-central-1")

ec2_client_stockholm = boto3_session.client('ec2', region_name="eu-north-1")
ec2_resource_stockholm = boto3_session.resource('ec2', region_name="eu-north-1")

instance_ids_frankfurt = []
instance_ids_stockholm = []

reservations_frankfurt = ec2_client_frankfurt.describe_instances()['Reservations']
for res in reservations_frankfurt:
    instances = res['Instances']
    for ins in instances:
        instance_ids_frankfurt.append(ins['InstanceId'])


response = ec2_resource_frankfurt.create_tags(
    Resources=instance_ids_frankfurt,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

reservations_stockholm = ec2_client_stockholm.describe_instances()['Reservations']
for res in reservations_stockholm:
    instances = res['Instances']
    for ins in instances:
        instance_ids_stockholm.append(ins['InstanceId'])


response = ec2_resource_stockholm.create_tags(
    Resources=instance_ids_stockholm,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
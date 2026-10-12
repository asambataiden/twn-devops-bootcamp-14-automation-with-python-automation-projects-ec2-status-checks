import time

import boto3
import schedule

boto3_session = boto3.Session(
    profile_name="asambataiden-dev"
)

ec2_client = boto3_session.client("ec2")
ec2_resource = boto3_session.resource("ec2")

print(ec2_client.describe_instances())
def check_instance_status() -> None:
    statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )

    for status in statuses["InstanceStatuses"]:
        instance_status = status["InstanceStatus"]["Status"]
        system_status = status["SystemStatus"]["Status"]
        state = status["InstanceState"]["Name"]
        instance_id = status["InstanceId"]

        print(
            f"Instance {instance_id} is {state} "
            f"with instance status {instance_status} "
            f"and system status {system_status}"
        )

    print("#############################\n")

schedule.every(5).minutes.do(check_instance_status)

while True:
    schedule.run_pending()



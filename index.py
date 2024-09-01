import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Initialize a session using Boto3
ec2 = boto3.client('ec2', region_name='your-region')

try:
    # Allocate a new Elastic IP
    allocation = ec2.allocate_address(Domain='vpc')
    print(f"Allocated Elastic IP: {allocation['PublicIp']} with Allocation ID: {allocation['AllocationId']}")

    # Associate the Elastic IP with an EC2 instance
    instance_id = 'your-instance-id'  # Replace with your instance ID
    association = ec2.associate_address(
        InstanceId=instance_id,
        AllocationId=allocation['AllocationId']
    )
    print(f"Elastic IP {allocation['PublicIp']} associated with Instance ID: {instance_id}")

    # Optionally, disassociate and release the Elastic IP
    # Disassociate the Elastic IP
    ec2.disassociate_address(AssociationId=association['AssociationId'])
    print(f"Elastic IP {allocation['PublicIp']} disassociated from Instance ID: {instance_id}")

    # Release the Elastic IP
    ec2.release_address(AllocationId=allocation['AllocationId'])
    print(f"Released Elastic IP: {allocation['PublicIp']}")

except NoCredentialsError:
    print("Credentials not available.")
except ClientError as e:
    print(f"Unexpected error: {e}")

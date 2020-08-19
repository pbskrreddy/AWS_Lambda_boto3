# import boto3
# ec2 = boto3.resource('ec2')
# for instance in ec2.instances.all():
#     print('instance id is {} and instance type is {}'.format(instance.instance_id,instance.instance_type))
#

import boto3
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    filters = [
        {
            'Name' : 'env',
            'Values' : 'Prod'
        },
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
    # filter the instances
    # ec2 = boto3.client('ec2', region_name=region)
    instances = ec2.instances.filter(Filters=filters)

    # locate all running instances
    RunningInstances = [instance.id for instance in instances]

    # print the instances for logging purposes
    print(RunningInstances)

    # make sure there are actually instances to shut down.

    shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
    return success

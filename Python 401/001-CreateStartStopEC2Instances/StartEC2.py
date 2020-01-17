import boto3


def lambda_handler(event, context):

    # First get Boto Client reference 

    the_client = boto3.client('ec2')

    # Then Get list of regions
    lstRegions = [region['RegionName'] for region in the_client.describe_regions()['Regions']]

    # Loop through the regions
    for region in lstRegions:
        ec2Resource = boto3.resource('ec2', region_name=region)

        print("Region:", region)

    # filter the stopped instances only
    stoppedinstances = ec2Resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

    # start the stopped instances
    for instance in stoppedinstances:
        instance.start()
        print('Started the instance: ', instance.id)
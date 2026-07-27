import boto3


def get_aws_client(
    service_name: str,
    access_key: str,
    secret_key: str,
    region: str,
):
    return boto3.client(
        service_name,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region,
    )
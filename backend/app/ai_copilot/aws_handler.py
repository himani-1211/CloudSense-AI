from app.ai_copilot.intent import Intent


def handle_aws_intent(
    intent: Intent,
    resources: dict,
) -> str:
    """
    Handles AWS-related AI Copilot questions.

    Parameters
    ----------
    intent : Intent
        Detected user intent.

    resources : dict
        AWS resources collected from discovery.

    Returns
    -------
    str
        AI response.
    """

    ec2 = resources["ec2"]
    s3 = resources["s3"]
    rds = resources["rds"]
    lambda_functions = resources["lambda"]
    vpcs = resources["vpcs"]
    ebs = resources["ebs"]

    # ==========================================================
    # EC2
    # ==========================================================

    if intent == Intent.EC2_COUNT:
        return f"You currently have {len(ec2)} EC2 instance(s)."

    if intent == Intent.EC2_LIST:

        if not ec2:
            return "You don't have any EC2 instances."

        response = "Your EC2 instances:\n\n"

        for index, instance in enumerate(ec2, start=1):

            name = instance.get("name", "Unnamed Instance")
            state = instance.get("state", "Unknown")
            instance_type = instance.get("instance_type", "Unknown")

            response += (
                f"{index}. {name}\n"
                f"   State : {state}\n"
                f"   Type  : {instance_type}\n\n"
            )

        return response

    # ==========================================================
    # S3
    # ==========================================================

    if intent == Intent.S3_COUNT:
        return f"You currently have {len(s3)} S3 bucket(s)."

    if intent == Intent.S3_LIST:

        if not s3:
            return "No S3 buckets found."

        response = "Your S3 Buckets:\n\n"

        for index, bucket in enumerate(s3, start=1):

            response += f"{index}. {bucket.get('name','Unnamed Bucket')}\n"

        return response

    # ==========================================================
    # Lambda
    # ==========================================================

    if intent == Intent.LAMBDA_COUNT:
        return f"You currently have {len(lambda_functions)} Lambda function(s)."

    if intent == Intent.LAMBDA_LIST:

        if not lambda_functions:
            return "No Lambda functions found."

        response = "Your Lambda Functions:\n\n"

        for index, function in enumerate(lambda_functions, start=1):

            response += (
                f"{index}. "
                f"{function.get('name','Unnamed Function')}\n"
            )

        return response

    # ==========================================================
    # RDS
    # ==========================================================

    if intent == Intent.RDS_COUNT:
        return f"You currently have {len(rds)} RDS database(s)."

    if intent == Intent.RDS_LIST:

        if not rds:
            return "No RDS databases found."

        response = "Your RDS Databases:\n\n"

        for index, database in enumerate(rds, start=1):

            response += (
                f"{index}. "
                f"{database.get('name','Unnamed Database')}\n"
            )

        return response

    # ==========================================================
    # VPC
    # ==========================================================

    if intent == Intent.VPC_COUNT:
        return f"You currently have {len(vpcs)} VPC(s)."

    if intent == Intent.VPC_LIST:

        if not vpcs:
            return "No VPCs found."

        response = "Your VPCs:\n\n"

        for index, vpc in enumerate(vpcs, start=1):

            response += (
                f"{index}. "
                f"{vpc.get('name','Unnamed VPC')}\n"
            )

        return response

    # ==========================================================
    # EBS
    # ==========================================================

    if intent == Intent.EBS_COUNT:
        return f"You currently have {len(ebs)} EBS volume(s)."

    if intent == Intent.EBS_LIST:

        if not ebs:
            return "No EBS volumes found."

        response = "Your EBS Volumes:\n\n"

        for index, volume in enumerate(ebs, start=1):

            response += (
                f"{index}. "
                f"{volume.get('name','Unnamed Volume')}\n"
            )

        return response

    # ==========================================================
    # Infrastructure Summary
    # ==========================================================

    if intent == Intent.SUMMARY:

        return f"""
AWS Infrastructure Summary

EC2 Instances      : {len(ec2)}
S3 Buckets         : {len(s3)}
Lambda Functions   : {len(lambda_functions)}
RDS Databases      : {len(rds)}
VPCs               : {len(vpcs)}
EBS Volumes        : {len(ebs)}
"""

    # ==========================================================

    return None
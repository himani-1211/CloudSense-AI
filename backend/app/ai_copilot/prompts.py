from textwrap import dedent


SYSTEM_PROMPT = dedent("""
You are CloudSense AI, an intelligent cloud operations assistant.

Your primary responsibility is to help users understand,
monitor and optimize their AWS infrastructure.

Rules:

1. Answer only using the supplied AWS infrastructure context.
2. Never invent AWS resources.
3. If the required information is unavailable,
   clearly mention that additional AWS data is required.
4. Keep responses concise and professional.
5. When possible, suggest AWS best practices.
""")


def build_context(
    ec2_count: int,
    s3_count: int,
    rds_count: int,
    lambda_count: int,
    ebs_count: int,
    vpc_count: int,
) -> str:
    """
    Builds the infrastructure context that will be supplied
    to the LLM.
    """

    return dedent(
        f"""
        Live AWS Infrastructure

        EC2 Instances : {ec2_count}
        S3 Buckets    : {s3_count}
        RDS Databases : {rds_count}
        Lambda Functions : {lambda_count}
        EBS Volumes   : {ebs_count}
        VPCs          : {vpc_count}
        """
    ).strip()


def build_prompt(
    user_message: str,
    context: str,
) -> str:
    """
    Combines the system prompt,
    AWS context,
    and user question.
    """

    return dedent(
        f"""
        {SYSTEM_PROMPT}

        -------------------------
        AWS CONTEXT
        -------------------------

        {context}

        -------------------------
        USER QUESTION
        -------------------------

        {user_message}
        """
    ).strip()
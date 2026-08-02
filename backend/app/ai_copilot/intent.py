from enum import Enum


class Intent(str, Enum):
    EC2_COUNT = "ec2_count"
    EC2_LIST = "ec2_list"

    S3_COUNT = "s3_count"
    S3_LIST = "s3_list"

    RDS_COUNT = "rds_count"
    RDS_LIST = "rds_list"

    LAMBDA_COUNT = "lambda_count"
    LAMBDA_LIST = "lambda_list"

    VPC_COUNT = "vpc_count"
    VPC_LIST = "vpc_list"

    EBS_COUNT = "ebs_count"
    EBS_LIST = "ebs_list"

    SUMMARY = "summary"

    UNKNOWN = "unknown"


def detect_intent(question: str) -> Intent:
    """
    Detect the user's intent from their question.
    """

    question = question.lower()

    # ---------------- EC2 ----------------

    if "ec2" in question or "instance" in question:
        if any(word in question for word in ["how many", "count", "number"]):
            return Intent.EC2_COUNT
        return Intent.EC2_LIST

    # ---------------- S3 ----------------

    if "s3" in question or "bucket" in question:
        if any(word in question for word in ["how many", "count", "number"]):
            return Intent.S3_COUNT
        return Intent.S3_LIST

    # ---------------- RDS ----------------

    if "rds" in question or "database" in question:
        if any(word in question for word in ["how many", "count", "number"]):
            return Intent.RDS_COUNT
        return Intent.RDS_LIST

    # ---------------- Lambda ----------------

    if "lambda" in question:
        if any(word in question for word in ["how many", "count", "number"]):
            return Intent.LAMBDA_COUNT
        return Intent.LAMBDA_LIST

    # ---------------- VPC ----------------

    if "vpc" in question:
        if any(word in question for word in ["how many", "count", "number"]):
            return Intent.VPC_COUNT
        return Intent.VPC_LIST

    # ---------------- EBS ----------------

    if "ebs" in question or "volume" in question:
        if any(word in question for word in ["how many", "count", "number"]):
            return Intent.EBS_COUNT
        return Intent.EBS_LIST

    # ---------------- Summary ----------------

    if any(
        word in question
        for word in [
            "summary",
            "overview",
            "infrastructure",
            "resources",
            "cloud summary",
        ]
    ):
        return Intent.SUMMARY

    return Intent.UNKNOWN
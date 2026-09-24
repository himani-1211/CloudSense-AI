from enum import Enum


class Intent(str, Enum):

    # ---------------- Conversation ----------------

    GREETING = "greeting"
    HELP = "help"
    THANKS = "thanks"
    GOODBYE = "goodbye"

    # ---------------- Knowledge ----------------

    KNOWLEDGE = "knowledge"

    # ---------------- AWS ----------------

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

    RECOMMENDATION = "recommendation"

    UNKNOWN = "unknown"


def detect_intent(question: str) -> Intent:

    q = question.lower().strip()

    # ====================================================
    # Greetings
    # ====================================================

    if q in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    ]:
        return Intent.GREETING

    # ====================================================
    # Thanks
    # ====================================================

    if any(word in q for word in [
        "thanks",
        "thank you",
        "thankyou",
    ]):
        return Intent.THANKS

    # ====================================================
    # Goodbye
    # ====================================================

    if any(word in q for word in [
        "bye",
        "goodbye",
        "see you",
    ]):
        return Intent.GOODBYE

    # ====================================================
    # Help
    # ====================================================

    if any(word in q for word in [
        "help",
        "what can you do",
        "who are you",
    ]):
        return Intent.HELP

    # ====================================================
    # Cloud Knowledge
    # ====================================================

    knowledge_words = [
        "what is",
        "how to",
        "how do i",
        "difference",
        "explain",
        "best practices",
    ]

    if any(word in q for word in knowledge_words):
        return Intent.KNOWLEDGE

    # ====================================================
    # Recommendations
    # ====================================================

    if any(word in q for word in [
        "recommend",
        "optimization",
        "improve",
        "improvements",
        "security",
        "cost",
    ]):
        return Intent.RECOMMENDATION

    # ====================================================
    # Infrastructure Summary
    # ====================================================

    if any(word in q for word in [
        "summary",
        "overview",
        "infrastructure",
    ]):
        return Intent.SUMMARY

    # ====================================================
    # EC2
    # ====================================================

    if "ec2" in q or "instance" in q:

        if any(word in q for word in [
            "count",
            "how many",
            "number",
        ]):
            return Intent.EC2_COUNT

        return Intent.EC2_LIST

    # ====================================================
    # S3
    # ====================================================

    if "s3" in q or "bucket" in q:

        if any(word in q for word in [
            "count",
            "how many",
            "number",
        ]):
            return Intent.S3_COUNT

        return Intent.S3_LIST

    # ====================================================
    # Lambda
    # ====================================================

    if "lambda" in q:

        if any(word in q for word in [
            "count",
            "how many",
            "number",
        ]):
            return Intent.LAMBDA_COUNT

        return Intent.LAMBDA_LIST

    # ====================================================
    # RDS
    # ====================================================

    if "rds" in q or "database" in q:

        if any(word in q for word in [
            "count",
            "how many",
            "number",
        ]):
            return Intent.RDS_COUNT

        return Intent.RDS_LIST

    # ====================================================
    # VPC
    # ====================================================

    if "vpc" in q:

        if any(word in q for word in [
            "count",
            "how many",
            "number",
        ]):
            return Intent.VPC_COUNT

        return Intent.VPC_LIST

    # ====================================================
    # EBS
    # ====================================================

    if "ebs" in q or "volume" in q:

        if any(word in q for word in [
            "count",
            "how many",
            "number",
        ]):
            return Intent.EBS_COUNT

        return Intent.EBS_LIST

    return Intent.UNKNOWN
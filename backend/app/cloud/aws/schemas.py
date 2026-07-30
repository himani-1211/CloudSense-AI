from pydantic import BaseModel, Field
from datetime import datetime

class AWSConnectRequest(BaseModel):
    access_key: str = Field(..., min_length=16)
    secret_key: str = Field(..., min_length=20)
    region: str


class AWSConnectResponse(BaseModel):
    account_id: str
    user_arn: str
    region: str
    message: str


class EC2InstanceResponse(BaseModel):
    instance_id: str
    state: str
    instance_type: str

class S3BucketResponse(BaseModel):
    name: str
    creation_date: datetime

class VPCResponse(BaseModel):
    vpc_id: str
    cidr_block: str
    state: str
    is_default: bool

class IAMUserResponse(BaseModel):
    user_name: str
    user_id: str
    arn: str
    create_date: datetime

class LambdaResponse(BaseModel):
    function_name: str
    runtime: str | None
    last_modified: str


class RDSResponse(BaseModel):
    db_instance_identifier: str
    engine: str
    status: str


class EBSResponse(BaseModel):
    volume_id: str
    size: int
    state: str
    volume_type: str

class AWSStatusResponse(BaseModel):
    connected: bool
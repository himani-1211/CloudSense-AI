from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.cloud.aws.schemas import (
    AWSConnectRequest,
    AWSConnectResponse,
    EC2InstanceResponse,
    S3BucketResponse,
    VPCResponse,
    IAMUserResponse,
    LambdaResponse,
    RDSResponse,
    EBSResponse,
)
from app.cloud.aws.service import connect_aws
from app.cloud.aws.resource_service import (
    list_ec2_instances,
    list_s3_buckets,
    list_vpcs,
    list_iam_users,
    list_lambda_functions,
    list_rds_instances,
    list_ebs_volumes,
)
from app.core.database import get_db
from app.models.user import User

router = APIRouter(
    prefix="/aws",
    tags=["AWS"],
)


@router.post(
    "/connect",
    response_model=AWSConnectResponse,
)
def connect(
    request: AWSConnectRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return connect_aws(
        data=request,
        db=db,
        current_user=current_user,
    )


@router.get(
    "/ec2",
    response_model=list[EC2InstanceResponse],
)
def get_ec2_instances(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_ec2_instances(
        db=db,
        current_user=current_user,
    )

@router.get(
    "/s3",
    response_model=list[S3BucketResponse],
)
def get_s3_buckets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_s3_buckets(
        db=db,
        current_user=current_user,
    )

@router.get(
    "/vpcs",
    response_model=list[VPCResponse],
)
def get_vpcs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_vpcs(
        db=db,
        current_user=current_user,
    )

@router.get(
    "/iam",
    response_model=list[IAMUserResponse],
)
def get_iam_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_iam_users(
        db=db,
        current_user=current_user,
    )

@router.get(
    "/lambda",
    response_model=list[LambdaResponse],
)
def get_lambda_functions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_lambda_functions(
        db=db,
        current_user=current_user,
    )

@router.get(
    "/rds",
    response_model=list[RDSResponse],
)
def get_rds_instances(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_rds_instances(
        db=db,
        current_user=current_user,
    )

@router.get(
    "/ebs",
    response_model=list[EBSResponse],
)
def get_ebs_volumes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_ebs_volumes(
        db=db,
        current_user=current_user,
    )
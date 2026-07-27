from sqlalchemy.orm import Session

from app.cloud.aws.credential_manager import get_authenticated_client
from app.models.user import User


def discover_lambda_functions(
    db: Session,
    current_user: User,
):
    client = get_authenticated_client(
        service_name="lambda",
        db=db,
        current_user=current_user,
    )

    response = client.list_functions()

    functions = []

    for function in response.get("Functions", []):
        functions.append(
            {
                "function_name": function["FunctionName"],
                "runtime": function.get("Runtime"),
                "last_modified": function["LastModified"],
            }
        )

    return functions
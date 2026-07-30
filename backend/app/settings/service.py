from sqlalchemy.orm import Session

from app.cloud.aws.models import AWSAccount
from app.models.user import User
from app.settings.schemas import (
    SettingItem,
    SettingsSummary,
    WorkspaceStatus,
)


def get_settings_summary(
    db: Session,
    current_user: User,
) -> SettingsSummary:
    """
    Returns the settings overview for the authenticated user.
    """

    aws_account = (
        db.query(AWSAccount)
        .filter(AWSAccount.owner_id == current_user.id)
        .first()
    )

    sections = [
        SettingItem(
            title="Profile",
            description="Manage your account information and preferences.",
        ),
        SettingItem(
            title="Notifications",
            description="Configure alerts and notification channels.",
        ),
        SettingItem(
            title="Security",
            description="Passwords, MFA and access management.",
        ),
        SettingItem(
            title="API Keys",
            description="Generate and manage API credentials.",
        ),
        SettingItem(
            title="Cloud Integrations",
            description="Manage connected cloud accounts and permissions.",
        ),
    ]

    workspace_status = WorkspaceStatus(
        workspace="Healthy",
        ai_services="Online",
        connected_clouds="1 Active" if aws_account else "0 Active",
    )

    return SettingsSummary(
        sections=sections,
        workspace_status=workspace_status,
    )
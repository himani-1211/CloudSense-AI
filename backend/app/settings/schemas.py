from pydantic import BaseModel, Field


# -----------------------------
# Settings Section
# -----------------------------
class SettingItem(BaseModel):
    title: str
    description: str


# -----------------------------
# Workspace Status
# -----------------------------
class WorkspaceStatus(BaseModel):
    workspace: str
    ai_services: str
    connected_clouds: str


# -----------------------------
# Response
# -----------------------------
class SettingsSummary(BaseModel):
    sections: list[SettingItem] = Field(default_factory=list)

    workspace_status: WorkspaceStatus
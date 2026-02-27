from enum import Enum


class PostByOrgApiKeysBodyScopesItem(str, Enum):
    ADMIN = "admin"
    GITREAD = "git:read"
    GITWRITE = "git:write"
    REPOCREATE = "repo:create"
    REPODELETE = "repo:delete"
    REPOREAD = "repo:read"
    WEBHOOKREAD = "webhook:read"
    WEBHOOKWRITE = "webhook:write"

    def __str__(self) -> str:
        return str(self.value)

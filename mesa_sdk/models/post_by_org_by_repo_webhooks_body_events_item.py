from enum import Enum


class PostByOrgByRepoWebhooksBodyEventsItem(str, Enum):
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)

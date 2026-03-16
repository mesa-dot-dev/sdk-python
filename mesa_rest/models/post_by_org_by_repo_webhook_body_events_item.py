from enum import Enum

class PostByOrgByRepoWebhookBodyEventsItem(str, Enum):
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)

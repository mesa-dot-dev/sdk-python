from enum import Enum


class PostByOrgByRepoWebhooksResponse201EventsItem(str, Enum):
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class GetByOrgByRepoWebhookResponse200WebhooksItemEventsItem(str, Enum):
    PUSH = "push"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum

class PostByOrgRepoBodyUpstreamAutosyncType0ResolutionStrategy(str, Enum):
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)

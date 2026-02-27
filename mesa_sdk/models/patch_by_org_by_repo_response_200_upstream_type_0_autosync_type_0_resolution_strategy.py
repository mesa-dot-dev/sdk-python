from enum import Enum


class PatchByOrgByRepoResponse200UpstreamType0AutosyncType0ResolutionStrategy(str, Enum):
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)

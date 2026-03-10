from enum import Enum

class PostByOrgByRepoCommitsBodyFilesItemType0Mode(str, Enum):
    VALUE_0 = "100644"
    VALUE_1 = "100755"

    def __str__(self) -> str:
        return str(self.value)

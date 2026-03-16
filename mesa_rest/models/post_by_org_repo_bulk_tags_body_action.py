from enum import Enum

class PostByOrgRepoBulkTagsBodyAction(str, Enum):
    REMOVE = "remove"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)

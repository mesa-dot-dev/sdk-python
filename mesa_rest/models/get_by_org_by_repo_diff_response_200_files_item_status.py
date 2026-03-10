from enum import Enum

class GetByOrgByRepoDiffResponse200FilesItemStatus(str, Enum):
    A = "A"
    C = "C"
    D = "D"
    M = "M"
    R = "R"
    T = "T"

    def __str__(self) -> str:
        return str(self.value)

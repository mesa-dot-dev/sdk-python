from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetByOrgByRepoDiffResponse200Stats")



@_attrs_define
class GetByOrgByRepoDiffResponse200Stats:
    """ 
        Attributes:
            files (float):
            additions (float):
            deletions (float):
            changes (float):
     """

    files: float
    additions: float
    deletions: float
    changes: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        files = self.files

        additions = self.additions

        deletions = self.deletions

        changes = self.changes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "files": files,
            "additions": additions,
            "deletions": deletions,
            "changes": changes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        files = d.pop("files")

        additions = d.pop("additions")

        deletions = d.pop("deletions")

        changes = d.pop("changes")

        get_by_org_by_repo_diff_response_200_stats = cls(
            files=files,
            additions=additions,
            deletions=deletions,
            changes=changes,
        )


        get_by_org_by_repo_diff_response_200_stats.additional_properties = d
        return get_by_org_by_repo_diff_response_200_stats

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

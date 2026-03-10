from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="PostByOrgByRepoCommitsBodyFilesItemType1")



@_attrs_define
class PostByOrgByRepoCommitsBodyFilesItemType1:
    """ 
        Attributes:
            path (str):
            action (Literal['delete']):
     """

    path: str
    action: Literal['delete']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        action = self.action


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "action": action,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        action = cast(Literal['delete'] , d.pop("action"))
        if action != 'delete':
            raise ValueError(f"action must match const 'delete', got '{action}'")

        post_by_org_by_repo_commits_body_files_item_type_1 = cls(
            path=path,
            action=action,
        )


        post_by_org_by_repo_commits_body_files_item_type_1.additional_properties = d
        return post_by_org_by_repo_commits_body_files_item_type_1

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetByOrgByRepoContentResponse200Type2EntriesItemType2")


@_attrs_define
class GetByOrgByRepoContentResponse200Type2EntriesItemType2:
    """
    Attributes:
        type_ (Literal['dir']):
        name (str):
        path (str):
        sha (str):
    """

    type_: Literal["dir"]
    name: str
    path: str
    sha: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        path = self.path

        sha = self.sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "path": path,
                "sha": sha,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["dir"], d.pop("type"))
        if type_ != "dir":
            raise ValueError(f"type must match const 'dir', got '{type_}'")

        name = d.pop("name")

        path = d.pop("path")

        sha = d.pop("sha")

        get_by_org_by_repo_content_response_200_type_2_entries_item_type_2 = cls(
            type_=type_,
            name=name,
            path=path,
            sha=sha,
        )

        get_by_org_by_repo_content_response_200_type_2_entries_item_type_2.additional_properties = d
        return get_by_org_by_repo_content_response_200_type_2_entries_item_type_2

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

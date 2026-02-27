from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetByOrgByRepoContentResponse200Type2EntriesItemType0")


@_attrs_define
class GetByOrgByRepoContentResponse200Type2EntriesItemType0:
    """
    Attributes:
        type_ (Literal['file']):
        name (str):
        path (str):
        sha (str):
        size (float):
        mode (int):
    """

    type_: Literal["file"]
    name: str
    path: str
    sha: str
    size: float
    mode: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        path = self.path

        sha = self.sha

        size = self.size

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "path": path,
                "sha": sha,
                "size": size,
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["file"], d.pop("type"))
        if type_ != "file":
            raise ValueError(f"type must match const 'file', got '{type_}'")

        name = d.pop("name")

        path = d.pop("path")

        sha = d.pop("sha")

        size = d.pop("size")

        mode = d.pop("mode")

        get_by_org_by_repo_content_response_200_type_2_entries_item_type_0 = cls(
            type_=type_,
            name=name,
            path=path,
            sha=sha,
            size=size,
            mode=mode,
        )

        get_by_org_by_repo_content_response_200_type_2_entries_item_type_0.additional_properties = d
        return get_by_org_by_repo_content_response_200_type_2_entries_item_type_0

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

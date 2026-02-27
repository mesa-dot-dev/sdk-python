from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetByOrgByRepoContentResponse200Type1")


@_attrs_define
class GetByOrgByRepoContentResponse200Type1:
    """
    Attributes:
        type_ (Literal['symlink']):
        name (str):
        path (str):
        sha (str):
        size (float):
        encoding (Literal['base64']):
        content (str):
        mode (int):
    """

    type_: Literal["symlink"]
    name: str
    path: str
    sha: str
    size: float
    encoding: Literal["base64"]
    content: str
    mode: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        path = self.path

        sha = self.sha

        size = self.size

        encoding = self.encoding

        content = self.content

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
                "encoding": encoding,
                "content": content,
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["symlink"], d.pop("type"))
        if type_ != "symlink":
            raise ValueError(f"type must match const 'symlink', got '{type_}'")

        name = d.pop("name")

        path = d.pop("path")

        sha = d.pop("sha")

        size = d.pop("size")

        encoding = cast(Literal["base64"], d.pop("encoding"))
        if encoding != "base64":
            raise ValueError(f"encoding must match const 'base64', got '{encoding}'")

        content = d.pop("content")

        mode = d.pop("mode")

        get_by_org_by_repo_content_response_200_type_1 = cls(
            type_=type_,
            name=name,
            path=path,
            sha=sha,
            size=size,
            encoding=encoding,
            content=content,
            mode=mode,
        )

        get_by_org_by_repo_content_response_200_type_1.additional_properties = d
        return get_by_org_by_repo_content_response_200_type_1

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

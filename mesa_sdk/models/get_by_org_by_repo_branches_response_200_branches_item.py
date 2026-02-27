from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetByOrgByRepoBranchesResponse200BranchesItem")


@_attrs_define
class GetByOrgByRepoBranchesResponse200BranchesItem:
    """
    Attributes:
        name (str):
        head_oid (str):
        is_default (bool):
    """

    name: str
    head_oid: str
    is_default: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        head_oid = self.head_oid

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "head_oid": head_oid,
                "is_default": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        head_oid = d.pop("head_oid")

        is_default = d.pop("is_default")

        get_by_org_by_repo_branches_response_200_branches_item = cls(
            name=name,
            head_oid=head_oid,
            is_default=is_default,
        )

        get_by_org_by_repo_branches_response_200_branches_item.additional_properties = d
        return get_by_org_by_repo_branches_response_200_branches_item

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

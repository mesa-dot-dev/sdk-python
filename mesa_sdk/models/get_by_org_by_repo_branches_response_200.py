from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_by_org_by_repo_branches_response_200_branches_item import (
        GetByOrgByRepoBranchesResponse200BranchesItem,
    )


T = TypeVar("T", bound="GetByOrgByRepoBranchesResponse200")


@_attrs_define
class GetByOrgByRepoBranchesResponse200:
    """
    Attributes:
        next_cursor (None | str):
        has_more (bool):
        branches (list[GetByOrgByRepoBranchesResponse200BranchesItem]):
    """

    next_cursor: None | str
    has_more: bool
    branches: list[GetByOrgByRepoBranchesResponse200BranchesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        branches = []
        for branches_item_data in self.branches:
            branches_item = branches_item_data.to_dict()
            branches.append(branches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next_cursor": next_cursor,
                "has_more": has_more,
                "branches": branches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_by_repo_branches_response_200_branches_item import (
            GetByOrgByRepoBranchesResponse200BranchesItem,
        )

        d = dict(src_dict)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        has_more = d.pop("has_more")

        branches = []
        _branches = d.pop("branches")
        for branches_item_data in _branches:
            branches_item = GetByOrgByRepoBranchesResponse200BranchesItem.from_dict(branches_item_data)

            branches.append(branches_item)

        get_by_org_by_repo_branches_response_200 = cls(
            next_cursor=next_cursor,
            has_more=has_more,
            branches=branches,
        )

        get_by_org_by_repo_branches_response_200.additional_properties = d
        return get_by_org_by_repo_branches_response_200

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

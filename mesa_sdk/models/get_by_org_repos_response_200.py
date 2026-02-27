from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_by_org_repos_response_200_repos_item import GetByOrgReposResponse200ReposItem


T = TypeVar("T", bound="GetByOrgReposResponse200")


@_attrs_define
class GetByOrgReposResponse200:
    """
    Attributes:
        next_cursor (None | str):
        has_more (bool):
        repos (list[GetByOrgReposResponse200ReposItem]):
    """

    next_cursor: None | str
    has_more: bool
    repos: list[GetByOrgReposResponse200ReposItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        repos = []
        for repos_item_data in self.repos:
            repos_item = repos_item_data.to_dict()
            repos.append(repos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next_cursor": next_cursor,
                "has_more": has_more,
                "repos": repos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_repos_response_200_repos_item import GetByOrgReposResponse200ReposItem

        d = dict(src_dict)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        has_more = d.pop("has_more")

        repos = []
        _repos = d.pop("repos")
        for repos_item_data in _repos:
            repos_item = GetByOrgReposResponse200ReposItem.from_dict(repos_item_data)

            repos.append(repos_item)

        get_by_org_repos_response_200 = cls(
            next_cursor=next_cursor,
            has_more=has_more,
            repos=repos,
        )

        get_by_org_repos_response_200.additional_properties = d
        return get_by_org_repos_response_200

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

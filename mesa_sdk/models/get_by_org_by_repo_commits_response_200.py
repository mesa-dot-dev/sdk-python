from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_by_org_by_repo_commits_response_200_commits_item import (
        GetByOrgByRepoCommitsResponse200CommitsItem,
    )


T = TypeVar("T", bound="GetByOrgByRepoCommitsResponse200")


@_attrs_define
class GetByOrgByRepoCommitsResponse200:
    """
    Attributes:
        next_cursor (None | str):
        has_more (bool):
        commits (list[GetByOrgByRepoCommitsResponse200CommitsItem]):
    """

    next_cursor: None | str
    has_more: bool
    commits: list[GetByOrgByRepoCommitsResponse200CommitsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        commits = []
        for commits_item_data in self.commits:
            commits_item = commits_item_data.to_dict()
            commits.append(commits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next_cursor": next_cursor,
                "has_more": has_more,
                "commits": commits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_by_repo_commits_response_200_commits_item import (
            GetByOrgByRepoCommitsResponse200CommitsItem,
        )

        d = dict(src_dict)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        has_more = d.pop("has_more")

        commits = []
        _commits = d.pop("commits")
        for commits_item_data in _commits:
            commits_item = GetByOrgByRepoCommitsResponse200CommitsItem.from_dict(commits_item_data)

            commits.append(commits_item)

        get_by_org_by_repo_commits_response_200 = cls(
            next_cursor=next_cursor,
            has_more=has_more,
            commits=commits,
        )

        get_by_org_by_repo_commits_response_200.additional_properties = d
        return get_by_org_by_repo_commits_response_200

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

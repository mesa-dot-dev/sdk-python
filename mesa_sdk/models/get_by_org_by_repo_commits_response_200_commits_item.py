from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_by_org_by_repo_commits_response_200_commits_item_author import (
        GetByOrgByRepoCommitsResponse200CommitsItemAuthor,
    )
    from ..models.get_by_org_by_repo_commits_response_200_commits_item_committer import (
        GetByOrgByRepoCommitsResponse200CommitsItemCommitter,
    )


T = TypeVar("T", bound="GetByOrgByRepoCommitsResponse200CommitsItem")


@_attrs_define
class GetByOrgByRepoCommitsResponse200CommitsItem:
    """
    Attributes:
        sha (str):
        message (str):
        author (GetByOrgByRepoCommitsResponse200CommitsItemAuthor):
        committer (GetByOrgByRepoCommitsResponse200CommitsItemCommitter):
    """

    sha: str
    message: str
    author: GetByOrgByRepoCommitsResponse200CommitsItemAuthor
    committer: GetByOrgByRepoCommitsResponse200CommitsItemCommitter
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sha = self.sha

        message = self.message

        author = self.author.to_dict()

        committer = self.committer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sha": sha,
                "message": message,
                "author": author,
                "committer": committer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_by_repo_commits_response_200_commits_item_author import (
            GetByOrgByRepoCommitsResponse200CommitsItemAuthor,
        )
        from ..models.get_by_org_by_repo_commits_response_200_commits_item_committer import (
            GetByOrgByRepoCommitsResponse200CommitsItemCommitter,
        )

        d = dict(src_dict)
        sha = d.pop("sha")

        message = d.pop("message")

        author = GetByOrgByRepoCommitsResponse200CommitsItemAuthor.from_dict(d.pop("author"))

        committer = GetByOrgByRepoCommitsResponse200CommitsItemCommitter.from_dict(d.pop("committer"))

        get_by_org_by_repo_commits_response_200_commits_item = cls(
            sha=sha,
            message=message,
            author=author,
            committer=committer,
        )

        get_by_org_by_repo_commits_response_200_commits_item.additional_properties = d
        return get_by_org_by_repo_commits_response_200_commits_item

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

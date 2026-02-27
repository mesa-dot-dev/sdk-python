from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_by_org_by_repo_commits_by_sha_response_200_author import (
        GetByOrgByRepoCommitsByShaResponse200Author,
    )
    from ..models.get_by_org_by_repo_commits_by_sha_response_200_committer import (
        GetByOrgByRepoCommitsByShaResponse200Committer,
    )


T = TypeVar("T", bound="GetByOrgByRepoCommitsByShaResponse200")


@_attrs_define
class GetByOrgByRepoCommitsByShaResponse200:
    """
    Attributes:
        sha (str):
        message (str):
        author (GetByOrgByRepoCommitsByShaResponse200Author):
        committer (GetByOrgByRepoCommitsByShaResponse200Committer):
    """

    sha: str
    message: str
    author: GetByOrgByRepoCommitsByShaResponse200Author
    committer: GetByOrgByRepoCommitsByShaResponse200Committer
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
        from ..models.get_by_org_by_repo_commits_by_sha_response_200_author import (
            GetByOrgByRepoCommitsByShaResponse200Author,
        )
        from ..models.get_by_org_by_repo_commits_by_sha_response_200_committer import (
            GetByOrgByRepoCommitsByShaResponse200Committer,
        )

        d = dict(src_dict)
        sha = d.pop("sha")

        message = d.pop("message")

        author = GetByOrgByRepoCommitsByShaResponse200Author.from_dict(d.pop("author"))

        committer = GetByOrgByRepoCommitsByShaResponse200Committer.from_dict(d.pop("committer"))

        get_by_org_by_repo_commits_by_sha_response_200 = cls(
            sha=sha,
            message=message,
            author=author,
            committer=committer,
        )

        get_by_org_by_repo_commits_by_sha_response_200.additional_properties = d
        return get_by_org_by_repo_commits_by_sha_response_200

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

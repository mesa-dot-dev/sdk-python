from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.post_by_org_by_repo_commit_body_author import PostByOrgByRepoCommitBodyAuthor
  from ..models.post_by_org_by_repo_commit_body_committer import PostByOrgByRepoCommitBodyCommitter
  from ..models.post_by_org_by_repo_commit_body_files_item_type_0 import PostByOrgByRepoCommitBodyFilesItemType0
  from ..models.post_by_org_by_repo_commit_body_files_item_type_1 import PostByOrgByRepoCommitBodyFilesItemType1





T = TypeVar("T", bound="PostByOrgByRepoCommitBody")



@_attrs_define
class PostByOrgByRepoCommitBody:
    """ 
        Attributes:
            branch (str):
            message (str):
            author (PostByOrgByRepoCommitBodyAuthor):
            files (list[PostByOrgByRepoCommitBodyFilesItemType0 | PostByOrgByRepoCommitBodyFilesItemType1]):
            committer (PostByOrgByRepoCommitBodyCommitter | Unset):
            base_sha (str | Unset):
     """

    branch: str
    message: str
    author: PostByOrgByRepoCommitBodyAuthor
    files: list[PostByOrgByRepoCommitBodyFilesItemType0 | PostByOrgByRepoCommitBodyFilesItemType1]
    committer: PostByOrgByRepoCommitBodyCommitter | Unset = UNSET
    base_sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_by_org_by_repo_commit_body_author import PostByOrgByRepoCommitBodyAuthor
        from ..models.post_by_org_by_repo_commit_body_files_item_type_1 import PostByOrgByRepoCommitBodyFilesItemType1
        from ..models.post_by_org_by_repo_commit_body_files_item_type_0 import PostByOrgByRepoCommitBodyFilesItemType0
        from ..models.post_by_org_by_repo_commit_body_committer import PostByOrgByRepoCommitBodyCommitter
        branch = self.branch

        message = self.message

        author = self.author.to_dict()

        files = []
        for files_item_data in self.files:
            files_item: dict[str, Any]
            if isinstance(files_item_data, PostByOrgByRepoCommitBodyFilesItemType0):
                files_item = files_item_data.to_dict()
            else:
                files_item = files_item_data.to_dict()

            files.append(files_item)



        committer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        base_sha = self.base_sha


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "branch": branch,
            "message": message,
            "author": author,
            "files": files,
        })
        if committer is not UNSET:
            field_dict["committer"] = committer
        if base_sha is not UNSET:
            field_dict["base_sha"] = base_sha

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_by_org_by_repo_commit_body_author import PostByOrgByRepoCommitBodyAuthor
        from ..models.post_by_org_by_repo_commit_body_committer import PostByOrgByRepoCommitBodyCommitter
        from ..models.post_by_org_by_repo_commit_body_files_item_type_0 import PostByOrgByRepoCommitBodyFilesItemType0
        from ..models.post_by_org_by_repo_commit_body_files_item_type_1 import PostByOrgByRepoCommitBodyFilesItemType1
        d = dict(src_dict)
        branch = d.pop("branch")

        message = d.pop("message")

        author = PostByOrgByRepoCommitBodyAuthor.from_dict(d.pop("author"))




        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            def _parse_files_item(data: object) -> PostByOrgByRepoCommitBodyFilesItemType0 | PostByOrgByRepoCommitBodyFilesItemType1:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    files_item_type_0 = PostByOrgByRepoCommitBodyFilesItemType0.from_dict(data)



                    return files_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                files_item_type_1 = PostByOrgByRepoCommitBodyFilesItemType1.from_dict(data)



                return files_item_type_1

            files_item = _parse_files_item(files_item_data)

            files.append(files_item)


        _committer = d.pop("committer", UNSET)
        committer: PostByOrgByRepoCommitBodyCommitter | Unset
        if isinstance(_committer,  Unset):
            committer = UNSET
        else:
            committer = PostByOrgByRepoCommitBodyCommitter.from_dict(_committer)




        base_sha = d.pop("base_sha", UNSET)

        post_by_org_by_repo_commit_body = cls(
            branch=branch,
            message=message,
            author=author,
            files=files,
            committer=committer,
            base_sha=base_sha,
        )


        post_by_org_by_repo_commit_body.additional_properties = d
        return post_by_org_by_repo_commit_body

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

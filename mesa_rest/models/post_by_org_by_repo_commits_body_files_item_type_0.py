from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_by_org_by_repo_commits_body_files_item_type_0_encoding import PostByOrgByRepoCommitsBodyFilesItemType0Encoding
from ..models.post_by_org_by_repo_commits_body_files_item_type_0_mode import PostByOrgByRepoCommitsBodyFilesItemType0Mode
from ..types import UNSET, Unset
from typing import Literal, cast






T = TypeVar("T", bound="PostByOrgByRepoCommitsBodyFilesItemType0")



@_attrs_define
class PostByOrgByRepoCommitsBodyFilesItemType0:
    """ 
        Attributes:
            path (str):
            content (str):
            encoding (PostByOrgByRepoCommitsBodyFilesItemType0Encoding | Unset):  Default:
                PostByOrgByRepoCommitsBodyFilesItemType0Encoding.UTF_8.
            action (Literal['upsert'] | Unset):
            mode (PostByOrgByRepoCommitsBodyFilesItemType0Mode | Unset):
     """

    path: str
    content: str
    encoding: PostByOrgByRepoCommitsBodyFilesItemType0Encoding | Unset = PostByOrgByRepoCommitsBodyFilesItemType0Encoding.UTF_8
    action: Literal['upsert'] | Unset = UNSET
    mode: PostByOrgByRepoCommitsBodyFilesItemType0Mode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        content = self.content

        encoding: str | Unset = UNSET
        if not isinstance(self.encoding, Unset):
            encoding = self.encoding.value


        action = self.action

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "content": content,
        })
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if action is not UNSET:
            field_dict["action"] = action
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        content = d.pop("content")

        _encoding = d.pop("encoding", UNSET)
        encoding: PostByOrgByRepoCommitsBodyFilesItemType0Encoding | Unset
        if isinstance(_encoding,  Unset):
            encoding = UNSET
        else:
            encoding = PostByOrgByRepoCommitsBodyFilesItemType0Encoding(_encoding)




        action = cast(Literal['upsert'] | Unset , d.pop("action", UNSET))
        if action != 'upsert'and not isinstance(action, Unset):
            raise ValueError(f"action must match const 'upsert', got '{action}'")

        _mode = d.pop("mode", UNSET)
        mode: PostByOrgByRepoCommitsBodyFilesItemType0Mode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = PostByOrgByRepoCommitsBodyFilesItemType0Mode(_mode)




        post_by_org_by_repo_commits_body_files_item_type_0 = cls(
            path=path,
            content=content,
            encoding=encoding,
            action=action,
            mode=mode,
        )


        post_by_org_by_repo_commits_body_files_item_type_0.additional_properties = d
        return post_by_org_by_repo_commits_body_files_item_type_0

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

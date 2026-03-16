from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.post_by_org_repo_body_tags import PostByOrgRepoBodyTags
  from ..models.post_by_org_repo_body_upstream import PostByOrgRepoBodyUpstream





T = TypeVar("T", bound="PostByOrgRepoBody")



@_attrs_define
class PostByOrgRepoBody:
    """ 
        Attributes:
            name (str):
            default_branch (str | Unset):  Default: 'main'.
            tags (PostByOrgRepoBodyTags | Unset):
            upstream (PostByOrgRepoBodyUpstream | Unset):
     """

    name: str
    default_branch: str | Unset = 'main'
    tags: PostByOrgRepoBodyTags | Unset = UNSET
    upstream: PostByOrgRepoBodyUpstream | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_by_org_repo_body_tags import PostByOrgRepoBodyTags
        from ..models.post_by_org_repo_body_upstream import PostByOrgRepoBodyUpstream
        name = self.name

        default_branch = self.default_branch

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        upstream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upstream, Unset):
            upstream = self.upstream.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if tags is not UNSET:
            field_dict["tags"] = tags
        if upstream is not UNSET:
            field_dict["upstream"] = upstream

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_by_org_repo_body_tags import PostByOrgRepoBodyTags
        from ..models.post_by_org_repo_body_upstream import PostByOrgRepoBodyUpstream
        d = dict(src_dict)
        name = d.pop("name")

        default_branch = d.pop("default_branch", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: PostByOrgRepoBodyTags | Unset
        if isinstance(_tags,  Unset):
            tags = UNSET
        else:
            tags = PostByOrgRepoBodyTags.from_dict(_tags)




        _upstream = d.pop("upstream", UNSET)
        upstream: PostByOrgRepoBodyUpstream | Unset
        if isinstance(_upstream,  Unset):
            upstream = UNSET
        else:
            upstream = PostByOrgRepoBodyUpstream.from_dict(_upstream)




        post_by_org_repo_body = cls(
            name=name,
            default_branch=default_branch,
            tags=tags,
            upstream=upstream,
        )


        post_by_org_repo_body.additional_properties = d
        return post_by_org_repo_body

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

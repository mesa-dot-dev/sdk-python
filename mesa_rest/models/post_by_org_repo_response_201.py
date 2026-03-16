from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.post_by_org_repo_response_201_tags import PostByOrgRepoResponse201Tags
  from ..models.post_by_org_repo_response_201_upstream_type_0 import PostByOrgRepoResponse201UpstreamType0





T = TypeVar("T", bound="PostByOrgRepoResponse201")



@_attrs_define
class PostByOrgRepoResponse201:
    """ 
        Attributes:
            id (str):
            org (str):
            name (str):
            default_branch (str):
            head_oid (None | str):
            created_at (str):
            tags (PostByOrgRepoResponse201Tags):
            upstream (None | PostByOrgRepoResponse201UpstreamType0): Optionally add an upstream repository. You can
                configure automatic syncing from the upstream repository.
     """

    id: str
    org: str
    name: str
    default_branch: str
    head_oid: None | str
    created_at: str
    tags: PostByOrgRepoResponse201Tags
    upstream: None | PostByOrgRepoResponse201UpstreamType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_by_org_repo_response_201_tags import PostByOrgRepoResponse201Tags
        from ..models.post_by_org_repo_response_201_upstream_type_0 import PostByOrgRepoResponse201UpstreamType0
        id = self.id

        org = self.org

        name = self.name

        default_branch = self.default_branch

        head_oid: None | str
        head_oid = self.head_oid

        created_at = self.created_at

        tags = self.tags.to_dict()

        upstream: dict[str, Any] | None
        if isinstance(self.upstream, PostByOrgRepoResponse201UpstreamType0):
            upstream = self.upstream.to_dict()
        else:
            upstream = self.upstream


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "org": org,
            "name": name,
            "default_branch": default_branch,
            "head_oid": head_oid,
            "created_at": created_at,
            "tags": tags,
            "upstream": upstream,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_by_org_repo_response_201_tags import PostByOrgRepoResponse201Tags
        from ..models.post_by_org_repo_response_201_upstream_type_0 import PostByOrgRepoResponse201UpstreamType0
        d = dict(src_dict)
        id = d.pop("id")

        org = d.pop("org")

        name = d.pop("name")

        default_branch = d.pop("default_branch")

        def _parse_head_oid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        head_oid = _parse_head_oid(d.pop("head_oid"))


        created_at = d.pop("created_at")

        tags = PostByOrgRepoResponse201Tags.from_dict(d.pop("tags"))




        def _parse_upstream(data: object) -> None | PostByOrgRepoResponse201UpstreamType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upstream_type_0 = PostByOrgRepoResponse201UpstreamType0.from_dict(data)



                return upstream_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostByOrgRepoResponse201UpstreamType0, data)

        upstream = _parse_upstream(d.pop("upstream"))


        post_by_org_repo_response_201 = cls(
            id=id,
            org=org,
            name=name,
            default_branch=default_branch,
            head_oid=head_oid,
            created_at=created_at,
            tags=tags,
            upstream=upstream,
        )


        post_by_org_repo_response_201.additional_properties = d
        return post_by_org_repo_response_201

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_by_org_repos_body_upstream import PostByOrgReposBodyUpstream


T = TypeVar("T", bound="PostByOrgReposBody")


@_attrs_define
class PostByOrgReposBody:
    """
    Attributes:
        name (str):
        default_branch (str | Unset):  Default: 'main'.
        upstream (PostByOrgReposBodyUpstream | Unset):
    """

    name: str
    default_branch: str | Unset = "main"
    upstream: PostByOrgReposBodyUpstream | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        default_branch = self.default_branch

        upstream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upstream, Unset):
            upstream = self.upstream.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if upstream is not UNSET:
            field_dict["upstream"] = upstream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_by_org_repos_body_upstream import PostByOrgReposBodyUpstream

        d = dict(src_dict)
        name = d.pop("name")

        default_branch = d.pop("default_branch", UNSET)

        _upstream = d.pop("upstream", UNSET)
        upstream: PostByOrgReposBodyUpstream | Unset
        if isinstance(_upstream, Unset):
            upstream = UNSET
        else:
            upstream = PostByOrgReposBodyUpstream.from_dict(_upstream)

        post_by_org_repos_body = cls(
            name=name,
            default_branch=default_branch,
            upstream=upstream,
        )

        post_by_org_repos_body.additional_properties = d
        return post_by_org_repos_body

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

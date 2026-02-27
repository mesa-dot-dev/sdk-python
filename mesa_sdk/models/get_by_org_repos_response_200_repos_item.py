from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_by_org_repos_response_200_repos_item_upstream_type_0 import (
        GetByOrgReposResponse200ReposItemUpstreamType0,
    )


T = TypeVar("T", bound="GetByOrgReposResponse200ReposItem")


@_attrs_define
class GetByOrgReposResponse200ReposItem:
    """
    Attributes:
        id (str):
        org (str):
        name (str):
        default_branch (str):
        head_oid (None | str):
        size_bytes (float):
        created_at (str):
        upstream (GetByOrgReposResponse200ReposItemUpstreamType0 | None): Optionally add an upstream repository. You can
            configure automatic syncing from the upstream repository.
    """

    id: str
    org: str
    name: str
    default_branch: str
    head_oid: None | str
    size_bytes: float
    created_at: str
    upstream: GetByOrgReposResponse200ReposItemUpstreamType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_by_org_repos_response_200_repos_item_upstream_type_0 import (
            GetByOrgReposResponse200ReposItemUpstreamType0,
        )

        id = self.id

        org = self.org

        name = self.name

        default_branch = self.default_branch

        head_oid: None | str
        head_oid = self.head_oid

        size_bytes = self.size_bytes

        created_at = self.created_at

        upstream: dict[str, Any] | None
        if isinstance(self.upstream, GetByOrgReposResponse200ReposItemUpstreamType0):
            upstream = self.upstream.to_dict()
        else:
            upstream = self.upstream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org": org,
                "name": name,
                "default_branch": default_branch,
                "head_oid": head_oid,
                "size_bytes": size_bytes,
                "created_at": created_at,
                "upstream": upstream,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_repos_response_200_repos_item_upstream_type_0 import (
            GetByOrgReposResponse200ReposItemUpstreamType0,
        )

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

        size_bytes = d.pop("size_bytes")

        created_at = d.pop("created_at")

        def _parse_upstream(data: object) -> GetByOrgReposResponse200ReposItemUpstreamType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upstream_type_0 = GetByOrgReposResponse200ReposItemUpstreamType0.from_dict(data)

                return upstream_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetByOrgReposResponse200ReposItemUpstreamType0 | None, data)

        upstream = _parse_upstream(d.pop("upstream"))

        get_by_org_repos_response_200_repos_item = cls(
            id=id,
            org=org,
            name=name,
            default_branch=default_branch,
            head_oid=head_oid,
            size_bytes=size_bytes,
            created_at=created_at,
            upstream=upstream,
        )

        get_by_org_repos_response_200_repos_item.additional_properties = d
        return get_by_org_repos_response_200_repos_item

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_by_org_by_repo_body_upstream_type_0 import PatchByOrgByRepoBodyUpstreamType0


T = TypeVar("T", bound="PatchByOrgByRepoBody")


@_attrs_define
class PatchByOrgByRepoBody:
    """
    Attributes:
        name (str | Unset):
        default_branch (str | Unset):
        upstream (None | PatchByOrgByRepoBodyUpstreamType0 | Unset):
    """

    name: str | Unset = UNSET
    default_branch: str | Unset = UNSET
    upstream: None | PatchByOrgByRepoBodyUpstreamType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_by_org_by_repo_body_upstream_type_0 import PatchByOrgByRepoBodyUpstreamType0

        name = self.name

        default_branch = self.default_branch

        upstream: dict[str, Any] | None | Unset
        if isinstance(self.upstream, Unset):
            upstream = UNSET
        elif isinstance(self.upstream, PatchByOrgByRepoBodyUpstreamType0):
            upstream = self.upstream.to_dict()
        else:
            upstream = self.upstream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if default_branch is not UNSET:
            field_dict["default_branch"] = default_branch
        if upstream is not UNSET:
            field_dict["upstream"] = upstream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_by_org_by_repo_body_upstream_type_0 import PatchByOrgByRepoBodyUpstreamType0

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        default_branch = d.pop("default_branch", UNSET)

        def _parse_upstream(data: object) -> None | PatchByOrgByRepoBodyUpstreamType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upstream_type_0 = PatchByOrgByRepoBodyUpstreamType0.from_dict(data)

                return upstream_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchByOrgByRepoBodyUpstreamType0 | Unset, data)

        upstream = _parse_upstream(d.pop("upstream", UNSET))

        patch_by_org_by_repo_body = cls(
            name=name,
            default_branch=default_branch,
            upstream=upstream,
        )

        patch_by_org_by_repo_body.additional_properties = d
        return patch_by_org_by_repo_body

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

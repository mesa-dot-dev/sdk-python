from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_by_org_repos_response_201_upstream_type_0_autosync_type_0_resolution_strategy import (
    PostByOrgReposResponse201UpstreamType0AutosyncType0ResolutionStrategy,
)

T = TypeVar("T", bound="PostByOrgReposResponse201UpstreamType0AutosyncType0")


@_attrs_define
class PostByOrgReposResponse201UpstreamType0AutosyncType0:
    """
    Attributes:
        type_ (Literal['poll']):
        period (float): Polling period in seconds
        resolution_strategy (PostByOrgReposResponse201UpstreamType0AutosyncType0ResolutionStrategy): Conflict resolution
            strategy. "none" means sync will fail on conflicts.
    """

    type_: Literal["poll"]
    period: float
    resolution_strategy: PostByOrgReposResponse201UpstreamType0AutosyncType0ResolutionStrategy
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        period = self.period

        resolution_strategy = self.resolution_strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "period": period,
                "resolution_strategy": resolution_strategy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["poll"], d.pop("type"))
        if type_ != "poll":
            raise ValueError(f"type must match const 'poll', got '{type_}'")

        period = d.pop("period")

        resolution_strategy = PostByOrgReposResponse201UpstreamType0AutosyncType0ResolutionStrategy(
            d.pop("resolution_strategy")
        )

        post_by_org_repos_response_201_upstream_type_0_autosync_type_0 = cls(
            type_=type_,
            period=period,
            resolution_strategy=resolution_strategy,
        )

        post_by_org_repos_response_201_upstream_type_0_autosync_type_0.additional_properties = d
        return post_by_org_repos_response_201_upstream_type_0_autosync_type_0

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

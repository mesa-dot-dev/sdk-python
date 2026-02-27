from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_by_org_by_repo_body_upstream_type_0_autosync_type_0_resolution_strategy import (
    PatchByOrgByRepoBodyUpstreamType0AutosyncType0ResolutionStrategy,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchByOrgByRepoBodyUpstreamType0AutosyncType0")


@_attrs_define
class PatchByOrgByRepoBodyUpstreamType0AutosyncType0:
    """
    Attributes:
        type_ (Literal['poll']):
        period (int): Polling period in seconds (60s to 24.8d)
        resolution_strategy (PatchByOrgByRepoBodyUpstreamType0AutosyncType0ResolutionStrategy | Unset): Conflict
            resolution strategy. "none" means sync will fail on conflicts. Default:
            PatchByOrgByRepoBodyUpstreamType0AutosyncType0ResolutionStrategy.NONE.
    """

    type_: Literal["poll"]
    period: int
    resolution_strategy: PatchByOrgByRepoBodyUpstreamType0AutosyncType0ResolutionStrategy | Unset = (
        PatchByOrgByRepoBodyUpstreamType0AutosyncType0ResolutionStrategy.NONE
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        period = self.period

        resolution_strategy: str | Unset = UNSET
        if not isinstance(self.resolution_strategy, Unset):
            resolution_strategy = self.resolution_strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "period": period,
            }
        )
        if resolution_strategy is not UNSET:
            field_dict["resolution_strategy"] = resolution_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["poll"], d.pop("type"))
        if type_ != "poll":
            raise ValueError(f"type must match const 'poll', got '{type_}'")

        period = d.pop("period")

        _resolution_strategy = d.pop("resolution_strategy", UNSET)
        resolution_strategy: PatchByOrgByRepoBodyUpstreamType0AutosyncType0ResolutionStrategy | Unset
        if isinstance(_resolution_strategy, Unset):
            resolution_strategy = UNSET
        else:
            resolution_strategy = PatchByOrgByRepoBodyUpstreamType0AutosyncType0ResolutionStrategy(_resolution_strategy)

        patch_by_org_by_repo_body_upstream_type_0_autosync_type_0 = cls(
            type_=type_,
            period=period,
            resolution_strategy=resolution_strategy,
        )

        patch_by_org_by_repo_body_upstream_type_0_autosync_type_0.additional_properties = d
        return patch_by_org_by_repo_body_upstream_type_0_autosync_type_0

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

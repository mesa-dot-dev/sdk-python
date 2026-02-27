from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_by_org_by_repo_body_upstream_type_0_autosync_type_0 import (
        PatchByOrgByRepoBodyUpstreamType0AutosyncType0,
    )


T = TypeVar("T", bound="PatchByOrgByRepoBodyUpstreamType0")


@_attrs_define
class PatchByOrgByRepoBodyUpstreamType0:
    """
    Attributes:
        uri (str): URL of the upstream repository
        autosync (PatchByOrgByRepoBodyUpstreamType0AutosyncType0 | Unset): Optionally enable automatic sync from the
            upstream repository
        token (None | str | Unset): Personal access token for private upstream repos. Set to null to unlink credential.
        token_username (str | Unset): Username for git credential auth. Defaults to "x-access-token". Use actual
            username for Bitbucket app passwords.
    """

    uri: str
    autosync: PatchByOrgByRepoBodyUpstreamType0AutosyncType0 | Unset = UNSET
    token: None | str | Unset = UNSET
    token_username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        autosync: dict[str, Any] | Unset
        if isinstance(self.autosync, Unset):
            autosync = UNSET
        else:
            autosync = self.autosync.to_dict()

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        token_username = self.token_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
            }
        )
        if autosync is not UNSET:
            field_dict["autosync"] = autosync
        if token is not UNSET:
            field_dict["token"] = token
        if token_username is not UNSET:
            field_dict["token_username"] = token_username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_by_org_by_repo_body_upstream_type_0_autosync_type_0 import (
            PatchByOrgByRepoBodyUpstreamType0AutosyncType0,
        )

        d = dict(src_dict)
        uri = d.pop("uri")

        def _parse_autosync(data: object) -> PatchByOrgByRepoBodyUpstreamType0AutosyncType0 | Unset:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            autosync_type_0 = PatchByOrgByRepoBodyUpstreamType0AutosyncType0.from_dict(data)

            return autosync_type_0

        autosync = _parse_autosync(d.pop("autosync", UNSET))

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

        token_username = d.pop("token_username", UNSET)

        patch_by_org_by_repo_body_upstream_type_0 = cls(
            uri=uri,
            autosync=autosync,
            token=token,
            token_username=token_username,
        )

        patch_by_org_by_repo_body_upstream_type_0.additional_properties = d
        return patch_by_org_by_repo_body_upstream_type_0

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

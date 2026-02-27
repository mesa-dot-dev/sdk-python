from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.patch_by_org_by_repo_response_200_upstream_type_0_autosync_type_0 import (
        PatchByOrgByRepoResponse200UpstreamType0AutosyncType0,
    )


T = TypeVar("T", bound="PatchByOrgByRepoResponse200UpstreamType0")


@_attrs_define
class PatchByOrgByRepoResponse200UpstreamType0:
    """
    Attributes:
        uri (str): URL of the upstream repository
        autosync (None | PatchByOrgByRepoResponse200UpstreamType0AutosyncType0): Automatic sync configuration, if
            enabled
        last_sync_attempt (datetime.datetime | None): Timestamp of the last sync attempt
        last_sync_success (datetime.datetime | None): Timestamp of the last successful sync
        last_sync_error (None | str): Error message from the last failed sync attempt
        has_credential (bool): Whether this upstream has an authentication credential configured
        credential_host (None | str): The host the credential is scoped to (e.g. "github.com")
    """

    uri: str
    autosync: None | PatchByOrgByRepoResponse200UpstreamType0AutosyncType0
    last_sync_attempt: datetime.datetime | None
    last_sync_success: datetime.datetime | None
    last_sync_error: None | str
    has_credential: bool
    credential_host: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_by_org_by_repo_response_200_upstream_type_0_autosync_type_0 import (
            PatchByOrgByRepoResponse200UpstreamType0AutosyncType0,
        )

        uri = self.uri

        autosync: dict[str, Any] | None
        if isinstance(self.autosync, PatchByOrgByRepoResponse200UpstreamType0AutosyncType0):
            autosync = self.autosync.to_dict()
        else:
            autosync = self.autosync

        last_sync_attempt: None | str
        if isinstance(self.last_sync_attempt, datetime.datetime):
            last_sync_attempt = self.last_sync_attempt.isoformat()
        else:
            last_sync_attempt = self.last_sync_attempt

        last_sync_success: None | str
        if isinstance(self.last_sync_success, datetime.datetime):
            last_sync_success = self.last_sync_success.isoformat()
        else:
            last_sync_success = self.last_sync_success

        last_sync_error: None | str
        last_sync_error = self.last_sync_error

        has_credential = self.has_credential

        credential_host: None | str
        credential_host = self.credential_host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uri": uri,
                "autosync": autosync,
                "last_sync_attempt": last_sync_attempt,
                "last_sync_success": last_sync_success,
                "last_sync_error": last_sync_error,
                "has_credential": has_credential,
                "credential_host": credential_host,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_by_org_by_repo_response_200_upstream_type_0_autosync_type_0 import (
            PatchByOrgByRepoResponse200UpstreamType0AutosyncType0,
        )

        d = dict(src_dict)
        uri = d.pop("uri")

        def _parse_autosync(data: object) -> None | PatchByOrgByRepoResponse200UpstreamType0AutosyncType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                autosync_type_0 = PatchByOrgByRepoResponse200UpstreamType0AutosyncType0.from_dict(data)

                return autosync_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchByOrgByRepoResponse200UpstreamType0AutosyncType0, data)

        autosync = _parse_autosync(d.pop("autosync"))

        def _parse_last_sync_attempt(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sync_attempt_type_0 = isoparse(data)

                return last_sync_attempt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_sync_attempt = _parse_last_sync_attempt(d.pop("last_sync_attempt"))

        def _parse_last_sync_success(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sync_success_type_0 = isoparse(data)

                return last_sync_success_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_sync_success = _parse_last_sync_success(d.pop("last_sync_success"))

        def _parse_last_sync_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_sync_error = _parse_last_sync_error(d.pop("last_sync_error"))

        has_credential = d.pop("has_credential")

        def _parse_credential_host(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        credential_host = _parse_credential_host(d.pop("credential_host"))

        patch_by_org_by_repo_response_200_upstream_type_0 = cls(
            uri=uri,
            autosync=autosync,
            last_sync_attempt=last_sync_attempt,
            last_sync_success=last_sync_success,
            last_sync_error=last_sync_error,
            has_credential=has_credential,
            credential_host=credential_host,
        )

        patch_by_org_by_repo_response_200_upstream_type_0.additional_properties = d
        return patch_by_org_by_repo_response_200_upstream_type_0

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

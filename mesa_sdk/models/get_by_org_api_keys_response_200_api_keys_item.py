from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetByOrgApiKeysResponse200ApiKeysItem")


@_attrs_define
class GetByOrgApiKeysResponse200ApiKeysItem:
    """
    Attributes:
        id (str):
        name (None | str):
        scopes (list[str]):
        last_used_at (None | str):
        expires_at (None | str):
        revoked_at (None | str):
        created_at (str):
    """

    id: str
    name: None | str
    scopes: list[str]
    last_used_at: None | str
    expires_at: None | str
    revoked_at: None | str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str
        name = self.name

        scopes = self.scopes

        last_used_at: None | str
        last_used_at = self.last_used_at

        expires_at: None | str
        expires_at = self.expires_at

        revoked_at: None | str
        revoked_at = self.revoked_at

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "scopes": scopes,
                "last_used_at": last_used_at,
                "expires_at": expires_at,
                "revoked_at": revoked_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        scopes = cast(list[str], d.pop("scopes"))

        def _parse_last_used_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        def _parse_expires_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        def _parse_revoked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        created_at = d.pop("created_at")

        get_by_org_api_keys_response_200_api_keys_item = cls(
            id=id,
            name=name,
            scopes=scopes,
            last_used_at=last_used_at,
            expires_at=expires_at,
            revoked_at=revoked_at,
            created_at=created_at,
        )

        get_by_org_api_keys_response_200_api_keys_item.additional_properties = d
        return get_by_org_api_keys_response_200_api_keys_item

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

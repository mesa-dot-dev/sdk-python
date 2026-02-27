from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_by_org_api_keys_by_id_response_401_error_details import (
        DeleteByOrgApiKeysByIdResponse401ErrorDetails,
    )


T = TypeVar("T", bound="DeleteByOrgApiKeysByIdResponse401Error")


@_attrs_define
class DeleteByOrgApiKeysByIdResponse401Error:
    """
    Attributes:
        code (str):
        message (str):
        details (DeleteByOrgApiKeysByIdResponse401ErrorDetails | Unset):
    """

    code: str
    message: str
    details: DeleteByOrgApiKeysByIdResponse401ErrorDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_by_org_api_keys_by_id_response_401_error_details import (
            DeleteByOrgApiKeysByIdResponse401ErrorDetails,
        )

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        _details = d.pop("details", UNSET)
        details: DeleteByOrgApiKeysByIdResponse401ErrorDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = DeleteByOrgApiKeysByIdResponse401ErrorDetails.from_dict(_details)

        delete_by_org_api_keys_by_id_response_401_error = cls(
            code=code,
            message=message,
            details=details,
        )

        delete_by_org_api_keys_by_id_response_401_error.additional_properties = d
        return delete_by_org_api_keys_by_id_response_401_error

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_by_org_by_repo_diff_response_200_files_item_status import GetByOrgByRepoDiffResponse200FilesItemStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="GetByOrgByRepoDiffResponse200FilesItem")



@_attrs_define
class GetByOrgByRepoDiffResponse200FilesItem:
    """ 
        Attributes:
            path (str):
            status (GetByOrgByRepoDiffResponse200FilesItemStatus):
            old_path (str | Unset):
            bytes_ (float | Unset):
            is_eof (bool | Unset):
            raw (str | Unset):
     """

    path: str
    status: GetByOrgByRepoDiffResponse200FilesItemStatus
    old_path: str | Unset = UNSET
    bytes_: float | Unset = UNSET
    is_eof: bool | Unset = UNSET
    raw: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        status = self.status.value

        old_path = self.old_path

        bytes_ = self.bytes_

        is_eof = self.is_eof

        raw = self.raw


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "path": path,
            "status": status,
        })
        if old_path is not UNSET:
            field_dict["old_path"] = old_path
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if is_eof is not UNSET:
            field_dict["is_eof"] = is_eof
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        status = GetByOrgByRepoDiffResponse200FilesItemStatus(d.pop("status"))




        old_path = d.pop("old_path", UNSET)

        bytes_ = d.pop("bytes", UNSET)

        is_eof = d.pop("is_eof", UNSET)

        raw = d.pop("raw", UNSET)

        get_by_org_by_repo_diff_response_200_files_item = cls(
            path=path,
            status=status,
            old_path=old_path,
            bytes_=bytes_,
            is_eof=is_eof,
            raw=raw,
        )


        get_by_org_by_repo_diff_response_200_files_item.additional_properties = d
        return get_by_org_by_repo_diff_response_200_files_item

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

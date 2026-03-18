from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PostByOrgApiKeyResponse201")



@_attrs_define
class PostByOrgApiKeyResponse201:
    """ 
        Attributes:
            id (str):
            key (str):
            name (None | str):
            scopes (list[str]):
            repo_ids (list[str] | None):
            created_at (str):
     """

    id: str
    key: str
    name: None | str
    scopes: list[str]
    repo_ids: list[str] | None
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        name: None | str
        name = self.name

        scopes = self.scopes



        repo_ids: list[str] | None
        if isinstance(self.repo_ids, list):
            repo_ids = self.repo_ids


        else:
            repo_ids = self.repo_ids

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "key": key,
            "name": name,
            "scopes": scopes,
            "repo_ids": repo_ids,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        scopes = cast(list[str], d.pop("scopes"))


        def _parse_repo_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repo_ids_type_0 = cast(list[str], data)

                return repo_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        repo_ids = _parse_repo_ids(d.pop("repo_ids"))


        created_at = d.pop("created_at")

        post_by_org_api_key_response_201 = cls(
            id=id,
            key=key,
            name=name,
            scopes=scopes,
            repo_ids=repo_ids,
            created_at=created_at,
        )


        post_by_org_api_key_response_201.additional_properties = d
        return post_by_org_api_key_response_201

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

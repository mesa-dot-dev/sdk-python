from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_by_org_api_key_body_scopes_item import PostByOrgApiKeyBodyScopesItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostByOrgApiKeyBody")



@_attrs_define
class PostByOrgApiKeyBody:
    """ 
        Attributes:
            name (str | Unset):
            scopes (list[PostByOrgApiKeyBodyScopesItem] | Unset):
            repo_ids (list[str] | Unset):
     """

    name: str | Unset = UNSET
    scopes: list[PostByOrgApiKeyBodyScopesItem] | Unset = UNSET
    repo_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.value
                scopes.append(scopes_item)



        repo_ids: list[str] | Unset = UNSET
        if not isinstance(self.repo_ids, Unset):
            repo_ids = self.repo_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if repo_ids is not UNSET:
            field_dict["repo_ids"] = repo_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[PostByOrgApiKeyBodyScopesItem] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = PostByOrgApiKeyBodyScopesItem(scopes_item_data)



                scopes.append(scopes_item)


        repo_ids = cast(list[str], d.pop("repo_ids", UNSET))


        post_by_org_api_key_body = cls(
            name=name,
            scopes=scopes,
            repo_ids=repo_ids,
        )


        post_by_org_api_key_body.additional_properties = d
        return post_by_org_api_key_body

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

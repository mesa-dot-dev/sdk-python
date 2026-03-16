from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_by_org_repo_bulk_tags_body_action import PostByOrgRepoBulkTagsBodyAction
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PostByOrgRepoBulkTagsBody")



@_attrs_define
class PostByOrgRepoBulkTagsBody:
    """ 
        Attributes:
            repo_ids (list[str]):
            action (PostByOrgRepoBulkTagsBodyAction):
            key (str):
            value (str | Unset):
     """

    repo_ids: list[str]
    action: PostByOrgRepoBulkTagsBodyAction
    key: str
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        repo_ids = self.repo_ids



        action = self.action.value

        key = self.key

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "repo_ids": repo_ids,
            "action": action,
            "key": key,
        })
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repo_ids = cast(list[str], d.pop("repo_ids"))


        action = PostByOrgRepoBulkTagsBodyAction(d.pop("action"))




        key = d.pop("key")

        value = d.pop("value", UNSET)

        post_by_org_repo_bulk_tags_body = cls(
            repo_ids=repo_ids,
            action=action,
            key=key,
            value=value,
        )


        post_by_org_repo_bulk_tags_body.additional_properties = d
        return post_by_org_repo_bulk_tags_body

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

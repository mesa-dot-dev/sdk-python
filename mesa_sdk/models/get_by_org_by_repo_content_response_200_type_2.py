from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_by_org_by_repo_content_response_200_type_2_entries_item_type_0 import (
        GetByOrgByRepoContentResponse200Type2EntriesItemType0,
    )
    from ..models.get_by_org_by_repo_content_response_200_type_2_entries_item_type_1 import (
        GetByOrgByRepoContentResponse200Type2EntriesItemType1,
    )
    from ..models.get_by_org_by_repo_content_response_200_type_2_entries_item_type_2 import (
        GetByOrgByRepoContentResponse200Type2EntriesItemType2,
    )


T = TypeVar("T", bound="GetByOrgByRepoContentResponse200Type2")


@_attrs_define
class GetByOrgByRepoContentResponse200Type2:
    """
    Attributes:
        type_ (Literal['dir']):
        name (str):
        path (str):
        sha (str):
        child_count (int):
        entries (list[GetByOrgByRepoContentResponse200Type2EntriesItemType0 |
            GetByOrgByRepoContentResponse200Type2EntriesItemType1 | GetByOrgByRepoContentResponse200Type2EntriesItemType2]):
        next_cursor (None | str):
        has_more (bool):
    """

    type_: Literal["dir"]
    name: str
    path: str
    sha: str
    child_count: int
    entries: list[
        GetByOrgByRepoContentResponse200Type2EntriesItemType0
        | GetByOrgByRepoContentResponse200Type2EntriesItemType1
        | GetByOrgByRepoContentResponse200Type2EntriesItemType2
    ]
    next_cursor: None | str
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_by_org_by_repo_content_response_200_type_2_entries_item_type_0 import (
            GetByOrgByRepoContentResponse200Type2EntriesItemType0,
        )
        from ..models.get_by_org_by_repo_content_response_200_type_2_entries_item_type_1 import (
            GetByOrgByRepoContentResponse200Type2EntriesItemType1,
        )

        type_ = self.type_

        name = self.name

        path = self.path

        sha = self.sha

        child_count = self.child_count

        entries = []
        for entries_item_data in self.entries:
            entries_item: dict[str, Any]
            if isinstance(entries_item_data, GetByOrgByRepoContentResponse200Type2EntriesItemType0):
                entries_item = entries_item_data.to_dict()
            elif isinstance(entries_item_data, GetByOrgByRepoContentResponse200Type2EntriesItemType1):
                entries_item = entries_item_data.to_dict()
            else:
                entries_item = entries_item_data.to_dict()

            entries.append(entries_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "path": path,
                "sha": sha,
                "child_count": child_count,
                "entries": entries,
                "next_cursor": next_cursor,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_by_repo_content_response_200_type_2_entries_item_type_0 import (
            GetByOrgByRepoContentResponse200Type2EntriesItemType0,
        )
        from ..models.get_by_org_by_repo_content_response_200_type_2_entries_item_type_1 import (
            GetByOrgByRepoContentResponse200Type2EntriesItemType1,
        )
        from ..models.get_by_org_by_repo_content_response_200_type_2_entries_item_type_2 import (
            GetByOrgByRepoContentResponse200Type2EntriesItemType2,
        )

        d = dict(src_dict)
        type_ = cast(Literal["dir"], d.pop("type"))
        if type_ != "dir":
            raise ValueError(f"type must match const 'dir', got '{type_}'")

        name = d.pop("name")

        path = d.pop("path")

        sha = d.pop("sha")

        child_count = d.pop("child_count")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:

            def _parse_entries_item(
                data: object,
            ) -> (
                GetByOrgByRepoContentResponse200Type2EntriesItemType0
                | GetByOrgByRepoContentResponse200Type2EntriesItemType1
                | GetByOrgByRepoContentResponse200Type2EntriesItemType2
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_0 = GetByOrgByRepoContentResponse200Type2EntriesItemType0.from_dict(data)

                    return entries_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entries_item_type_1 = GetByOrgByRepoContentResponse200Type2EntriesItemType1.from_dict(data)

                    return entries_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                entries_item_type_2 = GetByOrgByRepoContentResponse200Type2EntriesItemType2.from_dict(data)

                return entries_item_type_2

            entries_item = _parse_entries_item(entries_item_data)

            entries.append(entries_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        has_more = d.pop("has_more")

        get_by_org_by_repo_content_response_200_type_2 = cls(
            type_=type_,
            name=name,
            path=path,
            sha=sha,
            child_count=child_count,
            entries=entries,
            next_cursor=next_cursor,
            has_more=has_more,
        )

        get_by_org_by_repo_content_response_200_type_2.additional_properties = d
        return get_by_org_by_repo_content_response_200_type_2

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

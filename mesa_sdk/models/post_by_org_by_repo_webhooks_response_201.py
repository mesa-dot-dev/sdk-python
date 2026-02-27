from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_by_org_by_repo_webhooks_response_201_events_item import PostByOrgByRepoWebhooksResponse201EventsItem

T = TypeVar("T", bound="PostByOrgByRepoWebhooksResponse201")


@_attrs_define
class PostByOrgByRepoWebhooksResponse201:
    """
    Attributes:
        id (str):
        url (str):
        events (list[PostByOrgByRepoWebhooksResponse201EventsItem]):
        branches (list[str] | None):
        globs (list[str] | None):
        created_at (str):
        updated_at (str):
        secret (str):
    """

    id: str
    url: str
    events: list[PostByOrgByRepoWebhooksResponse201EventsItem]
    branches: list[str] | None
    globs: list[str] | None
    created_at: str
    updated_at: str
    secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        branches: list[str] | None
        if isinstance(self.branches, list):
            branches = self.branches

        else:
            branches = self.branches

        globs: list[str] | None
        if isinstance(self.globs, list):
            globs = self.globs

        else:
            globs = self.globs

        created_at = self.created_at

        updated_at = self.updated_at

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "events": events,
                "branches": branches,
                "globs": globs,
                "created_at": created_at,
                "updated_at": updated_at,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = PostByOrgByRepoWebhooksResponse201EventsItem(events_item_data)

            events.append(events_item)

        def _parse_branches(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                branches_type_0 = cast(list[str], data)

                return branches_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        branches = _parse_branches(d.pop("branches"))

        def _parse_globs(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                globs_type_0 = cast(list[str], data)

                return globs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        globs = _parse_globs(d.pop("globs"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        secret = d.pop("secret")

        post_by_org_by_repo_webhooks_response_201 = cls(
            id=id,
            url=url,
            events=events,
            branches=branches,
            globs=globs,
            created_at=created_at,
            updated_at=updated_at,
            secret=secret,
        )

        post_by_org_by_repo_webhooks_response_201.additional_properties = d
        return post_by_org_by_repo_webhooks_response_201

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

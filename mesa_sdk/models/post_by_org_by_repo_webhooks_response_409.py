from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_by_org_by_repo_webhooks_response_409_error import PostByOrgByRepoWebhooksResponse409Error


T = TypeVar("T", bound="PostByOrgByRepoWebhooksResponse409")


@_attrs_define
class PostByOrgByRepoWebhooksResponse409:
    """
    Attributes:
        error (PostByOrgByRepoWebhooksResponse409Error):
    """

    error: PostByOrgByRepoWebhooksResponse409Error
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_by_org_by_repo_webhooks_response_409_error import PostByOrgByRepoWebhooksResponse409Error

        d = dict(src_dict)
        error = PostByOrgByRepoWebhooksResponse409Error.from_dict(d.pop("error"))

        post_by_org_by_repo_webhooks_response_409 = cls(
            error=error,
        )

        post_by_org_by_repo_webhooks_response_409.additional_properties = d
        return post_by_org_by_repo_webhooks_response_409

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

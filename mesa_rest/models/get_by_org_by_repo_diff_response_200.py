from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_by_org_by_repo_diff_response_200_files_item import GetByOrgByRepoDiffResponse200FilesItem
  from ..models.get_by_org_by_repo_diff_response_200_filtered_files_item import GetByOrgByRepoDiffResponse200FilteredFilesItem
  from ..models.get_by_org_by_repo_diff_response_200_stats import GetByOrgByRepoDiffResponse200Stats





T = TypeVar("T", bound="GetByOrgByRepoDiffResponse200")



@_attrs_define
class GetByOrgByRepoDiffResponse200:
    """ 
        Attributes:
            base (str):
            head (str):
            truncated (bool):
            stats (GetByOrgByRepoDiffResponse200Stats):
            files (list[GetByOrgByRepoDiffResponse200FilesItem]):
            filtered_files (list[GetByOrgByRepoDiffResponse200FilteredFilesItem]):
     """

    base: str
    head: str
    truncated: bool
    stats: GetByOrgByRepoDiffResponse200Stats
    files: list[GetByOrgByRepoDiffResponse200FilesItem]
    filtered_files: list[GetByOrgByRepoDiffResponse200FilteredFilesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_by_org_by_repo_diff_response_200_files_item import GetByOrgByRepoDiffResponse200FilesItem
        from ..models.get_by_org_by_repo_diff_response_200_filtered_files_item import GetByOrgByRepoDiffResponse200FilteredFilesItem
        from ..models.get_by_org_by_repo_diff_response_200_stats import GetByOrgByRepoDiffResponse200Stats
        base = self.base

        head = self.head

        truncated = self.truncated

        stats = self.stats.to_dict()

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)



        filtered_files = []
        for filtered_files_item_data in self.filtered_files:
            filtered_files_item = filtered_files_item_data.to_dict()
            filtered_files.append(filtered_files_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "base": base,
            "head": head,
            "truncated": truncated,
            "stats": stats,
            "files": files,
            "filtered_files": filtered_files,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_org_by_repo_diff_response_200_files_item import GetByOrgByRepoDiffResponse200FilesItem
        from ..models.get_by_org_by_repo_diff_response_200_filtered_files_item import GetByOrgByRepoDiffResponse200FilteredFilesItem
        from ..models.get_by_org_by_repo_diff_response_200_stats import GetByOrgByRepoDiffResponse200Stats
        d = dict(src_dict)
        base = d.pop("base")

        head = d.pop("head")

        truncated = d.pop("truncated")

        stats = GetByOrgByRepoDiffResponse200Stats.from_dict(d.pop("stats"))




        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            files_item = GetByOrgByRepoDiffResponse200FilesItem.from_dict(files_item_data)



            files.append(files_item)


        filtered_files = []
        _filtered_files = d.pop("filtered_files")
        for filtered_files_item_data in (_filtered_files):
            filtered_files_item = GetByOrgByRepoDiffResponse200FilteredFilesItem.from_dict(filtered_files_item_data)



            filtered_files.append(filtered_files_item)


        get_by_org_by_repo_diff_response_200 = cls(
            base=base,
            head=head,
            truncated=truncated,
            stats=stats,
            files=files,
            filtered_files=filtered_files,
        )


        get_by_org_by_repo_diff_response_200.additional_properties = d
        return get_by_org_by_repo_diff_response_200

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

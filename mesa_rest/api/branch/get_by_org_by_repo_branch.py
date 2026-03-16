from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_by_org_by_repo_branch_response_200 import GetByOrgByRepoBranchResponse200
from ...models.get_by_org_by_repo_branch_response_400 import GetByOrgByRepoBranchResponse400
from ...models.get_by_org_by_repo_branch_response_401 import GetByOrgByRepoBranchResponse401
from ...models.get_by_org_by_repo_branch_response_403 import GetByOrgByRepoBranchResponse403
from ...models.get_by_org_by_repo_branch_response_404 import GetByOrgByRepoBranchResponse404
from ...models.get_by_org_by_repo_branch_response_406 import GetByOrgByRepoBranchResponse406
from ...models.get_by_org_by_repo_branch_response_409 import GetByOrgByRepoBranchResponse409
from ...models.get_by_org_by_repo_branch_response_500 import GetByOrgByRepoBranchResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    org: str,
    repo: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/{repo}/branch".format(org=quote(str(org), safe=""),repo=quote(str(repo), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500 | None:
    if response.status_code == 200:
        response_200 = GetByOrgByRepoBranchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgByRepoBranchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgByRepoBranchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgByRepoBranchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgByRepoBranchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgByRepoBranchResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgByRepoBranchResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgByRepoBranchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500]:
    """ List branches

     List all branches in a repository

    Args:
        org (str):
        repo (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
cursor=cursor,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500 | None:
    """ List branches

     List all branches in a repository

    Args:
        org (str):
        repo (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500
     """


    return sync_detailed(
        org=org,
repo=repo,
client=client,
cursor=cursor,
limit=limit,

    ).parsed

async def asyncio_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> Response[GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500]:
    """ List branches

     List all branches in a repository

    Args:
        org (str):
        repo (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
cursor=cursor,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,

) -> GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500 | None:
    """ List branches

     List all branches in a repository

    Args:
        org (str):
        repo (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoBranchResponse200 | GetByOrgByRepoBranchResponse400 | GetByOrgByRepoBranchResponse401 | GetByOrgByRepoBranchResponse403 | GetByOrgByRepoBranchResponse404 | GetByOrgByRepoBranchResponse406 | GetByOrgByRepoBranchResponse409 | GetByOrgByRepoBranchResponse500
     """


    return (await asyncio_detailed(
        org=org,
repo=repo,
client=client,
cursor=cursor,
limit=limit,

    )).parsed

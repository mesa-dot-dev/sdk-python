from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_by_org_repo_response_200 import GetByOrgRepoResponse200
from ...models.get_by_org_repo_response_400 import GetByOrgRepoResponse400
from ...models.get_by_org_repo_response_401 import GetByOrgRepoResponse401
from ...models.get_by_org_repo_response_403 import GetByOrgRepoResponse403
from ...models.get_by_org_repo_response_404 import GetByOrgRepoResponse404
from ...models.get_by_org_repo_response_406 import GetByOrgRepoResponse406
from ...models.get_by_org_repo_response_409 import GetByOrgRepoResponse409
from ...models.get_by_org_repo_response_500 import GetByOrgRepoResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    org: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    tags: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["tags"] = tags


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/repo".format(org=quote(str(org), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500 | None:
    if response.status_code == 200:
        response_200 = GetByOrgRepoResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgRepoResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgRepoResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgRepoResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgRepoResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgRepoResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgRepoResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgRepoResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    tags: str | Unset = UNSET,

) -> Response[GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500]:
    """ List repositories

     List repositories in the organization using cursor pagination

    Args:
        org (str):
        cursor (str | Unset):
        limit (int | Unset):
        tags (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
cursor=cursor,
limit=limit,
tags=tags,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    tags: str | Unset = UNSET,

) -> GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500 | None:
    """ List repositories

     List repositories in the organization using cursor pagination

    Args:
        org (str):
        cursor (str | Unset):
        limit (int | Unset):
        tags (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500
     """


    return sync_detailed(
        org=org,
client=client,
cursor=cursor,
limit=limit,
tags=tags,

    ).parsed

async def asyncio_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    tags: str | Unset = UNSET,

) -> Response[GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500]:
    """ List repositories

     List repositories in the organization using cursor pagination

    Args:
        org (str):
        cursor (str | Unset):
        limit (int | Unset):
        tags (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
cursor=cursor,
limit=limit,
tags=tags,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    tags: str | Unset = UNSET,

) -> GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500 | None:
    """ List repositories

     List repositories in the organization using cursor pagination

    Args:
        org (str):
        cursor (str | Unset):
        limit (int | Unset):
        tags (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgRepoResponse200 | GetByOrgRepoResponse400 | GetByOrgRepoResponse401 | GetByOrgRepoResponse403 | GetByOrgRepoResponse404 | GetByOrgRepoResponse406 | GetByOrgRepoResponse409 | GetByOrgRepoResponse500
     """


    return (await asyncio_detailed(
        org=org,
client=client,
cursor=cursor,
limit=limit,
tags=tags,

    )).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_org_repos_response_200 import GetByOrgReposResponse200
from ...models.get_by_org_repos_response_400 import GetByOrgReposResponse400
from ...models.get_by_org_repos_response_401 import GetByOrgReposResponse401
from ...models.get_by_org_repos_response_403 import GetByOrgReposResponse403
from ...models.get_by_org_repos_response_404 import GetByOrgReposResponse404
from ...models.get_by_org_repos_response_406 import GetByOrgReposResponse406
from ...models.get_by_org_repos_response_409 import GetByOrgReposResponse409
from ...models.get_by_org_repos_response_500 import GetByOrgReposResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org: str,
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
        "url": "/{org}/repos".format(
            org=quote(str(org), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetByOrgReposResponse200
    | GetByOrgReposResponse400
    | GetByOrgReposResponse401
    | GetByOrgReposResponse403
    | GetByOrgReposResponse404
    | GetByOrgReposResponse406
    | GetByOrgReposResponse409
    | GetByOrgReposResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetByOrgReposResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgReposResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgReposResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgReposResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgReposResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgReposResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgReposResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgReposResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetByOrgReposResponse200
    | GetByOrgReposResponse400
    | GetByOrgReposResponse401
    | GetByOrgReposResponse403
    | GetByOrgReposResponse404
    | GetByOrgReposResponse406
    | GetByOrgReposResponse409
    | GetByOrgReposResponse500
]:
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
) -> Response[
    GetByOrgReposResponse200
    | GetByOrgReposResponse400
    | GetByOrgReposResponse401
    | GetByOrgReposResponse403
    | GetByOrgReposResponse404
    | GetByOrgReposResponse406
    | GetByOrgReposResponse409
    | GetByOrgReposResponse500
]:
    """List repositories

     List all repositories in the organization

    Args:
        org (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgReposResponse200 | GetByOrgReposResponse400 | GetByOrgReposResponse401 | GetByOrgReposResponse403 | GetByOrgReposResponse404 | GetByOrgReposResponse406 | GetByOrgReposResponse409 | GetByOrgReposResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        cursor=cursor,
        limit=limit,
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
) -> (
    GetByOrgReposResponse200
    | GetByOrgReposResponse400
    | GetByOrgReposResponse401
    | GetByOrgReposResponse403
    | GetByOrgReposResponse404
    | GetByOrgReposResponse406
    | GetByOrgReposResponse409
    | GetByOrgReposResponse500
    | None
):
    """List repositories

     List all repositories in the organization

    Args:
        org (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgReposResponse200 | GetByOrgReposResponse400 | GetByOrgReposResponse401 | GetByOrgReposResponse403 | GetByOrgReposResponse404 | GetByOrgReposResponse406 | GetByOrgReposResponse409 | GetByOrgReposResponse500
    """

    return sync_detailed(
        org=org,
        client=client,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[
    GetByOrgReposResponse200
    | GetByOrgReposResponse400
    | GetByOrgReposResponse401
    | GetByOrgReposResponse403
    | GetByOrgReposResponse404
    | GetByOrgReposResponse406
    | GetByOrgReposResponse409
    | GetByOrgReposResponse500
]:
    """List repositories

     List all repositories in the organization

    Args:
        org (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgReposResponse200 | GetByOrgReposResponse400 | GetByOrgReposResponse401 | GetByOrgReposResponse403 | GetByOrgReposResponse404 | GetByOrgReposResponse406 | GetByOrgReposResponse409 | GetByOrgReposResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> (
    GetByOrgReposResponse200
    | GetByOrgReposResponse400
    | GetByOrgReposResponse401
    | GetByOrgReposResponse403
    | GetByOrgReposResponse404
    | GetByOrgReposResponse406
    | GetByOrgReposResponse409
    | GetByOrgReposResponse500
    | None
):
    """List repositories

     List all repositories in the organization

    Args:
        org (str):
        cursor (str | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgReposResponse200 | GetByOrgReposResponse400 | GetByOrgReposResponse401 | GetByOrgReposResponse403 | GetByOrgReposResponse404 | GetByOrgReposResponse406 | GetByOrgReposResponse409 | GetByOrgReposResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
            cursor=cursor,
            limit=limit,
        )
    ).parsed

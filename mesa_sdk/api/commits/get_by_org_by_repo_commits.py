from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_org_by_repo_commits_response_200 import GetByOrgByRepoCommitsResponse200
from ...models.get_by_org_by_repo_commits_response_400 import GetByOrgByRepoCommitsResponse400
from ...models.get_by_org_by_repo_commits_response_401 import GetByOrgByRepoCommitsResponse401
from ...models.get_by_org_by_repo_commits_response_403 import GetByOrgByRepoCommitsResponse403
from ...models.get_by_org_by_repo_commits_response_404 import GetByOrgByRepoCommitsResponse404
from ...models.get_by_org_by_repo_commits_response_406 import GetByOrgByRepoCommitsResponse406
from ...models.get_by_org_by_repo_commits_response_409 import GetByOrgByRepoCommitsResponse409
from ...models.get_by_org_by_repo_commits_response_500 import GetByOrgByRepoCommitsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org: str,
    repo: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ref: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["ref"] = ref

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/{repo}/commits".format(
            org=quote(str(org), safe=""),
            repo=quote(str(repo), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetByOrgByRepoCommitsResponse200
    | GetByOrgByRepoCommitsResponse400
    | GetByOrgByRepoCommitsResponse401
    | GetByOrgByRepoCommitsResponse403
    | GetByOrgByRepoCommitsResponse404
    | GetByOrgByRepoCommitsResponse406
    | GetByOrgByRepoCommitsResponse409
    | GetByOrgByRepoCommitsResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetByOrgByRepoCommitsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgByRepoCommitsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgByRepoCommitsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgByRepoCommitsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgByRepoCommitsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgByRepoCommitsResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgByRepoCommitsResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgByRepoCommitsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetByOrgByRepoCommitsResponse200
    | GetByOrgByRepoCommitsResponse400
    | GetByOrgByRepoCommitsResponse401
    | GetByOrgByRepoCommitsResponse403
    | GetByOrgByRepoCommitsResponse404
    | GetByOrgByRepoCommitsResponse406
    | GetByOrgByRepoCommitsResponse409
    | GetByOrgByRepoCommitsResponse500
]:
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
    ref: str | Unset = UNSET,
) -> Response[
    GetByOrgByRepoCommitsResponse200
    | GetByOrgByRepoCommitsResponse400
    | GetByOrgByRepoCommitsResponse401
    | GetByOrgByRepoCommitsResponse403
    | GetByOrgByRepoCommitsResponse404
    | GetByOrgByRepoCommitsResponse406
    | GetByOrgByRepoCommitsResponse409
    | GetByOrgByRepoCommitsResponse500
]:
    """List commits

     List commits for a repository from a specific ref

    Args:
        org (str):
        repo (str):
        cursor (str | Unset):
        limit (int | Unset):
        ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoCommitsResponse200 | GetByOrgByRepoCommitsResponse400 | GetByOrgByRepoCommitsResponse401 | GetByOrgByRepoCommitsResponse403 | GetByOrgByRepoCommitsResponse404 | GetByOrgByRepoCommitsResponse406 | GetByOrgByRepoCommitsResponse409 | GetByOrgByRepoCommitsResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        cursor=cursor,
        limit=limit,
        ref=ref,
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
    ref: str | Unset = UNSET,
) -> (
    GetByOrgByRepoCommitsResponse200
    | GetByOrgByRepoCommitsResponse400
    | GetByOrgByRepoCommitsResponse401
    | GetByOrgByRepoCommitsResponse403
    | GetByOrgByRepoCommitsResponse404
    | GetByOrgByRepoCommitsResponse406
    | GetByOrgByRepoCommitsResponse409
    | GetByOrgByRepoCommitsResponse500
    | None
):
    """List commits

     List commits for a repository from a specific ref

    Args:
        org (str):
        repo (str):
        cursor (str | Unset):
        limit (int | Unset):
        ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoCommitsResponse200 | GetByOrgByRepoCommitsResponse400 | GetByOrgByRepoCommitsResponse401 | GetByOrgByRepoCommitsResponse403 | GetByOrgByRepoCommitsResponse404 | GetByOrgByRepoCommitsResponse406 | GetByOrgByRepoCommitsResponse409 | GetByOrgByRepoCommitsResponse500
    """

    return sync_detailed(
        org=org,
        repo=repo,
        client=client,
        cursor=cursor,
        limit=limit,
        ref=ref,
    ).parsed


async def asyncio_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ref: str | Unset = UNSET,
) -> Response[
    GetByOrgByRepoCommitsResponse200
    | GetByOrgByRepoCommitsResponse400
    | GetByOrgByRepoCommitsResponse401
    | GetByOrgByRepoCommitsResponse403
    | GetByOrgByRepoCommitsResponse404
    | GetByOrgByRepoCommitsResponse406
    | GetByOrgByRepoCommitsResponse409
    | GetByOrgByRepoCommitsResponse500
]:
    """List commits

     List commits for a repository from a specific ref

    Args:
        org (str):
        repo (str):
        cursor (str | Unset):
        limit (int | Unset):
        ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoCommitsResponse200 | GetByOrgByRepoCommitsResponse400 | GetByOrgByRepoCommitsResponse401 | GetByOrgByRepoCommitsResponse403 | GetByOrgByRepoCommitsResponse404 | GetByOrgByRepoCommitsResponse406 | GetByOrgByRepoCommitsResponse409 | GetByOrgByRepoCommitsResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        cursor=cursor,
        limit=limit,
        ref=ref,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ref: str | Unset = UNSET,
) -> (
    GetByOrgByRepoCommitsResponse200
    | GetByOrgByRepoCommitsResponse400
    | GetByOrgByRepoCommitsResponse401
    | GetByOrgByRepoCommitsResponse403
    | GetByOrgByRepoCommitsResponse404
    | GetByOrgByRepoCommitsResponse406
    | GetByOrgByRepoCommitsResponse409
    | GetByOrgByRepoCommitsResponse500
    | None
):
    """List commits

     List commits for a repository from a specific ref

    Args:
        org (str):
        repo (str):
        cursor (str | Unset):
        limit (int | Unset):
        ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoCommitsResponse200 | GetByOrgByRepoCommitsResponse400 | GetByOrgByRepoCommitsResponse401 | GetByOrgByRepoCommitsResponse403 | GetByOrgByRepoCommitsResponse404 | GetByOrgByRepoCommitsResponse406 | GetByOrgByRepoCommitsResponse409 | GetByOrgByRepoCommitsResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            client=client,
            cursor=cursor,
            limit=limit,
            ref=ref,
        )
    ).parsed

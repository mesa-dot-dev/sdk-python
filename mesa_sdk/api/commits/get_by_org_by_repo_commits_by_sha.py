from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_org_by_repo_commits_by_sha_response_200 import GetByOrgByRepoCommitsByShaResponse200
from ...models.get_by_org_by_repo_commits_by_sha_response_400 import GetByOrgByRepoCommitsByShaResponse400
from ...models.get_by_org_by_repo_commits_by_sha_response_401 import GetByOrgByRepoCommitsByShaResponse401
from ...models.get_by_org_by_repo_commits_by_sha_response_403 import GetByOrgByRepoCommitsByShaResponse403
from ...models.get_by_org_by_repo_commits_by_sha_response_404 import GetByOrgByRepoCommitsByShaResponse404
from ...models.get_by_org_by_repo_commits_by_sha_response_406 import GetByOrgByRepoCommitsByShaResponse406
from ...models.get_by_org_by_repo_commits_by_sha_response_409 import GetByOrgByRepoCommitsByShaResponse409
from ...models.get_by_org_by_repo_commits_by_sha_response_500 import GetByOrgByRepoCommitsByShaResponse500
from ...types import Response


def _get_kwargs(
    org: str,
    repo: str,
    sha: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/{repo}/commits/{sha}".format(
            org=quote(str(org), safe=""),
            repo=quote(str(repo), safe=""),
            sha=quote(str(sha), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetByOrgByRepoCommitsByShaResponse200
    | GetByOrgByRepoCommitsByShaResponse400
    | GetByOrgByRepoCommitsByShaResponse401
    | GetByOrgByRepoCommitsByShaResponse403
    | GetByOrgByRepoCommitsByShaResponse404
    | GetByOrgByRepoCommitsByShaResponse406
    | GetByOrgByRepoCommitsByShaResponse409
    | GetByOrgByRepoCommitsByShaResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetByOrgByRepoCommitsByShaResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgByRepoCommitsByShaResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgByRepoCommitsByShaResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgByRepoCommitsByShaResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgByRepoCommitsByShaResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgByRepoCommitsByShaResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgByRepoCommitsByShaResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgByRepoCommitsByShaResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetByOrgByRepoCommitsByShaResponse200
    | GetByOrgByRepoCommitsByShaResponse400
    | GetByOrgByRepoCommitsByShaResponse401
    | GetByOrgByRepoCommitsByShaResponse403
    | GetByOrgByRepoCommitsByShaResponse404
    | GetByOrgByRepoCommitsByShaResponse406
    | GetByOrgByRepoCommitsByShaResponse409
    | GetByOrgByRepoCommitsByShaResponse500
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
    sha: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetByOrgByRepoCommitsByShaResponse200
    | GetByOrgByRepoCommitsByShaResponse400
    | GetByOrgByRepoCommitsByShaResponse401
    | GetByOrgByRepoCommitsByShaResponse403
    | GetByOrgByRepoCommitsByShaResponse404
    | GetByOrgByRepoCommitsByShaResponse406
    | GetByOrgByRepoCommitsByShaResponse409
    | GetByOrgByRepoCommitsByShaResponse500
]:
    """Get commit

     Retrieve a specific commit by its SHA

    Args:
        org (str):
        repo (str):
        sha (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoCommitsByShaResponse200 | GetByOrgByRepoCommitsByShaResponse400 | GetByOrgByRepoCommitsByShaResponse401 | GetByOrgByRepoCommitsByShaResponse403 | GetByOrgByRepoCommitsByShaResponse404 | GetByOrgByRepoCommitsByShaResponse406 | GetByOrgByRepoCommitsByShaResponse409 | GetByOrgByRepoCommitsByShaResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        sha=sha,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org: str,
    repo: str,
    sha: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetByOrgByRepoCommitsByShaResponse200
    | GetByOrgByRepoCommitsByShaResponse400
    | GetByOrgByRepoCommitsByShaResponse401
    | GetByOrgByRepoCommitsByShaResponse403
    | GetByOrgByRepoCommitsByShaResponse404
    | GetByOrgByRepoCommitsByShaResponse406
    | GetByOrgByRepoCommitsByShaResponse409
    | GetByOrgByRepoCommitsByShaResponse500
    | None
):
    """Get commit

     Retrieve a specific commit by its SHA

    Args:
        org (str):
        repo (str):
        sha (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoCommitsByShaResponse200 | GetByOrgByRepoCommitsByShaResponse400 | GetByOrgByRepoCommitsByShaResponse401 | GetByOrgByRepoCommitsByShaResponse403 | GetByOrgByRepoCommitsByShaResponse404 | GetByOrgByRepoCommitsByShaResponse406 | GetByOrgByRepoCommitsByShaResponse409 | GetByOrgByRepoCommitsByShaResponse500
    """

    return sync_detailed(
        org=org,
        repo=repo,
        sha=sha,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    repo: str,
    sha: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetByOrgByRepoCommitsByShaResponse200
    | GetByOrgByRepoCommitsByShaResponse400
    | GetByOrgByRepoCommitsByShaResponse401
    | GetByOrgByRepoCommitsByShaResponse403
    | GetByOrgByRepoCommitsByShaResponse404
    | GetByOrgByRepoCommitsByShaResponse406
    | GetByOrgByRepoCommitsByShaResponse409
    | GetByOrgByRepoCommitsByShaResponse500
]:
    """Get commit

     Retrieve a specific commit by its SHA

    Args:
        org (str):
        repo (str):
        sha (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoCommitsByShaResponse200 | GetByOrgByRepoCommitsByShaResponse400 | GetByOrgByRepoCommitsByShaResponse401 | GetByOrgByRepoCommitsByShaResponse403 | GetByOrgByRepoCommitsByShaResponse404 | GetByOrgByRepoCommitsByShaResponse406 | GetByOrgByRepoCommitsByShaResponse409 | GetByOrgByRepoCommitsByShaResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        sha=sha,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    repo: str,
    sha: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetByOrgByRepoCommitsByShaResponse200
    | GetByOrgByRepoCommitsByShaResponse400
    | GetByOrgByRepoCommitsByShaResponse401
    | GetByOrgByRepoCommitsByShaResponse403
    | GetByOrgByRepoCommitsByShaResponse404
    | GetByOrgByRepoCommitsByShaResponse406
    | GetByOrgByRepoCommitsByShaResponse409
    | GetByOrgByRepoCommitsByShaResponse500
    | None
):
    """Get commit

     Retrieve a specific commit by its SHA

    Args:
        org (str):
        repo (str):
        sha (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoCommitsByShaResponse200 | GetByOrgByRepoCommitsByShaResponse400 | GetByOrgByRepoCommitsByShaResponse401 | GetByOrgByRepoCommitsByShaResponse403 | GetByOrgByRepoCommitsByShaResponse404 | GetByOrgByRepoCommitsByShaResponse406 | GetByOrgByRepoCommitsByShaResponse409 | GetByOrgByRepoCommitsByShaResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            sha=sha,
            client=client,
        )
    ).parsed

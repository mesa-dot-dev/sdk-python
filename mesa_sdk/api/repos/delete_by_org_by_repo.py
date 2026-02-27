from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_by_org_by_repo_response_200 import DeleteByOrgByRepoResponse200
from ...models.delete_by_org_by_repo_response_400 import DeleteByOrgByRepoResponse400
from ...models.delete_by_org_by_repo_response_401 import DeleteByOrgByRepoResponse401
from ...models.delete_by_org_by_repo_response_403 import DeleteByOrgByRepoResponse403
from ...models.delete_by_org_by_repo_response_404 import DeleteByOrgByRepoResponse404
from ...models.delete_by_org_by_repo_response_406 import DeleteByOrgByRepoResponse406
from ...models.delete_by_org_by_repo_response_409 import DeleteByOrgByRepoResponse409
from ...models.delete_by_org_by_repo_response_500 import DeleteByOrgByRepoResponse500
from ...types import Response


def _get_kwargs(
    org: str,
    repo: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{org}/{repo}".format(
            org=quote(str(org), safe=""),
            repo=quote(str(repo), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteByOrgByRepoResponse200
    | DeleteByOrgByRepoResponse400
    | DeleteByOrgByRepoResponse401
    | DeleteByOrgByRepoResponse403
    | DeleteByOrgByRepoResponse404
    | DeleteByOrgByRepoResponse406
    | DeleteByOrgByRepoResponse409
    | DeleteByOrgByRepoResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DeleteByOrgByRepoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteByOrgByRepoResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteByOrgByRepoResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteByOrgByRepoResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteByOrgByRepoResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = DeleteByOrgByRepoResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteByOrgByRepoResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = DeleteByOrgByRepoResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteByOrgByRepoResponse200
    | DeleteByOrgByRepoResponse400
    | DeleteByOrgByRepoResponse401
    | DeleteByOrgByRepoResponse403
    | DeleteByOrgByRepoResponse404
    | DeleteByOrgByRepoResponse406
    | DeleteByOrgByRepoResponse409
    | DeleteByOrgByRepoResponse500
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
) -> Response[
    DeleteByOrgByRepoResponse200
    | DeleteByOrgByRepoResponse400
    | DeleteByOrgByRepoResponse401
    | DeleteByOrgByRepoResponse403
    | DeleteByOrgByRepoResponse404
    | DeleteByOrgByRepoResponse406
    | DeleteByOrgByRepoResponse409
    | DeleteByOrgByRepoResponse500
]:
    """Delete repository

     Permanently delete a repository and all its data

    Args:
        org (str):
        repo (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoResponse200 | DeleteByOrgByRepoResponse400 | DeleteByOrgByRepoResponse401 | DeleteByOrgByRepoResponse403 | DeleteByOrgByRepoResponse404 | DeleteByOrgByRepoResponse406 | DeleteByOrgByRepoResponse409 | DeleteByOrgByRepoResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
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
) -> (
    DeleteByOrgByRepoResponse200
    | DeleteByOrgByRepoResponse400
    | DeleteByOrgByRepoResponse401
    | DeleteByOrgByRepoResponse403
    | DeleteByOrgByRepoResponse404
    | DeleteByOrgByRepoResponse406
    | DeleteByOrgByRepoResponse409
    | DeleteByOrgByRepoResponse500
    | None
):
    """Delete repository

     Permanently delete a repository and all its data

    Args:
        org (str):
        repo (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoResponse200 | DeleteByOrgByRepoResponse400 | DeleteByOrgByRepoResponse401 | DeleteByOrgByRepoResponse403 | DeleteByOrgByRepoResponse404 | DeleteByOrgByRepoResponse406 | DeleteByOrgByRepoResponse409 | DeleteByOrgByRepoResponse500
    """

    return sync_detailed(
        org=org,
        repo=repo,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteByOrgByRepoResponse200
    | DeleteByOrgByRepoResponse400
    | DeleteByOrgByRepoResponse401
    | DeleteByOrgByRepoResponse403
    | DeleteByOrgByRepoResponse404
    | DeleteByOrgByRepoResponse406
    | DeleteByOrgByRepoResponse409
    | DeleteByOrgByRepoResponse500
]:
    """Delete repository

     Permanently delete a repository and all its data

    Args:
        org (str):
        repo (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoResponse200 | DeleteByOrgByRepoResponse400 | DeleteByOrgByRepoResponse401 | DeleteByOrgByRepoResponse403 | DeleteByOrgByRepoResponse404 | DeleteByOrgByRepoResponse406 | DeleteByOrgByRepoResponse409 | DeleteByOrgByRepoResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteByOrgByRepoResponse200
    | DeleteByOrgByRepoResponse400
    | DeleteByOrgByRepoResponse401
    | DeleteByOrgByRepoResponse403
    | DeleteByOrgByRepoResponse404
    | DeleteByOrgByRepoResponse406
    | DeleteByOrgByRepoResponse409
    | DeleteByOrgByRepoResponse500
    | None
):
    """Delete repository

     Permanently delete a repository and all its data

    Args:
        org (str):
        repo (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoResponse200 | DeleteByOrgByRepoResponse400 | DeleteByOrgByRepoResponse401 | DeleteByOrgByRepoResponse403 | DeleteByOrgByRepoResponse404 | DeleteByOrgByRepoResponse406 | DeleteByOrgByRepoResponse409 | DeleteByOrgByRepoResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            client=client,
        )
    ).parsed

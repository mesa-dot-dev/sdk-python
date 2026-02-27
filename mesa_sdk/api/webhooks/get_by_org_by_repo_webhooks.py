from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_org_by_repo_webhooks_response_200 import GetByOrgByRepoWebhooksResponse200
from ...models.get_by_org_by_repo_webhooks_response_400 import GetByOrgByRepoWebhooksResponse400
from ...models.get_by_org_by_repo_webhooks_response_401 import GetByOrgByRepoWebhooksResponse401
from ...models.get_by_org_by_repo_webhooks_response_403 import GetByOrgByRepoWebhooksResponse403
from ...models.get_by_org_by_repo_webhooks_response_404 import GetByOrgByRepoWebhooksResponse404
from ...models.get_by_org_by_repo_webhooks_response_406 import GetByOrgByRepoWebhooksResponse406
from ...models.get_by_org_by_repo_webhooks_response_409 import GetByOrgByRepoWebhooksResponse409
from ...models.get_by_org_by_repo_webhooks_response_500 import GetByOrgByRepoWebhooksResponse500
from ...types import Response


def _get_kwargs(
    org: str,
    repo: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/{repo}/webhooks".format(
            org=quote(str(org), safe=""),
            repo=quote(str(repo), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetByOrgByRepoWebhooksResponse200
    | GetByOrgByRepoWebhooksResponse400
    | GetByOrgByRepoWebhooksResponse401
    | GetByOrgByRepoWebhooksResponse403
    | GetByOrgByRepoWebhooksResponse404
    | GetByOrgByRepoWebhooksResponse406
    | GetByOrgByRepoWebhooksResponse409
    | GetByOrgByRepoWebhooksResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetByOrgByRepoWebhooksResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgByRepoWebhooksResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgByRepoWebhooksResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgByRepoWebhooksResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgByRepoWebhooksResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgByRepoWebhooksResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgByRepoWebhooksResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgByRepoWebhooksResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetByOrgByRepoWebhooksResponse200
    | GetByOrgByRepoWebhooksResponse400
    | GetByOrgByRepoWebhooksResponse401
    | GetByOrgByRepoWebhooksResponse403
    | GetByOrgByRepoWebhooksResponse404
    | GetByOrgByRepoWebhooksResponse406
    | GetByOrgByRepoWebhooksResponse409
    | GetByOrgByRepoWebhooksResponse500
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
    GetByOrgByRepoWebhooksResponse200
    | GetByOrgByRepoWebhooksResponse400
    | GetByOrgByRepoWebhooksResponse401
    | GetByOrgByRepoWebhooksResponse403
    | GetByOrgByRepoWebhooksResponse404
    | GetByOrgByRepoWebhooksResponse406
    | GetByOrgByRepoWebhooksResponse409
    | GetByOrgByRepoWebhooksResponse500
]:
    """List webhooks

     List webhooks for a repository

    Args:
        org (str):
        repo (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoWebhooksResponse200 | GetByOrgByRepoWebhooksResponse400 | GetByOrgByRepoWebhooksResponse401 | GetByOrgByRepoWebhooksResponse403 | GetByOrgByRepoWebhooksResponse404 | GetByOrgByRepoWebhooksResponse406 | GetByOrgByRepoWebhooksResponse409 | GetByOrgByRepoWebhooksResponse500]
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
    GetByOrgByRepoWebhooksResponse200
    | GetByOrgByRepoWebhooksResponse400
    | GetByOrgByRepoWebhooksResponse401
    | GetByOrgByRepoWebhooksResponse403
    | GetByOrgByRepoWebhooksResponse404
    | GetByOrgByRepoWebhooksResponse406
    | GetByOrgByRepoWebhooksResponse409
    | GetByOrgByRepoWebhooksResponse500
    | None
):
    """List webhooks

     List webhooks for a repository

    Args:
        org (str):
        repo (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoWebhooksResponse200 | GetByOrgByRepoWebhooksResponse400 | GetByOrgByRepoWebhooksResponse401 | GetByOrgByRepoWebhooksResponse403 | GetByOrgByRepoWebhooksResponse404 | GetByOrgByRepoWebhooksResponse406 | GetByOrgByRepoWebhooksResponse409 | GetByOrgByRepoWebhooksResponse500
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
    GetByOrgByRepoWebhooksResponse200
    | GetByOrgByRepoWebhooksResponse400
    | GetByOrgByRepoWebhooksResponse401
    | GetByOrgByRepoWebhooksResponse403
    | GetByOrgByRepoWebhooksResponse404
    | GetByOrgByRepoWebhooksResponse406
    | GetByOrgByRepoWebhooksResponse409
    | GetByOrgByRepoWebhooksResponse500
]:
    """List webhooks

     List webhooks for a repository

    Args:
        org (str):
        repo (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoWebhooksResponse200 | GetByOrgByRepoWebhooksResponse400 | GetByOrgByRepoWebhooksResponse401 | GetByOrgByRepoWebhooksResponse403 | GetByOrgByRepoWebhooksResponse404 | GetByOrgByRepoWebhooksResponse406 | GetByOrgByRepoWebhooksResponse409 | GetByOrgByRepoWebhooksResponse500]
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
    GetByOrgByRepoWebhooksResponse200
    | GetByOrgByRepoWebhooksResponse400
    | GetByOrgByRepoWebhooksResponse401
    | GetByOrgByRepoWebhooksResponse403
    | GetByOrgByRepoWebhooksResponse404
    | GetByOrgByRepoWebhooksResponse406
    | GetByOrgByRepoWebhooksResponse409
    | GetByOrgByRepoWebhooksResponse500
    | None
):
    """List webhooks

     List webhooks for a repository

    Args:
        org (str):
        repo (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoWebhooksResponse200 | GetByOrgByRepoWebhooksResponse400 | GetByOrgByRepoWebhooksResponse401 | GetByOrgByRepoWebhooksResponse403 | GetByOrgByRepoWebhooksResponse404 | GetByOrgByRepoWebhooksResponse406 | GetByOrgByRepoWebhooksResponse409 | GetByOrgByRepoWebhooksResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            client=client,
        )
    ).parsed

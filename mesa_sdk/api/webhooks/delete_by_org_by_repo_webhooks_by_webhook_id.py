from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_by_org_by_repo_webhooks_by_webhook_id_response_200 import (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse200,
)
from ...models.delete_by_org_by_repo_webhooks_by_webhook_id_response_400 import (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse400,
)
from ...models.delete_by_org_by_repo_webhooks_by_webhook_id_response_401 import (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse401,
)
from ...models.delete_by_org_by_repo_webhooks_by_webhook_id_response_403 import (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse403,
)
from ...models.delete_by_org_by_repo_webhooks_by_webhook_id_response_404 import (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse404,
)
from ...models.delete_by_org_by_repo_webhooks_by_webhook_id_response_406 import (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse406,
)
from ...models.delete_by_org_by_repo_webhooks_by_webhook_id_response_409 import (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse409,
)
from ...models.delete_by_org_by_repo_webhooks_by_webhook_id_response_500 import (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse500,
)
from ...types import Response


def _get_kwargs(
    org: str,
    repo: str,
    webhook_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{org}/{repo}/webhooks/{webhook_id}".format(
            org=quote(str(org), safe=""),
            repo=quote(str(repo), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse200
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse400
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse401
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse403
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse404
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse406
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse409
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DeleteByOrgByRepoWebhooksByWebhookIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteByOrgByRepoWebhooksByWebhookIdResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteByOrgByRepoWebhooksByWebhookIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteByOrgByRepoWebhooksByWebhookIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteByOrgByRepoWebhooksByWebhookIdResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = DeleteByOrgByRepoWebhooksByWebhookIdResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteByOrgByRepoWebhooksByWebhookIdResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = DeleteByOrgByRepoWebhooksByWebhookIdResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteByOrgByRepoWebhooksByWebhookIdResponse200
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse400
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse401
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse403
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse404
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse406
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse409
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse500
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
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteByOrgByRepoWebhooksByWebhookIdResponse200
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse400
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse401
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse403
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse404
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse406
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse409
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse500
]:
    """Delete webhook

     Delete a webhook from a repository

    Args:
        org (str):
        repo (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoWebhooksByWebhookIdResponse200 | DeleteByOrgByRepoWebhooksByWebhookIdResponse400 | DeleteByOrgByRepoWebhooksByWebhookIdResponse401 | DeleteByOrgByRepoWebhooksByWebhookIdResponse403 | DeleteByOrgByRepoWebhooksByWebhookIdResponse404 | DeleteByOrgByRepoWebhooksByWebhookIdResponse406 | DeleteByOrgByRepoWebhooksByWebhookIdResponse409 | DeleteByOrgByRepoWebhooksByWebhookIdResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org: str,
    repo: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse200
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse400
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse401
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse403
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse404
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse406
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse409
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse500
    | None
):
    """Delete webhook

     Delete a webhook from a repository

    Args:
        org (str):
        repo (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoWebhooksByWebhookIdResponse200 | DeleteByOrgByRepoWebhooksByWebhookIdResponse400 | DeleteByOrgByRepoWebhooksByWebhookIdResponse401 | DeleteByOrgByRepoWebhooksByWebhookIdResponse403 | DeleteByOrgByRepoWebhooksByWebhookIdResponse404 | DeleteByOrgByRepoWebhooksByWebhookIdResponse406 | DeleteByOrgByRepoWebhooksByWebhookIdResponse409 | DeleteByOrgByRepoWebhooksByWebhookIdResponse500
    """

    return sync_detailed(
        org=org,
        repo=repo,
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    repo: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteByOrgByRepoWebhooksByWebhookIdResponse200
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse400
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse401
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse403
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse404
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse406
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse409
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse500
]:
    """Delete webhook

     Delete a webhook from a repository

    Args:
        org (str):
        repo (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoWebhooksByWebhookIdResponse200 | DeleteByOrgByRepoWebhooksByWebhookIdResponse400 | DeleteByOrgByRepoWebhooksByWebhookIdResponse401 | DeleteByOrgByRepoWebhooksByWebhookIdResponse403 | DeleteByOrgByRepoWebhooksByWebhookIdResponse404 | DeleteByOrgByRepoWebhooksByWebhookIdResponse406 | DeleteByOrgByRepoWebhooksByWebhookIdResponse409 | DeleteByOrgByRepoWebhooksByWebhookIdResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    repo: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteByOrgByRepoWebhooksByWebhookIdResponse200
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse400
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse401
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse403
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse404
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse406
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse409
    | DeleteByOrgByRepoWebhooksByWebhookIdResponse500
    | None
):
    """Delete webhook

     Delete a webhook from a repository

    Args:
        org (str):
        repo (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoWebhooksByWebhookIdResponse200 | DeleteByOrgByRepoWebhooksByWebhookIdResponse400 | DeleteByOrgByRepoWebhooksByWebhookIdResponse401 | DeleteByOrgByRepoWebhooksByWebhookIdResponse403 | DeleteByOrgByRepoWebhooksByWebhookIdResponse404 | DeleteByOrgByRepoWebhooksByWebhookIdResponse406 | DeleteByOrgByRepoWebhooksByWebhookIdResponse409 | DeleteByOrgByRepoWebhooksByWebhookIdResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed

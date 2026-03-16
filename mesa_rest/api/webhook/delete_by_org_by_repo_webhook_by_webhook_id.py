from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_by_org_by_repo_webhook_by_webhook_id_response_200 import DeleteByOrgByRepoWebhookByWebhookIdResponse200
from ...models.delete_by_org_by_repo_webhook_by_webhook_id_response_400 import DeleteByOrgByRepoWebhookByWebhookIdResponse400
from ...models.delete_by_org_by_repo_webhook_by_webhook_id_response_401 import DeleteByOrgByRepoWebhookByWebhookIdResponse401
from ...models.delete_by_org_by_repo_webhook_by_webhook_id_response_403 import DeleteByOrgByRepoWebhookByWebhookIdResponse403
from ...models.delete_by_org_by_repo_webhook_by_webhook_id_response_404 import DeleteByOrgByRepoWebhookByWebhookIdResponse404
from ...models.delete_by_org_by_repo_webhook_by_webhook_id_response_406 import DeleteByOrgByRepoWebhookByWebhookIdResponse406
from ...models.delete_by_org_by_repo_webhook_by_webhook_id_response_409 import DeleteByOrgByRepoWebhookByWebhookIdResponse409
from ...models.delete_by_org_by_repo_webhook_by_webhook_id_response_500 import DeleteByOrgByRepoWebhookByWebhookIdResponse500
from typing import cast



def _get_kwargs(
    org: str,
    repo: str,
    webhook_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{org}/{repo}/webhook/{webhook_id}".format(org=quote(str(org), safe=""),repo=quote(str(repo), safe=""),webhook_id=quote(str(webhook_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteByOrgByRepoWebhookByWebhookIdResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteByOrgByRepoWebhookByWebhookIdResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteByOrgByRepoWebhookByWebhookIdResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteByOrgByRepoWebhookByWebhookIdResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteByOrgByRepoWebhookByWebhookIdResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = DeleteByOrgByRepoWebhookByWebhookIdResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = DeleteByOrgByRepoWebhookByWebhookIdResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = DeleteByOrgByRepoWebhookByWebhookIdResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500]:
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

) -> Response[DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500]:
    """ Delete webhook

     Delete a webhook from a repository

    Args:
        org (str):
        repo (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500]
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

) -> DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500 | None:
    """ Delete webhook

     Delete a webhook from a repository

    Args:
        org (str):
        repo (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500
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

) -> Response[DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500]:
    """ Delete webhook

     Delete a webhook from a repository

    Args:
        org (str):
        repo (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
webhook_id=webhook_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    repo: str,
    webhook_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500 | None:
    """ Delete webhook

     Delete a webhook from a repository

    Args:
        org (str):
        repo (str):
        webhook_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoWebhookByWebhookIdResponse200 | DeleteByOrgByRepoWebhookByWebhookIdResponse400 | DeleteByOrgByRepoWebhookByWebhookIdResponse401 | DeleteByOrgByRepoWebhookByWebhookIdResponse403 | DeleteByOrgByRepoWebhookByWebhookIdResponse404 | DeleteByOrgByRepoWebhookByWebhookIdResponse406 | DeleteByOrgByRepoWebhookByWebhookIdResponse409 | DeleteByOrgByRepoWebhookByWebhookIdResponse500
     """


    return (await asyncio_detailed(
        org=org,
repo=repo,
webhook_id=webhook_id,
client=client,

    )).parsed

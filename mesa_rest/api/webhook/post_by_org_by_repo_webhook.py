from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_by_org_by_repo_webhook_body import PostByOrgByRepoWebhookBody
from ...models.post_by_org_by_repo_webhook_response_201 import PostByOrgByRepoWebhookResponse201
from ...models.post_by_org_by_repo_webhook_response_400 import PostByOrgByRepoWebhookResponse400
from ...models.post_by_org_by_repo_webhook_response_401 import PostByOrgByRepoWebhookResponse401
from ...models.post_by_org_by_repo_webhook_response_403 import PostByOrgByRepoWebhookResponse403
from ...models.post_by_org_by_repo_webhook_response_404 import PostByOrgByRepoWebhookResponse404
from ...models.post_by_org_by_repo_webhook_response_406 import PostByOrgByRepoWebhookResponse406
from ...models.post_by_org_by_repo_webhook_response_409 import PostByOrgByRepoWebhookResponse409
from ...models.post_by_org_by_repo_webhook_response_500 import PostByOrgByRepoWebhookResponse500
from typing import cast



def _get_kwargs(
    org: str,
    repo: str,
    *,
    body: PostByOrgByRepoWebhookBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/{repo}/webhook".format(org=quote(str(org), safe=""),repo=quote(str(repo), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500 | None:
    if response.status_code == 201:
        response_201 = PostByOrgByRepoWebhookResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostByOrgByRepoWebhookResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgByRepoWebhookResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgByRepoWebhookResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgByRepoWebhookResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgByRepoWebhookResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgByRepoWebhookResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgByRepoWebhookResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500]:
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
    body: PostByOrgByRepoWebhookBody,

) -> Response[PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500]:
    """ Create webhook

     Create a webhook for a repository

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
body=body,

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
    body: PostByOrgByRepoWebhookBody,

) -> PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500 | None:
    """ Create webhook

     Create a webhook for a repository

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500
     """


    return sync_detailed(
        org=org,
repo=repo,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgByRepoWebhookBody,

) -> Response[PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500]:
    """ Create webhook

     Create a webhook for a repository

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
body=body,

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
    body: PostByOrgByRepoWebhookBody,

) -> PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500 | None:
    """ Create webhook

     Create a webhook for a repository

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgByRepoWebhookResponse201 | PostByOrgByRepoWebhookResponse400 | PostByOrgByRepoWebhookResponse401 | PostByOrgByRepoWebhookResponse403 | PostByOrgByRepoWebhookResponse404 | PostByOrgByRepoWebhookResponse406 | PostByOrgByRepoWebhookResponse409 | PostByOrgByRepoWebhookResponse500
     """


    return (await asyncio_detailed(
        org=org,
repo=repo,
client=client,
body=body,

    )).parsed

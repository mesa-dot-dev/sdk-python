from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_by_org_api_key_body import PostByOrgApiKeyBody
from ...models.post_by_org_api_key_response_201 import PostByOrgApiKeyResponse201
from ...models.post_by_org_api_key_response_400 import PostByOrgApiKeyResponse400
from ...models.post_by_org_api_key_response_401 import PostByOrgApiKeyResponse401
from ...models.post_by_org_api_key_response_403 import PostByOrgApiKeyResponse403
from ...models.post_by_org_api_key_response_404 import PostByOrgApiKeyResponse404
from ...models.post_by_org_api_key_response_406 import PostByOrgApiKeyResponse406
from ...models.post_by_org_api_key_response_409 import PostByOrgApiKeyResponse409
from ...models.post_by_org_api_key_response_500 import PostByOrgApiKeyResponse500
from typing import cast



def _get_kwargs(
    org: str,
    *,
    body: PostByOrgApiKeyBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/api-key".format(org=quote(str(org), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500 | None:
    if response.status_code == 201:
        response_201 = PostByOrgApiKeyResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostByOrgApiKeyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgApiKeyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgApiKeyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgApiKeyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgApiKeyResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgApiKeyResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgApiKeyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500]:
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
    body: PostByOrgApiKeyBody,

) -> Response[PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500]:
    """ Create API key

     Create a new API key for programmatic access

    Args:
        org (str):
        body (PostByOrgApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgApiKeyBody,

) -> PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500 | None:
    """ Create API key

     Create a new API key for programmatic access

    Args:
        org (str):
        body (PostByOrgApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500
     """


    return sync_detailed(
        org=org,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgApiKeyBody,

) -> Response[PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500]:
    """ Create API key

     Create a new API key for programmatic access

    Args:
        org (str):
        body (PostByOrgApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgApiKeyBody,

) -> PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500 | None:
    """ Create API key

     Create a new API key for programmatic access

    Args:
        org (str):
        body (PostByOrgApiKeyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgApiKeyResponse201 | PostByOrgApiKeyResponse400 | PostByOrgApiKeyResponse401 | PostByOrgApiKeyResponse403 | PostByOrgApiKeyResponse404 | PostByOrgApiKeyResponse406 | PostByOrgApiKeyResponse409 | PostByOrgApiKeyResponse500
     """


    return (await asyncio_detailed(
        org=org,
client=client,
body=body,

    )).parsed

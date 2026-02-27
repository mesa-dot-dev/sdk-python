from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_by_org_api_keys_body import PostByOrgApiKeysBody
from ...models.post_by_org_api_keys_response_201 import PostByOrgApiKeysResponse201
from ...models.post_by_org_api_keys_response_400 import PostByOrgApiKeysResponse400
from ...models.post_by_org_api_keys_response_401 import PostByOrgApiKeysResponse401
from ...models.post_by_org_api_keys_response_403 import PostByOrgApiKeysResponse403
from ...models.post_by_org_api_keys_response_404 import PostByOrgApiKeysResponse404
from ...models.post_by_org_api_keys_response_406 import PostByOrgApiKeysResponse406
from ...models.post_by_org_api_keys_response_409 import PostByOrgApiKeysResponse409
from ...models.post_by_org_api_keys_response_500 import PostByOrgApiKeysResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org: str,
    *,
    body: PostByOrgApiKeysBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/api-keys".format(
            org=quote(str(org), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostByOrgApiKeysResponse201
    | PostByOrgApiKeysResponse400
    | PostByOrgApiKeysResponse401
    | PostByOrgApiKeysResponse403
    | PostByOrgApiKeysResponse404
    | PostByOrgApiKeysResponse406
    | PostByOrgApiKeysResponse409
    | PostByOrgApiKeysResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostByOrgApiKeysResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostByOrgApiKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgApiKeysResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgApiKeysResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgApiKeysResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgApiKeysResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgApiKeysResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgApiKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostByOrgApiKeysResponse201
    | PostByOrgApiKeysResponse400
    | PostByOrgApiKeysResponse401
    | PostByOrgApiKeysResponse403
    | PostByOrgApiKeysResponse404
    | PostByOrgApiKeysResponse406
    | PostByOrgApiKeysResponse409
    | PostByOrgApiKeysResponse500
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
    body: PostByOrgApiKeysBody | Unset = UNSET,
) -> Response[
    PostByOrgApiKeysResponse201
    | PostByOrgApiKeysResponse400
    | PostByOrgApiKeysResponse401
    | PostByOrgApiKeysResponse403
    | PostByOrgApiKeysResponse404
    | PostByOrgApiKeysResponse406
    | PostByOrgApiKeysResponse409
    | PostByOrgApiKeysResponse500
]:
    """Create API key

     Create a new API key for programmatic access

    Args:
        org (str):
        body (PostByOrgApiKeysBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgApiKeysResponse201 | PostByOrgApiKeysResponse400 | PostByOrgApiKeysResponse401 | PostByOrgApiKeysResponse403 | PostByOrgApiKeysResponse404 | PostByOrgApiKeysResponse406 | PostByOrgApiKeysResponse409 | PostByOrgApiKeysResponse500]
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
    body: PostByOrgApiKeysBody | Unset = UNSET,
) -> (
    PostByOrgApiKeysResponse201
    | PostByOrgApiKeysResponse400
    | PostByOrgApiKeysResponse401
    | PostByOrgApiKeysResponse403
    | PostByOrgApiKeysResponse404
    | PostByOrgApiKeysResponse406
    | PostByOrgApiKeysResponse409
    | PostByOrgApiKeysResponse500
    | None
):
    """Create API key

     Create a new API key for programmatic access

    Args:
        org (str):
        body (PostByOrgApiKeysBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgApiKeysResponse201 | PostByOrgApiKeysResponse400 | PostByOrgApiKeysResponse401 | PostByOrgApiKeysResponse403 | PostByOrgApiKeysResponse404 | PostByOrgApiKeysResponse406 | PostByOrgApiKeysResponse409 | PostByOrgApiKeysResponse500
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
    body: PostByOrgApiKeysBody | Unset = UNSET,
) -> Response[
    PostByOrgApiKeysResponse201
    | PostByOrgApiKeysResponse400
    | PostByOrgApiKeysResponse401
    | PostByOrgApiKeysResponse403
    | PostByOrgApiKeysResponse404
    | PostByOrgApiKeysResponse406
    | PostByOrgApiKeysResponse409
    | PostByOrgApiKeysResponse500
]:
    """Create API key

     Create a new API key for programmatic access

    Args:
        org (str):
        body (PostByOrgApiKeysBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgApiKeysResponse201 | PostByOrgApiKeysResponse400 | PostByOrgApiKeysResponse401 | PostByOrgApiKeysResponse403 | PostByOrgApiKeysResponse404 | PostByOrgApiKeysResponse406 | PostByOrgApiKeysResponse409 | PostByOrgApiKeysResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgApiKeysBody | Unset = UNSET,
) -> (
    PostByOrgApiKeysResponse201
    | PostByOrgApiKeysResponse400
    | PostByOrgApiKeysResponse401
    | PostByOrgApiKeysResponse403
    | PostByOrgApiKeysResponse404
    | PostByOrgApiKeysResponse406
    | PostByOrgApiKeysResponse409
    | PostByOrgApiKeysResponse500
    | None
):
    """Create API key

     Create a new API key for programmatic access

    Args:
        org (str):
        body (PostByOrgApiKeysBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgApiKeysResponse201 | PostByOrgApiKeysResponse400 | PostByOrgApiKeysResponse401 | PostByOrgApiKeysResponse403 | PostByOrgApiKeysResponse404 | PostByOrgApiKeysResponse406 | PostByOrgApiKeysResponse409 | PostByOrgApiKeysResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
            body=body,
        )
    ).parsed

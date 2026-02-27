from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_by_org_repos_body import PostByOrgReposBody
from ...models.post_by_org_repos_response_201 import PostByOrgReposResponse201
from ...models.post_by_org_repos_response_400 import PostByOrgReposResponse400
from ...models.post_by_org_repos_response_401 import PostByOrgReposResponse401
from ...models.post_by_org_repos_response_403 import PostByOrgReposResponse403
from ...models.post_by_org_repos_response_404 import PostByOrgReposResponse404
from ...models.post_by_org_repos_response_406 import PostByOrgReposResponse406
from ...models.post_by_org_repos_response_409 import PostByOrgReposResponse409
from ...models.post_by_org_repos_response_500 import PostByOrgReposResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org: str,
    *,
    body: PostByOrgReposBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/repos".format(
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
    PostByOrgReposResponse201
    | PostByOrgReposResponse400
    | PostByOrgReposResponse401
    | PostByOrgReposResponse403
    | PostByOrgReposResponse404
    | PostByOrgReposResponse406
    | PostByOrgReposResponse409
    | PostByOrgReposResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostByOrgReposResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostByOrgReposResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgReposResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgReposResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgReposResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgReposResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgReposResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgReposResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostByOrgReposResponse201
    | PostByOrgReposResponse400
    | PostByOrgReposResponse401
    | PostByOrgReposResponse403
    | PostByOrgReposResponse404
    | PostByOrgReposResponse406
    | PostByOrgReposResponse409
    | PostByOrgReposResponse500
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
    body: PostByOrgReposBody | Unset = UNSET,
) -> Response[
    PostByOrgReposResponse201
    | PostByOrgReposResponse400
    | PostByOrgReposResponse401
    | PostByOrgReposResponse403
    | PostByOrgReposResponse404
    | PostByOrgReposResponse406
    | PostByOrgReposResponse409
    | PostByOrgReposResponse500
]:
    """Create repository

     Create a new repository in the organization

    Args:
        org (str):
        body (PostByOrgReposBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgReposResponse201 | PostByOrgReposResponse400 | PostByOrgReposResponse401 | PostByOrgReposResponse403 | PostByOrgReposResponse404 | PostByOrgReposResponse406 | PostByOrgReposResponse409 | PostByOrgReposResponse500]
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
    body: PostByOrgReposBody | Unset = UNSET,
) -> (
    PostByOrgReposResponse201
    | PostByOrgReposResponse400
    | PostByOrgReposResponse401
    | PostByOrgReposResponse403
    | PostByOrgReposResponse404
    | PostByOrgReposResponse406
    | PostByOrgReposResponse409
    | PostByOrgReposResponse500
    | None
):
    """Create repository

     Create a new repository in the organization

    Args:
        org (str):
        body (PostByOrgReposBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgReposResponse201 | PostByOrgReposResponse400 | PostByOrgReposResponse401 | PostByOrgReposResponse403 | PostByOrgReposResponse404 | PostByOrgReposResponse406 | PostByOrgReposResponse409 | PostByOrgReposResponse500
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
    body: PostByOrgReposBody | Unset = UNSET,
) -> Response[
    PostByOrgReposResponse201
    | PostByOrgReposResponse400
    | PostByOrgReposResponse401
    | PostByOrgReposResponse403
    | PostByOrgReposResponse404
    | PostByOrgReposResponse406
    | PostByOrgReposResponse409
    | PostByOrgReposResponse500
]:
    """Create repository

     Create a new repository in the organization

    Args:
        org (str):
        body (PostByOrgReposBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgReposResponse201 | PostByOrgReposResponse400 | PostByOrgReposResponse401 | PostByOrgReposResponse403 | PostByOrgReposResponse404 | PostByOrgReposResponse406 | PostByOrgReposResponse409 | PostByOrgReposResponse500]
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
    body: PostByOrgReposBody | Unset = UNSET,
) -> (
    PostByOrgReposResponse201
    | PostByOrgReposResponse400
    | PostByOrgReposResponse401
    | PostByOrgReposResponse403
    | PostByOrgReposResponse404
    | PostByOrgReposResponse406
    | PostByOrgReposResponse409
    | PostByOrgReposResponse500
    | None
):
    """Create repository

     Create a new repository in the organization

    Args:
        org (str):
        body (PostByOrgReposBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgReposResponse201 | PostByOrgReposResponse400 | PostByOrgReposResponse401 | PostByOrgReposResponse403 | PostByOrgReposResponse404 | PostByOrgReposResponse406 | PostByOrgReposResponse409 | PostByOrgReposResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
            body=body,
        )
    ).parsed

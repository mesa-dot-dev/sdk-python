from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_by_org_repo_body import PostByOrgRepoBody
from ...models.post_by_org_repo_response_201 import PostByOrgRepoResponse201
from ...models.post_by_org_repo_response_400 import PostByOrgRepoResponse400
from ...models.post_by_org_repo_response_401 import PostByOrgRepoResponse401
from ...models.post_by_org_repo_response_403 import PostByOrgRepoResponse403
from ...models.post_by_org_repo_response_404 import PostByOrgRepoResponse404
from ...models.post_by_org_repo_response_406 import PostByOrgRepoResponse406
from ...models.post_by_org_repo_response_409 import PostByOrgRepoResponse409
from ...models.post_by_org_repo_response_500 import PostByOrgRepoResponse500
from typing import cast



def _get_kwargs(
    org: str,
    *,
    body: PostByOrgRepoBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/repo".format(org=quote(str(org), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500 | None:
    if response.status_code == 201:
        response_201 = PostByOrgRepoResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostByOrgRepoResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgRepoResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgRepoResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgRepoResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgRepoResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgRepoResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgRepoResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500]:
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
    body: PostByOrgRepoBody,

) -> Response[PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500]:
    """ Create repository

     Create a new repository in the organization

    Args:
        org (str):
        body (PostByOrgRepoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500]
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
    body: PostByOrgRepoBody,

) -> PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500 | None:
    """ Create repository

     Create a new repository in the organization

    Args:
        org (str):
        body (PostByOrgRepoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500
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
    body: PostByOrgRepoBody,

) -> Response[PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500]:
    """ Create repository

     Create a new repository in the organization

    Args:
        org (str):
        body (PostByOrgRepoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500]
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
    body: PostByOrgRepoBody,

) -> PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500 | None:
    """ Create repository

     Create a new repository in the organization

    Args:
        org (str):
        body (PostByOrgRepoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgRepoResponse201 | PostByOrgRepoResponse400 | PostByOrgRepoResponse401 | PostByOrgRepoResponse403 | PostByOrgRepoResponse404 | PostByOrgRepoResponse406 | PostByOrgRepoResponse409 | PostByOrgRepoResponse500
     """


    return (await asyncio_detailed(
        org=org,
client=client,
body=body,

    )).parsed

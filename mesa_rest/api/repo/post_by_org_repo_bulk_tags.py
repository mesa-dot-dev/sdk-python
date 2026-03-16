from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_by_org_repo_bulk_tags_body import PostByOrgRepoBulkTagsBody
from ...models.post_by_org_repo_bulk_tags_response_200 import PostByOrgRepoBulkTagsResponse200
from ...models.post_by_org_repo_bulk_tags_response_400 import PostByOrgRepoBulkTagsResponse400
from ...models.post_by_org_repo_bulk_tags_response_401 import PostByOrgRepoBulkTagsResponse401
from ...models.post_by_org_repo_bulk_tags_response_403 import PostByOrgRepoBulkTagsResponse403
from ...models.post_by_org_repo_bulk_tags_response_404 import PostByOrgRepoBulkTagsResponse404
from ...models.post_by_org_repo_bulk_tags_response_406 import PostByOrgRepoBulkTagsResponse406
from ...models.post_by_org_repo_bulk_tags_response_409 import PostByOrgRepoBulkTagsResponse409
from ...models.post_by_org_repo_bulk_tags_response_500 import PostByOrgRepoBulkTagsResponse500
from typing import cast



def _get_kwargs(
    org: str,
    *,
    body: PostByOrgRepoBulkTagsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/repo/bulk/tags".format(org=quote(str(org), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500 | None:
    if response.status_code == 200:
        response_200 = PostByOrgRepoBulkTagsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostByOrgRepoBulkTagsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgRepoBulkTagsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgRepoBulkTagsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgRepoBulkTagsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgRepoBulkTagsResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgRepoBulkTagsResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgRepoBulkTagsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500]:
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
    body: PostByOrgRepoBulkTagsBody,

) -> Response[PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500]:
    """ Bulk update Tags

     Bulk set or remove repo tags

    Args:
        org (str):
        body (PostByOrgRepoBulkTagsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500]
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
    body: PostByOrgRepoBulkTagsBody,

) -> PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500 | None:
    """ Bulk update Tags

     Bulk set or remove repo tags

    Args:
        org (str):
        body (PostByOrgRepoBulkTagsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500
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
    body: PostByOrgRepoBulkTagsBody,

) -> Response[PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500]:
    """ Bulk update Tags

     Bulk set or remove repo tags

    Args:
        org (str):
        body (PostByOrgRepoBulkTagsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500]
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
    body: PostByOrgRepoBulkTagsBody,

) -> PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500 | None:
    """ Bulk update Tags

     Bulk set or remove repo tags

    Args:
        org (str):
        body (PostByOrgRepoBulkTagsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgRepoBulkTagsResponse200 | PostByOrgRepoBulkTagsResponse400 | PostByOrgRepoBulkTagsResponse401 | PostByOrgRepoBulkTagsResponse403 | PostByOrgRepoBulkTagsResponse404 | PostByOrgRepoBulkTagsResponse406 | PostByOrgRepoBulkTagsResponse409 | PostByOrgRepoBulkTagsResponse500
     """


    return (await asyncio_detailed(
        org=org,
client=client,
body=body,

    )).parsed

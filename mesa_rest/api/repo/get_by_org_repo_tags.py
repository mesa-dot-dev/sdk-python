from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_by_org_repo_tags_response_200 import GetByOrgRepoTagsResponse200
from ...models.get_by_org_repo_tags_response_400 import GetByOrgRepoTagsResponse400
from ...models.get_by_org_repo_tags_response_401 import GetByOrgRepoTagsResponse401
from ...models.get_by_org_repo_tags_response_403 import GetByOrgRepoTagsResponse403
from ...models.get_by_org_repo_tags_response_404 import GetByOrgRepoTagsResponse404
from ...models.get_by_org_repo_tags_response_406 import GetByOrgRepoTagsResponse406
from ...models.get_by_org_repo_tags_response_409 import GetByOrgRepoTagsResponse409
from ...models.get_by_org_repo_tags_response_500 import GetByOrgRepoTagsResponse500
from typing import cast



def _get_kwargs(
    org: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/repo/tags".format(org=quote(str(org), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetByOrgRepoTagsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgRepoTagsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgRepoTagsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgRepoTagsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgRepoTagsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgRepoTagsResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgRepoTagsResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgRepoTagsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500]:
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

) -> Response[GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500]:
    """ Get repo Tags

     Get repository tag values and counts

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500]
     """


    kwargs = _get_kwargs(
        org=org,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    org: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500 | None:
    """ Get repo Tags

     Get repository tag values and counts

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500
     """


    return sync_detailed(
        org=org,
client=client,

    ).parsed

async def asyncio_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500]:
    """ Get repo Tags

     Get repository tag values and counts

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500]
     """


    kwargs = _get_kwargs(
        org=org,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient | Client,

) -> GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500 | None:
    """ Get repo Tags

     Get repository tag values and counts

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgRepoTagsResponse200 | GetByOrgRepoTagsResponse400 | GetByOrgRepoTagsResponse401 | GetByOrgRepoTagsResponse403 | GetByOrgRepoTagsResponse404 | GetByOrgRepoTagsResponse406 | GetByOrgRepoTagsResponse409 | GetByOrgRepoTagsResponse500
     """


    return (await asyncio_detailed(
        org=org,
client=client,

    )).parsed

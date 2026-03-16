from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_whoami_response_200 import GetWhoamiResponse200
from ...models.get_whoami_response_400 import GetWhoamiResponse400
from ...models.get_whoami_response_401 import GetWhoamiResponse401
from ...models.get_whoami_response_403 import GetWhoamiResponse403
from ...models.get_whoami_response_404 import GetWhoamiResponse404
from ...models.get_whoami_response_406 import GetWhoamiResponse406
from ...models.get_whoami_response_409 import GetWhoamiResponse409
from ...models.get_whoami_response_500 import GetWhoamiResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/whoami",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500 | None:
    if response.status_code == 200:
        response_200 = GetWhoamiResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetWhoamiResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetWhoamiResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetWhoamiResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetWhoamiResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = GetWhoamiResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = GetWhoamiResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = GetWhoamiResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500]:
    """ Get caller identity

     Get the authenticated organization, effective scopes, and API key metadata

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500 | None:
    """ Get caller identity

     Get the authenticated organization, effective scopes, and API key metadata

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500]:
    """ Get caller identity

     Get the authenticated organization, effective scopes, and API key metadata

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500 | None:
    """ Get caller identity

     Get the authenticated organization, effective scopes, and API key metadata

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWhoamiResponse200 | GetWhoamiResponse400 | GetWhoamiResponse401 | GetWhoamiResponse403 | GetWhoamiResponse404 | GetWhoamiResponse406 | GetWhoamiResponse409 | GetWhoamiResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed

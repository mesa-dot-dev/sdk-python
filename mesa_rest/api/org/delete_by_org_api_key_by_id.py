from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_by_org_api_key_by_id_response_200 import DeleteByOrgApiKeyByIdResponse200
from ...models.delete_by_org_api_key_by_id_response_400 import DeleteByOrgApiKeyByIdResponse400
from ...models.delete_by_org_api_key_by_id_response_401 import DeleteByOrgApiKeyByIdResponse401
from ...models.delete_by_org_api_key_by_id_response_403 import DeleteByOrgApiKeyByIdResponse403
from ...models.delete_by_org_api_key_by_id_response_404 import DeleteByOrgApiKeyByIdResponse404
from ...models.delete_by_org_api_key_by_id_response_406 import DeleteByOrgApiKeyByIdResponse406
from ...models.delete_by_org_api_key_by_id_response_409 import DeleteByOrgApiKeyByIdResponse409
from ...models.delete_by_org_api_key_by_id_response_500 import DeleteByOrgApiKeyByIdResponse500
from typing import cast



def _get_kwargs(
    org: str,
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{org}/api-key/{id}".format(org=quote(str(org), safe=""),id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteByOrgApiKeyByIdResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteByOrgApiKeyByIdResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteByOrgApiKeyByIdResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteByOrgApiKeyByIdResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteByOrgApiKeyByIdResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = DeleteByOrgApiKeyByIdResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = DeleteByOrgApiKeyByIdResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = DeleteByOrgApiKeyByIdResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500]:
    """ Revoke API key

     Revoke an API key by its ID

    Args:
        org (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    org: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500 | None:
    """ Revoke API key

     Revoke an API key by its ID

    Args:
        org (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500
     """


    return sync_detailed(
        org=org,
id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    org: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500]:
    """ Revoke API key

     Revoke an API key by its ID

    Args:
        org (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500 | None:
    """ Revoke API key

     Revoke an API key by its ID

    Args:
        org (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgApiKeyByIdResponse200 | DeleteByOrgApiKeyByIdResponse400 | DeleteByOrgApiKeyByIdResponse401 | DeleteByOrgApiKeyByIdResponse403 | DeleteByOrgApiKeyByIdResponse404 | DeleteByOrgApiKeyByIdResponse406 | DeleteByOrgApiKeyByIdResponse409 | DeleteByOrgApiKeyByIdResponse500
     """


    return (await asyncio_detailed(
        org=org,
id=id,
client=client,

    )).parsed

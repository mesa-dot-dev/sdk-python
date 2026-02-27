from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_org_api_keys_response_200 import GetByOrgApiKeysResponse200
from ...models.get_by_org_api_keys_response_400 import GetByOrgApiKeysResponse400
from ...models.get_by_org_api_keys_response_401 import GetByOrgApiKeysResponse401
from ...models.get_by_org_api_keys_response_403 import GetByOrgApiKeysResponse403
from ...models.get_by_org_api_keys_response_404 import GetByOrgApiKeysResponse404
from ...models.get_by_org_api_keys_response_406 import GetByOrgApiKeysResponse406
from ...models.get_by_org_api_keys_response_409 import GetByOrgApiKeysResponse409
from ...models.get_by_org_api_keys_response_500 import GetByOrgApiKeysResponse500
from ...types import Response


def _get_kwargs(
    org: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/api-keys".format(
            org=quote(str(org), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetByOrgApiKeysResponse200
    | GetByOrgApiKeysResponse400
    | GetByOrgApiKeysResponse401
    | GetByOrgApiKeysResponse403
    | GetByOrgApiKeysResponse404
    | GetByOrgApiKeysResponse406
    | GetByOrgApiKeysResponse409
    | GetByOrgApiKeysResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetByOrgApiKeysResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgApiKeysResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgApiKeysResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgApiKeysResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgApiKeysResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgApiKeysResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgApiKeysResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgApiKeysResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetByOrgApiKeysResponse200
    | GetByOrgApiKeysResponse400
    | GetByOrgApiKeysResponse401
    | GetByOrgApiKeysResponse403
    | GetByOrgApiKeysResponse404
    | GetByOrgApiKeysResponse406
    | GetByOrgApiKeysResponse409
    | GetByOrgApiKeysResponse500
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
) -> Response[
    GetByOrgApiKeysResponse200
    | GetByOrgApiKeysResponse400
    | GetByOrgApiKeysResponse401
    | GetByOrgApiKeysResponse403
    | GetByOrgApiKeysResponse404
    | GetByOrgApiKeysResponse406
    | GetByOrgApiKeysResponse409
    | GetByOrgApiKeysResponse500
]:
    """List API keys

     List all API keys for the organization (key values are not returned)

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgApiKeysResponse200 | GetByOrgApiKeysResponse400 | GetByOrgApiKeysResponse401 | GetByOrgApiKeysResponse403 | GetByOrgApiKeysResponse404 | GetByOrgApiKeysResponse406 | GetByOrgApiKeysResponse409 | GetByOrgApiKeysResponse500]
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
) -> (
    GetByOrgApiKeysResponse200
    | GetByOrgApiKeysResponse400
    | GetByOrgApiKeysResponse401
    | GetByOrgApiKeysResponse403
    | GetByOrgApiKeysResponse404
    | GetByOrgApiKeysResponse406
    | GetByOrgApiKeysResponse409
    | GetByOrgApiKeysResponse500
    | None
):
    """List API keys

     List all API keys for the organization (key values are not returned)

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgApiKeysResponse200 | GetByOrgApiKeysResponse400 | GetByOrgApiKeysResponse401 | GetByOrgApiKeysResponse403 | GetByOrgApiKeysResponse404 | GetByOrgApiKeysResponse406 | GetByOrgApiKeysResponse409 | GetByOrgApiKeysResponse500
    """

    return sync_detailed(
        org=org,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetByOrgApiKeysResponse200
    | GetByOrgApiKeysResponse400
    | GetByOrgApiKeysResponse401
    | GetByOrgApiKeysResponse403
    | GetByOrgApiKeysResponse404
    | GetByOrgApiKeysResponse406
    | GetByOrgApiKeysResponse409
    | GetByOrgApiKeysResponse500
]:
    """List API keys

     List all API keys for the organization (key values are not returned)

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgApiKeysResponse200 | GetByOrgApiKeysResponse400 | GetByOrgApiKeysResponse401 | GetByOrgApiKeysResponse403 | GetByOrgApiKeysResponse404 | GetByOrgApiKeysResponse406 | GetByOrgApiKeysResponse409 | GetByOrgApiKeysResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetByOrgApiKeysResponse200
    | GetByOrgApiKeysResponse400
    | GetByOrgApiKeysResponse401
    | GetByOrgApiKeysResponse403
    | GetByOrgApiKeysResponse404
    | GetByOrgApiKeysResponse406
    | GetByOrgApiKeysResponse409
    | GetByOrgApiKeysResponse500
    | None
):
    """List API keys

     List all API keys for the organization (key values are not returned)

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgApiKeysResponse200 | GetByOrgApiKeysResponse400 | GetByOrgApiKeysResponse401 | GetByOrgApiKeysResponse403 | GetByOrgApiKeysResponse404 | GetByOrgApiKeysResponse406 | GetByOrgApiKeysResponse409 | GetByOrgApiKeysResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
        )
    ).parsed

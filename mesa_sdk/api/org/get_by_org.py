from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_org_response_200 import GetByOrgResponse200
from ...models.get_by_org_response_400 import GetByOrgResponse400
from ...models.get_by_org_response_401 import GetByOrgResponse401
from ...models.get_by_org_response_403 import GetByOrgResponse403
from ...models.get_by_org_response_404 import GetByOrgResponse404
from ...models.get_by_org_response_406 import GetByOrgResponse406
from ...models.get_by_org_response_409 import GetByOrgResponse409
from ...models.get_by_org_response_500 import GetByOrgResponse500
from ...types import Response


def _get_kwargs(
    org: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}".format(
            org=quote(str(org), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetByOrgResponse200
    | GetByOrgResponse400
    | GetByOrgResponse401
    | GetByOrgResponse403
    | GetByOrgResponse404
    | GetByOrgResponse406
    | GetByOrgResponse409
    | GetByOrgResponse500
    | None
):
    if response.status_code == 200:
        response_200 = GetByOrgResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetByOrgResponse200
    | GetByOrgResponse400
    | GetByOrgResponse401
    | GetByOrgResponse403
    | GetByOrgResponse404
    | GetByOrgResponse406
    | GetByOrgResponse409
    | GetByOrgResponse500
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
    GetByOrgResponse200
    | GetByOrgResponse400
    | GetByOrgResponse401
    | GetByOrgResponse403
    | GetByOrgResponse404
    | GetByOrgResponse406
    | GetByOrgResponse409
    | GetByOrgResponse500
]:
    """Get organization

     Get organization metadata and repository counts

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgResponse200 | GetByOrgResponse400 | GetByOrgResponse401 | GetByOrgResponse403 | GetByOrgResponse404 | GetByOrgResponse406 | GetByOrgResponse409 | GetByOrgResponse500]
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
    GetByOrgResponse200
    | GetByOrgResponse400
    | GetByOrgResponse401
    | GetByOrgResponse403
    | GetByOrgResponse404
    | GetByOrgResponse406
    | GetByOrgResponse409
    | GetByOrgResponse500
    | None
):
    """Get organization

     Get organization metadata and repository counts

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgResponse200 | GetByOrgResponse400 | GetByOrgResponse401 | GetByOrgResponse403 | GetByOrgResponse404 | GetByOrgResponse406 | GetByOrgResponse409 | GetByOrgResponse500
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
    GetByOrgResponse200
    | GetByOrgResponse400
    | GetByOrgResponse401
    | GetByOrgResponse403
    | GetByOrgResponse404
    | GetByOrgResponse406
    | GetByOrgResponse409
    | GetByOrgResponse500
]:
    """Get organization

     Get organization metadata and repository counts

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgResponse200 | GetByOrgResponse400 | GetByOrgResponse401 | GetByOrgResponse403 | GetByOrgResponse404 | GetByOrgResponse406 | GetByOrgResponse409 | GetByOrgResponse500]
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
    GetByOrgResponse200
    | GetByOrgResponse400
    | GetByOrgResponse401
    | GetByOrgResponse403
    | GetByOrgResponse404
    | GetByOrgResponse406
    | GetByOrgResponse409
    | GetByOrgResponse500
    | None
):
    """Get organization

     Get organization metadata and repository counts

    Args:
        org (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgResponse200 | GetByOrgResponse400 | GetByOrgResponse401 | GetByOrgResponse403 | GetByOrgResponse404 | GetByOrgResponse406 | GetByOrgResponse409 | GetByOrgResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            client=client,
        )
    ).parsed

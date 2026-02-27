from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_by_org_api_keys_by_id_response_200 import DeleteByOrgApiKeysByIdResponse200
from ...models.delete_by_org_api_keys_by_id_response_400 import DeleteByOrgApiKeysByIdResponse400
from ...models.delete_by_org_api_keys_by_id_response_401 import DeleteByOrgApiKeysByIdResponse401
from ...models.delete_by_org_api_keys_by_id_response_403 import DeleteByOrgApiKeysByIdResponse403
from ...models.delete_by_org_api_keys_by_id_response_404 import DeleteByOrgApiKeysByIdResponse404
from ...models.delete_by_org_api_keys_by_id_response_406 import DeleteByOrgApiKeysByIdResponse406
from ...models.delete_by_org_api_keys_by_id_response_409 import DeleteByOrgApiKeysByIdResponse409
from ...models.delete_by_org_api_keys_by_id_response_500 import DeleteByOrgApiKeysByIdResponse500
from ...types import Response


def _get_kwargs(
    org: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{org}/api-keys/{id}".format(
            org=quote(str(org), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteByOrgApiKeysByIdResponse200
    | DeleteByOrgApiKeysByIdResponse400
    | DeleteByOrgApiKeysByIdResponse401
    | DeleteByOrgApiKeysByIdResponse403
    | DeleteByOrgApiKeysByIdResponse404
    | DeleteByOrgApiKeysByIdResponse406
    | DeleteByOrgApiKeysByIdResponse409
    | DeleteByOrgApiKeysByIdResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DeleteByOrgApiKeysByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteByOrgApiKeysByIdResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteByOrgApiKeysByIdResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteByOrgApiKeysByIdResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteByOrgApiKeysByIdResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = DeleteByOrgApiKeysByIdResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteByOrgApiKeysByIdResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = DeleteByOrgApiKeysByIdResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteByOrgApiKeysByIdResponse200
    | DeleteByOrgApiKeysByIdResponse400
    | DeleteByOrgApiKeysByIdResponse401
    | DeleteByOrgApiKeysByIdResponse403
    | DeleteByOrgApiKeysByIdResponse404
    | DeleteByOrgApiKeysByIdResponse406
    | DeleteByOrgApiKeysByIdResponse409
    | DeleteByOrgApiKeysByIdResponse500
]:
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
) -> Response[
    DeleteByOrgApiKeysByIdResponse200
    | DeleteByOrgApiKeysByIdResponse400
    | DeleteByOrgApiKeysByIdResponse401
    | DeleteByOrgApiKeysByIdResponse403
    | DeleteByOrgApiKeysByIdResponse404
    | DeleteByOrgApiKeysByIdResponse406
    | DeleteByOrgApiKeysByIdResponse409
    | DeleteByOrgApiKeysByIdResponse500
]:
    """Revoke API key

     Revoke an API key by its ID

    Args:
        org (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgApiKeysByIdResponse200 | DeleteByOrgApiKeysByIdResponse400 | DeleteByOrgApiKeysByIdResponse401 | DeleteByOrgApiKeysByIdResponse403 | DeleteByOrgApiKeysByIdResponse404 | DeleteByOrgApiKeysByIdResponse406 | DeleteByOrgApiKeysByIdResponse409 | DeleteByOrgApiKeysByIdResponse500]
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
) -> (
    DeleteByOrgApiKeysByIdResponse200
    | DeleteByOrgApiKeysByIdResponse400
    | DeleteByOrgApiKeysByIdResponse401
    | DeleteByOrgApiKeysByIdResponse403
    | DeleteByOrgApiKeysByIdResponse404
    | DeleteByOrgApiKeysByIdResponse406
    | DeleteByOrgApiKeysByIdResponse409
    | DeleteByOrgApiKeysByIdResponse500
    | None
):
    """Revoke API key

     Revoke an API key by its ID

    Args:
        org (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgApiKeysByIdResponse200 | DeleteByOrgApiKeysByIdResponse400 | DeleteByOrgApiKeysByIdResponse401 | DeleteByOrgApiKeysByIdResponse403 | DeleteByOrgApiKeysByIdResponse404 | DeleteByOrgApiKeysByIdResponse406 | DeleteByOrgApiKeysByIdResponse409 | DeleteByOrgApiKeysByIdResponse500
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
) -> Response[
    DeleteByOrgApiKeysByIdResponse200
    | DeleteByOrgApiKeysByIdResponse400
    | DeleteByOrgApiKeysByIdResponse401
    | DeleteByOrgApiKeysByIdResponse403
    | DeleteByOrgApiKeysByIdResponse404
    | DeleteByOrgApiKeysByIdResponse406
    | DeleteByOrgApiKeysByIdResponse409
    | DeleteByOrgApiKeysByIdResponse500
]:
    """Revoke API key

     Revoke an API key by its ID

    Args:
        org (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgApiKeysByIdResponse200 | DeleteByOrgApiKeysByIdResponse400 | DeleteByOrgApiKeysByIdResponse401 | DeleteByOrgApiKeysByIdResponse403 | DeleteByOrgApiKeysByIdResponse404 | DeleteByOrgApiKeysByIdResponse406 | DeleteByOrgApiKeysByIdResponse409 | DeleteByOrgApiKeysByIdResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteByOrgApiKeysByIdResponse200
    | DeleteByOrgApiKeysByIdResponse400
    | DeleteByOrgApiKeysByIdResponse401
    | DeleteByOrgApiKeysByIdResponse403
    | DeleteByOrgApiKeysByIdResponse404
    | DeleteByOrgApiKeysByIdResponse406
    | DeleteByOrgApiKeysByIdResponse409
    | DeleteByOrgApiKeysByIdResponse500
    | None
):
    """Revoke API key

     Revoke an API key by its ID

    Args:
        org (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgApiKeysByIdResponse200 | DeleteByOrgApiKeysByIdResponse400 | DeleteByOrgApiKeysByIdResponse401 | DeleteByOrgApiKeysByIdResponse403 | DeleteByOrgApiKeysByIdResponse404 | DeleteByOrgApiKeysByIdResponse406 | DeleteByOrgApiKeysByIdResponse409 | DeleteByOrgApiKeysByIdResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            id=id,
            client=client,
        )
    ).parsed

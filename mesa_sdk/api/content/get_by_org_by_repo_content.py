from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_org_by_repo_content_response_200_type_0 import GetByOrgByRepoContentResponse200Type0
from ...models.get_by_org_by_repo_content_response_200_type_1 import GetByOrgByRepoContentResponse200Type1
from ...models.get_by_org_by_repo_content_response_200_type_2 import GetByOrgByRepoContentResponse200Type2
from ...models.get_by_org_by_repo_content_response_400 import GetByOrgByRepoContentResponse400
from ...models.get_by_org_by_repo_content_response_401 import GetByOrgByRepoContentResponse401
from ...models.get_by_org_by_repo_content_response_403 import GetByOrgByRepoContentResponse403
from ...models.get_by_org_by_repo_content_response_404 import GetByOrgByRepoContentResponse404
from ...models.get_by_org_by_repo_content_response_406 import GetByOrgByRepoContentResponse406
from ...models.get_by_org_by_repo_content_response_409 import GetByOrgByRepoContentResponse409
from ...models.get_by_org_by_repo_content_response_500 import GetByOrgByRepoContentResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org: str,
    repo: str,
    *,
    oid: str | Unset = UNSET,
    path: str | Unset = UNSET,
    depth: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["oid"] = oid

    params["path"] = path

    params["depth"] = depth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/{repo}/content".format(
            org=quote(str(org), safe=""),
            repo=quote(str(repo), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetByOrgByRepoContentResponse200Type0
    | GetByOrgByRepoContentResponse200Type1
    | GetByOrgByRepoContentResponse200Type2
    | GetByOrgByRepoContentResponse400
    | GetByOrgByRepoContentResponse401
    | GetByOrgByRepoContentResponse403
    | GetByOrgByRepoContentResponse404
    | GetByOrgByRepoContentResponse406
    | GetByOrgByRepoContentResponse409
    | GetByOrgByRepoContentResponse500
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            GetByOrgByRepoContentResponse200Type0
            | GetByOrgByRepoContentResponse200Type1
            | GetByOrgByRepoContentResponse200Type2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = GetByOrgByRepoContentResponse200Type0.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = GetByOrgByRepoContentResponse200Type1.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = GetByOrgByRepoContentResponse200Type2.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgByRepoContentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgByRepoContentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgByRepoContentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgByRepoContentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgByRepoContentResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgByRepoContentResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgByRepoContentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetByOrgByRepoContentResponse200Type0
    | GetByOrgByRepoContentResponse200Type1
    | GetByOrgByRepoContentResponse200Type2
    | GetByOrgByRepoContentResponse400
    | GetByOrgByRepoContentResponse401
    | GetByOrgByRepoContentResponse403
    | GetByOrgByRepoContentResponse404
    | GetByOrgByRepoContentResponse406
    | GetByOrgByRepoContentResponse409
    | GetByOrgByRepoContentResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    oid: str | Unset = UNSET,
    path: str | Unset = UNSET,
    depth: int | Unset = UNSET,
) -> Response[
    GetByOrgByRepoContentResponse200Type0
    | GetByOrgByRepoContentResponse200Type1
    | GetByOrgByRepoContentResponse200Type2
    | GetByOrgByRepoContentResponse400
    | GetByOrgByRepoContentResponse401
    | GetByOrgByRepoContentResponse403
    | GetByOrgByRepoContentResponse404
    | GetByOrgByRepoContentResponse406
    | GetByOrgByRepoContentResponse409
    | GetByOrgByRepoContentResponse500
]:
    """Get content

     Get file content or directory listing at a path. Use Accept: application/json for the JSON union
    response, or Accept: application/octet-stream for raw file bytes. Directory + octet-stream requests
    return 406 Not Acceptable.

    Args:
        org (str):
        repo (str):
        oid (str | Unset):
        path (str | Unset):
        depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoContentResponse200Type0 | GetByOrgByRepoContentResponse200Type1 | GetByOrgByRepoContentResponse200Type2 | GetByOrgByRepoContentResponse400 | GetByOrgByRepoContentResponse401 | GetByOrgByRepoContentResponse403 | GetByOrgByRepoContentResponse404 | GetByOrgByRepoContentResponse406 | GetByOrgByRepoContentResponse409 | GetByOrgByRepoContentResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        oid=oid,
        path=path,
        depth=depth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    oid: str | Unset = UNSET,
    path: str | Unset = UNSET,
    depth: int | Unset = UNSET,
) -> (
    GetByOrgByRepoContentResponse200Type0
    | GetByOrgByRepoContentResponse200Type1
    | GetByOrgByRepoContentResponse200Type2
    | GetByOrgByRepoContentResponse400
    | GetByOrgByRepoContentResponse401
    | GetByOrgByRepoContentResponse403
    | GetByOrgByRepoContentResponse404
    | GetByOrgByRepoContentResponse406
    | GetByOrgByRepoContentResponse409
    | GetByOrgByRepoContentResponse500
    | None
):
    """Get content

     Get file content or directory listing at a path. Use Accept: application/json for the JSON union
    response, or Accept: application/octet-stream for raw file bytes. Directory + octet-stream requests
    return 406 Not Acceptable.

    Args:
        org (str):
        repo (str):
        oid (str | Unset):
        path (str | Unset):
        depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoContentResponse200Type0 | GetByOrgByRepoContentResponse200Type1 | GetByOrgByRepoContentResponse200Type2 | GetByOrgByRepoContentResponse400 | GetByOrgByRepoContentResponse401 | GetByOrgByRepoContentResponse403 | GetByOrgByRepoContentResponse404 | GetByOrgByRepoContentResponse406 | GetByOrgByRepoContentResponse409 | GetByOrgByRepoContentResponse500
    """

    return sync_detailed(
        org=org,
        repo=repo,
        client=client,
        oid=oid,
        path=path,
        depth=depth,
    ).parsed


async def asyncio_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    oid: str | Unset = UNSET,
    path: str | Unset = UNSET,
    depth: int | Unset = UNSET,
) -> Response[
    GetByOrgByRepoContentResponse200Type0
    | GetByOrgByRepoContentResponse200Type1
    | GetByOrgByRepoContentResponse200Type2
    | GetByOrgByRepoContentResponse400
    | GetByOrgByRepoContentResponse401
    | GetByOrgByRepoContentResponse403
    | GetByOrgByRepoContentResponse404
    | GetByOrgByRepoContentResponse406
    | GetByOrgByRepoContentResponse409
    | GetByOrgByRepoContentResponse500
]:
    """Get content

     Get file content or directory listing at a path. Use Accept: application/json for the JSON union
    response, or Accept: application/octet-stream for raw file bytes. Directory + octet-stream requests
    return 406 Not Acceptable.

    Args:
        org (str):
        repo (str):
        oid (str | Unset):
        path (str | Unset):
        depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoContentResponse200Type0 | GetByOrgByRepoContentResponse200Type1 | GetByOrgByRepoContentResponse200Type2 | GetByOrgByRepoContentResponse400 | GetByOrgByRepoContentResponse401 | GetByOrgByRepoContentResponse403 | GetByOrgByRepoContentResponse404 | GetByOrgByRepoContentResponse406 | GetByOrgByRepoContentResponse409 | GetByOrgByRepoContentResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        oid=oid,
        path=path,
        depth=depth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    oid: str | Unset = UNSET,
    path: str | Unset = UNSET,
    depth: int | Unset = UNSET,
) -> (
    GetByOrgByRepoContentResponse200Type0
    | GetByOrgByRepoContentResponse200Type1
    | GetByOrgByRepoContentResponse200Type2
    | GetByOrgByRepoContentResponse400
    | GetByOrgByRepoContentResponse401
    | GetByOrgByRepoContentResponse403
    | GetByOrgByRepoContentResponse404
    | GetByOrgByRepoContentResponse406
    | GetByOrgByRepoContentResponse409
    | GetByOrgByRepoContentResponse500
    | None
):
    """Get content

     Get file content or directory listing at a path. Use Accept: application/json for the JSON union
    response, or Accept: application/octet-stream for raw file bytes. Directory + octet-stream requests
    return 406 Not Acceptable.

    Args:
        org (str):
        repo (str):
        oid (str | Unset):
        path (str | Unset):
        depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoContentResponse200Type0 | GetByOrgByRepoContentResponse200Type1 | GetByOrgByRepoContentResponse200Type2 | GetByOrgByRepoContentResponse400 | GetByOrgByRepoContentResponse401 | GetByOrgByRepoContentResponse403 | GetByOrgByRepoContentResponse404 | GetByOrgByRepoContentResponse406 | GetByOrgByRepoContentResponse409 | GetByOrgByRepoContentResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            client=client,
            oid=oid,
            path=path,
            depth=depth,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_by_org_by_repo_body import PatchByOrgByRepoBody
from ...models.patch_by_org_by_repo_response_200 import PatchByOrgByRepoResponse200
from ...models.patch_by_org_by_repo_response_400 import PatchByOrgByRepoResponse400
from ...models.patch_by_org_by_repo_response_401 import PatchByOrgByRepoResponse401
from ...models.patch_by_org_by_repo_response_403 import PatchByOrgByRepoResponse403
from ...models.patch_by_org_by_repo_response_404 import PatchByOrgByRepoResponse404
from ...models.patch_by_org_by_repo_response_406 import PatchByOrgByRepoResponse406
from ...models.patch_by_org_by_repo_response_409 import PatchByOrgByRepoResponse409
from ...models.patch_by_org_by_repo_response_500 import PatchByOrgByRepoResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org: str,
    repo: str,
    *,
    body: PatchByOrgByRepoBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/{org}/{repo}".format(
            org=quote(str(org), safe=""),
            repo=quote(str(repo), safe=""),
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
    PatchByOrgByRepoResponse200
    | PatchByOrgByRepoResponse400
    | PatchByOrgByRepoResponse401
    | PatchByOrgByRepoResponse403
    | PatchByOrgByRepoResponse404
    | PatchByOrgByRepoResponse406
    | PatchByOrgByRepoResponse409
    | PatchByOrgByRepoResponse500
    | None
):
    if response.status_code == 200:
        response_200 = PatchByOrgByRepoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PatchByOrgByRepoResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PatchByOrgByRepoResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PatchByOrgByRepoResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PatchByOrgByRepoResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = PatchByOrgByRepoResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PatchByOrgByRepoResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = PatchByOrgByRepoResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PatchByOrgByRepoResponse200
    | PatchByOrgByRepoResponse400
    | PatchByOrgByRepoResponse401
    | PatchByOrgByRepoResponse403
    | PatchByOrgByRepoResponse404
    | PatchByOrgByRepoResponse406
    | PatchByOrgByRepoResponse409
    | PatchByOrgByRepoResponse500
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
    body: PatchByOrgByRepoBody | Unset = UNSET,
) -> Response[
    PatchByOrgByRepoResponse200
    | PatchByOrgByRepoResponse400
    | PatchByOrgByRepoResponse401
    | PatchByOrgByRepoResponse403
    | PatchByOrgByRepoResponse404
    | PatchByOrgByRepoResponse406
    | PatchByOrgByRepoResponse409
    | PatchByOrgByRepoResponse500
]:
    """Update repository

     Update repository name or upstream configuration

    Args:
        org (str):
        repo (str):
        body (PatchByOrgByRepoBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchByOrgByRepoResponse200 | PatchByOrgByRepoResponse400 | PatchByOrgByRepoResponse401 | PatchByOrgByRepoResponse403 | PatchByOrgByRepoResponse404 | PatchByOrgByRepoResponse406 | PatchByOrgByRepoResponse409 | PatchByOrgByRepoResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        body=body,
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
    body: PatchByOrgByRepoBody | Unset = UNSET,
) -> (
    PatchByOrgByRepoResponse200
    | PatchByOrgByRepoResponse400
    | PatchByOrgByRepoResponse401
    | PatchByOrgByRepoResponse403
    | PatchByOrgByRepoResponse404
    | PatchByOrgByRepoResponse406
    | PatchByOrgByRepoResponse409
    | PatchByOrgByRepoResponse500
    | None
):
    """Update repository

     Update repository name or upstream configuration

    Args:
        org (str):
        repo (str):
        body (PatchByOrgByRepoBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchByOrgByRepoResponse200 | PatchByOrgByRepoResponse400 | PatchByOrgByRepoResponse401 | PatchByOrgByRepoResponse403 | PatchByOrgByRepoResponse404 | PatchByOrgByRepoResponse406 | PatchByOrgByRepoResponse409 | PatchByOrgByRepoResponse500
    """

    return sync_detailed(
        org=org,
        repo=repo,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchByOrgByRepoBody | Unset = UNSET,
) -> Response[
    PatchByOrgByRepoResponse200
    | PatchByOrgByRepoResponse400
    | PatchByOrgByRepoResponse401
    | PatchByOrgByRepoResponse403
    | PatchByOrgByRepoResponse404
    | PatchByOrgByRepoResponse406
    | PatchByOrgByRepoResponse409
    | PatchByOrgByRepoResponse500
]:
    """Update repository

     Update repository name or upstream configuration

    Args:
        org (str):
        repo (str):
        body (PatchByOrgByRepoBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchByOrgByRepoResponse200 | PatchByOrgByRepoResponse400 | PatchByOrgByRepoResponse401 | PatchByOrgByRepoResponse403 | PatchByOrgByRepoResponse404 | PatchByOrgByRepoResponse406 | PatchByOrgByRepoResponse409 | PatchByOrgByRepoResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchByOrgByRepoBody | Unset = UNSET,
) -> (
    PatchByOrgByRepoResponse200
    | PatchByOrgByRepoResponse400
    | PatchByOrgByRepoResponse401
    | PatchByOrgByRepoResponse403
    | PatchByOrgByRepoResponse404
    | PatchByOrgByRepoResponse406
    | PatchByOrgByRepoResponse409
    | PatchByOrgByRepoResponse500
    | None
):
    """Update repository

     Update repository name or upstream configuration

    Args:
        org (str):
        repo (str):
        body (PatchByOrgByRepoBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchByOrgByRepoResponse200 | PatchByOrgByRepoResponse400 | PatchByOrgByRepoResponse401 | PatchByOrgByRepoResponse403 | PatchByOrgByRepoResponse404 | PatchByOrgByRepoResponse406 | PatchByOrgByRepoResponse409 | PatchByOrgByRepoResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            client=client,
            body=body,
        )
    ).parsed

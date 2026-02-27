from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_by_org_by_repo_branches_body import PostByOrgByRepoBranchesBody
from ...models.post_by_org_by_repo_branches_response_201 import PostByOrgByRepoBranchesResponse201
from ...models.post_by_org_by_repo_branches_response_400 import PostByOrgByRepoBranchesResponse400
from ...models.post_by_org_by_repo_branches_response_401 import PostByOrgByRepoBranchesResponse401
from ...models.post_by_org_by_repo_branches_response_403 import PostByOrgByRepoBranchesResponse403
from ...models.post_by_org_by_repo_branches_response_404 import PostByOrgByRepoBranchesResponse404
from ...models.post_by_org_by_repo_branches_response_406 import PostByOrgByRepoBranchesResponse406
from ...models.post_by_org_by_repo_branches_response_409 import PostByOrgByRepoBranchesResponse409
from ...models.post_by_org_by_repo_branches_response_500 import PostByOrgByRepoBranchesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org: str,
    repo: str,
    *,
    body: PostByOrgByRepoBranchesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/{repo}/branches".format(
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
    PostByOrgByRepoBranchesResponse201
    | PostByOrgByRepoBranchesResponse400
    | PostByOrgByRepoBranchesResponse401
    | PostByOrgByRepoBranchesResponse403
    | PostByOrgByRepoBranchesResponse404
    | PostByOrgByRepoBranchesResponse406
    | PostByOrgByRepoBranchesResponse409
    | PostByOrgByRepoBranchesResponse500
    | None
):
    if response.status_code == 201:
        response_201 = PostByOrgByRepoBranchesResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PostByOrgByRepoBranchesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgByRepoBranchesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgByRepoBranchesResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgByRepoBranchesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgByRepoBranchesResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgByRepoBranchesResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgByRepoBranchesResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostByOrgByRepoBranchesResponse201
    | PostByOrgByRepoBranchesResponse400
    | PostByOrgByRepoBranchesResponse401
    | PostByOrgByRepoBranchesResponse403
    | PostByOrgByRepoBranchesResponse404
    | PostByOrgByRepoBranchesResponse406
    | PostByOrgByRepoBranchesResponse409
    | PostByOrgByRepoBranchesResponse500
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
    body: PostByOrgByRepoBranchesBody | Unset = UNSET,
) -> Response[
    PostByOrgByRepoBranchesResponse201
    | PostByOrgByRepoBranchesResponse400
    | PostByOrgByRepoBranchesResponse401
    | PostByOrgByRepoBranchesResponse403
    | PostByOrgByRepoBranchesResponse404
    | PostByOrgByRepoBranchesResponse406
    | PostByOrgByRepoBranchesResponse409
    | PostByOrgByRepoBranchesResponse500
]:
    """Create branch

     Create a new branch from an existing ref

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoBranchesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgByRepoBranchesResponse201 | PostByOrgByRepoBranchesResponse400 | PostByOrgByRepoBranchesResponse401 | PostByOrgByRepoBranchesResponse403 | PostByOrgByRepoBranchesResponse404 | PostByOrgByRepoBranchesResponse406 | PostByOrgByRepoBranchesResponse409 | PostByOrgByRepoBranchesResponse500]
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
    body: PostByOrgByRepoBranchesBody | Unset = UNSET,
) -> (
    PostByOrgByRepoBranchesResponse201
    | PostByOrgByRepoBranchesResponse400
    | PostByOrgByRepoBranchesResponse401
    | PostByOrgByRepoBranchesResponse403
    | PostByOrgByRepoBranchesResponse404
    | PostByOrgByRepoBranchesResponse406
    | PostByOrgByRepoBranchesResponse409
    | PostByOrgByRepoBranchesResponse500
    | None
):
    """Create branch

     Create a new branch from an existing ref

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoBranchesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgByRepoBranchesResponse201 | PostByOrgByRepoBranchesResponse400 | PostByOrgByRepoBranchesResponse401 | PostByOrgByRepoBranchesResponse403 | PostByOrgByRepoBranchesResponse404 | PostByOrgByRepoBranchesResponse406 | PostByOrgByRepoBranchesResponse409 | PostByOrgByRepoBranchesResponse500
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
    body: PostByOrgByRepoBranchesBody | Unset = UNSET,
) -> Response[
    PostByOrgByRepoBranchesResponse201
    | PostByOrgByRepoBranchesResponse400
    | PostByOrgByRepoBranchesResponse401
    | PostByOrgByRepoBranchesResponse403
    | PostByOrgByRepoBranchesResponse404
    | PostByOrgByRepoBranchesResponse406
    | PostByOrgByRepoBranchesResponse409
    | PostByOrgByRepoBranchesResponse500
]:
    """Create branch

     Create a new branch from an existing ref

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoBranchesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgByRepoBranchesResponse201 | PostByOrgByRepoBranchesResponse400 | PostByOrgByRepoBranchesResponse401 | PostByOrgByRepoBranchesResponse403 | PostByOrgByRepoBranchesResponse404 | PostByOrgByRepoBranchesResponse406 | PostByOrgByRepoBranchesResponse409 | PostByOrgByRepoBranchesResponse500]
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
    body: PostByOrgByRepoBranchesBody | Unset = UNSET,
) -> (
    PostByOrgByRepoBranchesResponse201
    | PostByOrgByRepoBranchesResponse400
    | PostByOrgByRepoBranchesResponse401
    | PostByOrgByRepoBranchesResponse403
    | PostByOrgByRepoBranchesResponse404
    | PostByOrgByRepoBranchesResponse406
    | PostByOrgByRepoBranchesResponse409
    | PostByOrgByRepoBranchesResponse500
    | None
):
    """Create branch

     Create a new branch from an existing ref

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoBranchesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgByRepoBranchesResponse201 | PostByOrgByRepoBranchesResponse400 | PostByOrgByRepoBranchesResponse401 | PostByOrgByRepoBranchesResponse403 | PostByOrgByRepoBranchesResponse404 | PostByOrgByRepoBranchesResponse406 | PostByOrgByRepoBranchesResponse409 | PostByOrgByRepoBranchesResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            client=client,
            body=body,
        )
    ).parsed

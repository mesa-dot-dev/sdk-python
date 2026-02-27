from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_by_org_by_repo_branches_by_branch_response_200 import DeleteByOrgByRepoBranchesByBranchResponse200
from ...models.delete_by_org_by_repo_branches_by_branch_response_400 import DeleteByOrgByRepoBranchesByBranchResponse400
from ...models.delete_by_org_by_repo_branches_by_branch_response_401 import DeleteByOrgByRepoBranchesByBranchResponse401
from ...models.delete_by_org_by_repo_branches_by_branch_response_403 import DeleteByOrgByRepoBranchesByBranchResponse403
from ...models.delete_by_org_by_repo_branches_by_branch_response_404 import DeleteByOrgByRepoBranchesByBranchResponse404
from ...models.delete_by_org_by_repo_branches_by_branch_response_406 import DeleteByOrgByRepoBranchesByBranchResponse406
from ...models.delete_by_org_by_repo_branches_by_branch_response_409 import DeleteByOrgByRepoBranchesByBranchResponse409
from ...models.delete_by_org_by_repo_branches_by_branch_response_500 import DeleteByOrgByRepoBranchesByBranchResponse500
from ...types import Response


def _get_kwargs(
    org: str,
    repo: str,
    branch: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{org}/{repo}/branches/{branch}".format(
            org=quote(str(org), safe=""),
            repo=quote(str(repo), safe=""),
            branch=quote(str(branch), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteByOrgByRepoBranchesByBranchResponse200
    | DeleteByOrgByRepoBranchesByBranchResponse400
    | DeleteByOrgByRepoBranchesByBranchResponse401
    | DeleteByOrgByRepoBranchesByBranchResponse403
    | DeleteByOrgByRepoBranchesByBranchResponse404
    | DeleteByOrgByRepoBranchesByBranchResponse406
    | DeleteByOrgByRepoBranchesByBranchResponse409
    | DeleteByOrgByRepoBranchesByBranchResponse500
    | None
):
    if response.status_code == 200:
        response_200 = DeleteByOrgByRepoBranchesByBranchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteByOrgByRepoBranchesByBranchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteByOrgByRepoBranchesByBranchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteByOrgByRepoBranchesByBranchResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteByOrgByRepoBranchesByBranchResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = DeleteByOrgByRepoBranchesByBranchResponse406.from_dict(response.json())

        return response_406

    if response.status_code == 409:
        response_409 = DeleteByOrgByRepoBranchesByBranchResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 500:
        response_500 = DeleteByOrgByRepoBranchesByBranchResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteByOrgByRepoBranchesByBranchResponse200
    | DeleteByOrgByRepoBranchesByBranchResponse400
    | DeleteByOrgByRepoBranchesByBranchResponse401
    | DeleteByOrgByRepoBranchesByBranchResponse403
    | DeleteByOrgByRepoBranchesByBranchResponse404
    | DeleteByOrgByRepoBranchesByBranchResponse406
    | DeleteByOrgByRepoBranchesByBranchResponse409
    | DeleteByOrgByRepoBranchesByBranchResponse500
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
    branch: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteByOrgByRepoBranchesByBranchResponse200
    | DeleteByOrgByRepoBranchesByBranchResponse400
    | DeleteByOrgByRepoBranchesByBranchResponse401
    | DeleteByOrgByRepoBranchesByBranchResponse403
    | DeleteByOrgByRepoBranchesByBranchResponse404
    | DeleteByOrgByRepoBranchesByBranchResponse406
    | DeleteByOrgByRepoBranchesByBranchResponse409
    | DeleteByOrgByRepoBranchesByBranchResponse500
]:
    """Delete branch

     Delete a branch from a repository

    Args:
        org (str):
        repo (str):
        branch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoBranchesByBranchResponse200 | DeleteByOrgByRepoBranchesByBranchResponse400 | DeleteByOrgByRepoBranchesByBranchResponse401 | DeleteByOrgByRepoBranchesByBranchResponse403 | DeleteByOrgByRepoBranchesByBranchResponse404 | DeleteByOrgByRepoBranchesByBranchResponse406 | DeleteByOrgByRepoBranchesByBranchResponse409 | DeleteByOrgByRepoBranchesByBranchResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        branch=branch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    org: str,
    repo: str,
    branch: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteByOrgByRepoBranchesByBranchResponse200
    | DeleteByOrgByRepoBranchesByBranchResponse400
    | DeleteByOrgByRepoBranchesByBranchResponse401
    | DeleteByOrgByRepoBranchesByBranchResponse403
    | DeleteByOrgByRepoBranchesByBranchResponse404
    | DeleteByOrgByRepoBranchesByBranchResponse406
    | DeleteByOrgByRepoBranchesByBranchResponse409
    | DeleteByOrgByRepoBranchesByBranchResponse500
    | None
):
    """Delete branch

     Delete a branch from a repository

    Args:
        org (str):
        repo (str):
        branch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoBranchesByBranchResponse200 | DeleteByOrgByRepoBranchesByBranchResponse400 | DeleteByOrgByRepoBranchesByBranchResponse401 | DeleteByOrgByRepoBranchesByBranchResponse403 | DeleteByOrgByRepoBranchesByBranchResponse404 | DeleteByOrgByRepoBranchesByBranchResponse406 | DeleteByOrgByRepoBranchesByBranchResponse409 | DeleteByOrgByRepoBranchesByBranchResponse500
    """

    return sync_detailed(
        org=org,
        repo=repo,
        branch=branch,
        client=client,
    ).parsed


async def asyncio_detailed(
    org: str,
    repo: str,
    branch: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    DeleteByOrgByRepoBranchesByBranchResponse200
    | DeleteByOrgByRepoBranchesByBranchResponse400
    | DeleteByOrgByRepoBranchesByBranchResponse401
    | DeleteByOrgByRepoBranchesByBranchResponse403
    | DeleteByOrgByRepoBranchesByBranchResponse404
    | DeleteByOrgByRepoBranchesByBranchResponse406
    | DeleteByOrgByRepoBranchesByBranchResponse409
    | DeleteByOrgByRepoBranchesByBranchResponse500
]:
    """Delete branch

     Delete a branch from a repository

    Args:
        org (str):
        repo (str):
        branch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoBranchesByBranchResponse200 | DeleteByOrgByRepoBranchesByBranchResponse400 | DeleteByOrgByRepoBranchesByBranchResponse401 | DeleteByOrgByRepoBranchesByBranchResponse403 | DeleteByOrgByRepoBranchesByBranchResponse404 | DeleteByOrgByRepoBranchesByBranchResponse406 | DeleteByOrgByRepoBranchesByBranchResponse409 | DeleteByOrgByRepoBranchesByBranchResponse500]
    """

    kwargs = _get_kwargs(
        org=org,
        repo=repo,
        branch=branch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    org: str,
    repo: str,
    branch: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    DeleteByOrgByRepoBranchesByBranchResponse200
    | DeleteByOrgByRepoBranchesByBranchResponse400
    | DeleteByOrgByRepoBranchesByBranchResponse401
    | DeleteByOrgByRepoBranchesByBranchResponse403
    | DeleteByOrgByRepoBranchesByBranchResponse404
    | DeleteByOrgByRepoBranchesByBranchResponse406
    | DeleteByOrgByRepoBranchesByBranchResponse409
    | DeleteByOrgByRepoBranchesByBranchResponse500
    | None
):
    """Delete branch

     Delete a branch from a repository

    Args:
        org (str):
        repo (str):
        branch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoBranchesByBranchResponse200 | DeleteByOrgByRepoBranchesByBranchResponse400 | DeleteByOrgByRepoBranchesByBranchResponse401 | DeleteByOrgByRepoBranchesByBranchResponse403 | DeleteByOrgByRepoBranchesByBranchResponse404 | DeleteByOrgByRepoBranchesByBranchResponse406 | DeleteByOrgByRepoBranchesByBranchResponse409 | DeleteByOrgByRepoBranchesByBranchResponse500
    """

    return (
        await asyncio_detailed(
            org=org,
            repo=repo,
            branch=branch,
            client=client,
        )
    ).parsed

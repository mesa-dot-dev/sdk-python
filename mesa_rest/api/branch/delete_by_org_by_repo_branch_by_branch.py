from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_by_org_by_repo_branch_by_branch_response_200 import DeleteByOrgByRepoBranchByBranchResponse200
from ...models.delete_by_org_by_repo_branch_by_branch_response_400 import DeleteByOrgByRepoBranchByBranchResponse400
from ...models.delete_by_org_by_repo_branch_by_branch_response_401 import DeleteByOrgByRepoBranchByBranchResponse401
from ...models.delete_by_org_by_repo_branch_by_branch_response_403 import DeleteByOrgByRepoBranchByBranchResponse403
from ...models.delete_by_org_by_repo_branch_by_branch_response_404 import DeleteByOrgByRepoBranchByBranchResponse404
from ...models.delete_by_org_by_repo_branch_by_branch_response_406 import DeleteByOrgByRepoBranchByBranchResponse406
from ...models.delete_by_org_by_repo_branch_by_branch_response_409 import DeleteByOrgByRepoBranchByBranchResponse409
from ...models.delete_by_org_by_repo_branch_by_branch_response_500 import DeleteByOrgByRepoBranchByBranchResponse500
from typing import cast



def _get_kwargs(
    org: str,
    repo: str,
    branch: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/{org}/{repo}/branch/{branch}".format(org=quote(str(org), safe=""),repo=quote(str(repo), safe=""),branch=quote(str(branch), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteByOrgByRepoBranchByBranchResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteByOrgByRepoBranchByBranchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteByOrgByRepoBranchByBranchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteByOrgByRepoBranchByBranchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteByOrgByRepoBranchByBranchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = DeleteByOrgByRepoBranchByBranchResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = DeleteByOrgByRepoBranchByBranchResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = DeleteByOrgByRepoBranchByBranchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500]:
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

) -> Response[DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500]:
    """ Delete branch

     Delete a branch from a repository

    Args:
        org (str):
        repo (str):
        branch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500]
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

) -> DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500 | None:
    """ Delete branch

     Delete a branch from a repository

    Args:
        org (str):
        repo (str):
        branch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500
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

) -> Response[DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500]:
    """ Delete branch

     Delete a branch from a repository

    Args:
        org (str):
        repo (str):
        branch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
branch=branch,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    repo: str,
    branch: str,
    *,
    client: AuthenticatedClient | Client,

) -> DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500 | None:
    """ Delete branch

     Delete a branch from a repository

    Args:
        org (str):
        repo (str):
        branch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByOrgByRepoBranchByBranchResponse200 | DeleteByOrgByRepoBranchByBranchResponse400 | DeleteByOrgByRepoBranchByBranchResponse401 | DeleteByOrgByRepoBranchByBranchResponse403 | DeleteByOrgByRepoBranchByBranchResponse404 | DeleteByOrgByRepoBranchByBranchResponse406 | DeleteByOrgByRepoBranchByBranchResponse409 | DeleteByOrgByRepoBranchByBranchResponse500
     """


    return (await asyncio_detailed(
        org=org,
repo=repo,
branch=branch,
client=client,

    )).parsed

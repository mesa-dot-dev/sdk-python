from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_by_org_by_repo_branch_body import PostByOrgByRepoBranchBody
from ...models.post_by_org_by_repo_branch_response_201 import PostByOrgByRepoBranchResponse201
from ...models.post_by_org_by_repo_branch_response_400 import PostByOrgByRepoBranchResponse400
from ...models.post_by_org_by_repo_branch_response_401 import PostByOrgByRepoBranchResponse401
from ...models.post_by_org_by_repo_branch_response_403 import PostByOrgByRepoBranchResponse403
from ...models.post_by_org_by_repo_branch_response_404 import PostByOrgByRepoBranchResponse404
from ...models.post_by_org_by_repo_branch_response_406 import PostByOrgByRepoBranchResponse406
from ...models.post_by_org_by_repo_branch_response_409 import PostByOrgByRepoBranchResponse409
from ...models.post_by_org_by_repo_branch_response_500 import PostByOrgByRepoBranchResponse500
from typing import cast



def _get_kwargs(
    org: str,
    repo: str,
    *,
    body: PostByOrgByRepoBranchBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/{repo}/branch".format(org=quote(str(org), safe=""),repo=quote(str(repo), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500 | None:
    if response.status_code == 201:
        response_201 = PostByOrgByRepoBranchResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostByOrgByRepoBranchResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgByRepoBranchResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgByRepoBranchResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgByRepoBranchResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgByRepoBranchResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgByRepoBranchResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgByRepoBranchResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500]:
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
    body: PostByOrgByRepoBranchBody,

) -> Response[PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500]:
    """ Create branch

     Create a new branch from an existing ref

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoBranchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500]
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
    body: PostByOrgByRepoBranchBody,

) -> PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500 | None:
    """ Create branch

     Create a new branch from an existing ref

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoBranchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500
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
    body: PostByOrgByRepoBranchBody,

) -> Response[PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500]:
    """ Create branch

     Create a new branch from an existing ref

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoBranchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostByOrgByRepoBranchBody,

) -> PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500 | None:
    """ Create branch

     Create a new branch from an existing ref

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoBranchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgByRepoBranchResponse201 | PostByOrgByRepoBranchResponse400 | PostByOrgByRepoBranchResponse401 | PostByOrgByRepoBranchResponse403 | PostByOrgByRepoBranchResponse404 | PostByOrgByRepoBranchResponse406 | PostByOrgByRepoBranchResponse409 | PostByOrgByRepoBranchResponse500
     """


    return (await asyncio_detailed(
        org=org,
repo=repo,
client=client,
body=body,

    )).parsed

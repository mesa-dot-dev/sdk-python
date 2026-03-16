from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_by_org_by_repo_commit_body import PostByOrgByRepoCommitBody
from ...models.post_by_org_by_repo_commit_response_201 import PostByOrgByRepoCommitResponse201
from ...models.post_by_org_by_repo_commit_response_400 import PostByOrgByRepoCommitResponse400
from ...models.post_by_org_by_repo_commit_response_401 import PostByOrgByRepoCommitResponse401
from ...models.post_by_org_by_repo_commit_response_403 import PostByOrgByRepoCommitResponse403
from ...models.post_by_org_by_repo_commit_response_404 import PostByOrgByRepoCommitResponse404
from ...models.post_by_org_by_repo_commit_response_406 import PostByOrgByRepoCommitResponse406
from ...models.post_by_org_by_repo_commit_response_409 import PostByOrgByRepoCommitResponse409
from ...models.post_by_org_by_repo_commit_response_500 import PostByOrgByRepoCommitResponse500
from typing import cast



def _get_kwargs(
    org: str,
    repo: str,
    *,
    body: PostByOrgByRepoCommitBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/{org}/{repo}/commit".format(org=quote(str(org), safe=""),repo=quote(str(repo), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500 | None:
    if response.status_code == 201:
        response_201 = PostByOrgByRepoCommitResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostByOrgByRepoCommitResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostByOrgByRepoCommitResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostByOrgByRepoCommitResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostByOrgByRepoCommitResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = PostByOrgByRepoCommitResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = PostByOrgByRepoCommitResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = PostByOrgByRepoCommitResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500]:
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
    body: PostByOrgByRepoCommitBody,

) -> Response[PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500]:
    """ Create commit

     Create a new commit on a branch with file changes

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoCommitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500]
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
    body: PostByOrgByRepoCommitBody,

) -> PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500 | None:
    """ Create commit

     Create a new commit on a branch with file changes

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoCommitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500
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
    body: PostByOrgByRepoCommitBody,

) -> Response[PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500]:
    """ Create commit

     Create a new commit on a branch with file changes

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoCommitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500]
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
    body: PostByOrgByRepoCommitBody,

) -> PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500 | None:
    """ Create commit

     Create a new commit on a branch with file changes

    Args:
        org (str):
        repo (str):
        body (PostByOrgByRepoCommitBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostByOrgByRepoCommitResponse201 | PostByOrgByRepoCommitResponse400 | PostByOrgByRepoCommitResponse401 | PostByOrgByRepoCommitResponse403 | PostByOrgByRepoCommitResponse404 | PostByOrgByRepoCommitResponse406 | PostByOrgByRepoCommitResponse409 | PostByOrgByRepoCommitResponse500
     """


    return (await asyncio_detailed(
        org=org,
repo=repo,
client=client,
body=body,

    )).parsed

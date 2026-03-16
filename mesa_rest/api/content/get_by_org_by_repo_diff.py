from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_by_org_by_repo_diff_response_200 import GetByOrgByRepoDiffResponse200
from ...models.get_by_org_by_repo_diff_response_400 import GetByOrgByRepoDiffResponse400
from ...models.get_by_org_by_repo_diff_response_401 import GetByOrgByRepoDiffResponse401
from ...models.get_by_org_by_repo_diff_response_403 import GetByOrgByRepoDiffResponse403
from ...models.get_by_org_by_repo_diff_response_404 import GetByOrgByRepoDiffResponse404
from ...models.get_by_org_by_repo_diff_response_406 import GetByOrgByRepoDiffResponse406
from ...models.get_by_org_by_repo_diff_response_409 import GetByOrgByRepoDiffResponse409
from ...models.get_by_org_by_repo_diff_response_500 import GetByOrgByRepoDiffResponse500
from typing import cast



def _get_kwargs(
    org: str,
    repo: str,
    *,
    base: str,
    head: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["base"] = base

    params["head"] = head


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/{org}/{repo}/diff".format(org=quote(str(org), safe=""),repo=quote(str(repo), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500 | None:
    if response.status_code == 200:
        response_200 = GetByOrgByRepoDiffResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetByOrgByRepoDiffResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetByOrgByRepoDiffResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetByOrgByRepoDiffResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetByOrgByRepoDiffResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 406:
        response_406 = GetByOrgByRepoDiffResponse406.from_dict(response.json())



        return response_406

    if response.status_code == 409:
        response_409 = GetByOrgByRepoDiffResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = GetByOrgByRepoDiffResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500]:
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
    base: str,
    head: str,

) -> Response[GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500]:
    """ Get diff

     Retrieve the diff between two commit OIDs

    Args:
        org (str):
        repo (str):
        base (str):
        head (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
base=base,
head=head,

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
    base: str,
    head: str,

) -> GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500 | None:
    """ Get diff

     Retrieve the diff between two commit OIDs

    Args:
        org (str):
        repo (str):
        base (str):
        head (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500
     """


    return sync_detailed(
        org=org,
repo=repo,
client=client,
base=base,
head=head,

    ).parsed

async def asyncio_detailed(
    org: str,
    repo: str,
    *,
    client: AuthenticatedClient | Client,
    base: str,
    head: str,

) -> Response[GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500]:
    """ Get diff

     Retrieve the diff between two commit OIDs

    Args:
        org (str):
        repo (str):
        base (str):
        head (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500]
     """


    kwargs = _get_kwargs(
        org=org,
repo=repo,
base=base,
head=head,

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
    base: str,
    head: str,

) -> GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500 | None:
    """ Get diff

     Retrieve the diff between two commit OIDs

    Args:
        org (str):
        repo (str):
        base (str):
        head (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetByOrgByRepoDiffResponse200 | GetByOrgByRepoDiffResponse400 | GetByOrgByRepoDiffResponse401 | GetByOrgByRepoDiffResponse403 | GetByOrgByRepoDiffResponse404 | GetByOrgByRepoDiffResponse406 | GetByOrgByRepoDiffResponse409 | GetByOrgByRepoDiffResponse500
     """


    return (await asyncio_detailed(
        org=org,
repo=repo,
client=client,
base=base,
head=head,

    )).parsed

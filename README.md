# mesa-sdk

Python SDK for the [Mesa](https://mesa.dev) API.

Generated from the OpenAPI specification using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

## Installation

```bash
pip install mesa-sdk
```

## Usage

```python
from mesa_sdk import Client

client = Client(
    base_url="https://depot.mesa.dev/api/v1",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)
```

## License

Apache-2.0

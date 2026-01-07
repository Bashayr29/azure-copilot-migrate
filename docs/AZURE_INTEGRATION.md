# Azure Integration Guide

## Overview

This guide explains how to integrate Azure services with GitHub Copilot assistance.

## Azure Services

### Supported Services

This test repository demonstrates patterns for:
- Azure Storage
- Azure Functions
- Azure App Service
- Azure Key Vault
- Azure SQL Database

## Configuration

### Environment Variables

Create a `.env` file (not committed to repo):

```bash
AZURE_SUBSCRIPTION_ID=your-subscription-id
AZURE_RESOURCE_GROUP=your-resource-group
AZURE_REGION=eastus
```

### Authentication

Using Azure CLI:
```bash
az login
az account set --subscription <subscription-id>
```

Using Service Principal:
```bash
export AZURE_CLIENT_ID=<client-id>
export AZURE_CLIENT_SECRET=<client-secret>
export AZURE_TENANT_ID=<tenant-id>
```

## Code Examples

### Azure Storage

```python
from azure.storage.blob import BlobServiceClient

# Copilot can help generate Azure SDK code
connection_string = "your-connection-string"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
```

### Azure Key Vault

```python
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# Copilot understands Azure patterns
credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://your-vault.vault.azure.net/", credential=credential)
```

## Best Practices

1. **Use Managed Identity**: When running in Azure
2. **Store Secrets Securely**: Use Azure Key Vault
3. **Handle Errors**: Azure SDK throws specific exceptions
4. **Use Async When Possible**: For better performance
5. **Monitor Costs**: Be aware of service pricing

## Testing

Mock Azure services for local testing:
```python
from unittest.mock import Mock

mock_client = Mock()
mock_client.get_secret.return_value = "test-secret"
```

## Copilot Tips for Azure

- Import Azure SDKs before asking for suggestions
- Use standard Azure naming conventions
- Provide connection strings or credentials in context
- Comment what you want to achieve with Azure services

## Resources

- [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)
- [Azure Documentation](https://docs.microsoft.com/azure)
- [GitHub Copilot Documentation](https://docs.github.com/copilot)

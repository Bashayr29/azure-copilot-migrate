"""
Azure integration utilities for copilot testing.

This module contains utilities for Azure service integration,
demonstrating how copilot can assist with cloud development.
"""

class AzureConfig:
    """Configuration for Azure services."""
    
    def __init__(self, subscription_id=None, resource_group=None):
        """
        Initialize Azure configuration.
        
        Args:
            subscription_id: Azure subscription ID
            resource_group: Azure resource group name
        """
        self.subscription_id = subscription_id or "default-subscription"
        self.resource_group = resource_group or "default-rg"
        self.region = "eastus"
    
    def get_connection_string(self):
        """Generate a connection configuration."""
        return {
            "subscription_id": self.subscription_id,
            "resource_group": self.resource_group,
            "region": self.region
        }
    
    def validate(self):
        """Validate the configuration."""
        if not self.subscription_id:
            return False, "Subscription ID is required"
        if not self.resource_group:
            return False, "Resource group is required"
        return True, "Configuration is valid"


class AzureService:
    """Mock Azure service for testing purposes."""
    
    def __init__(self, config):
        """Initialize the service with configuration."""
        self.config = config
        self.connected = False
    
    def connect(self):
        """Establish connection to Azure services."""
        is_valid, message = self.config.validate()
        if is_valid:
            self.connected = True
            return True, "Connected successfully"
        return False, f"Connection failed: {message}"
    
    def disconnect(self):
        """Disconnect from Azure services."""
        self.connected = False
        return "Disconnected"
    
    def get_status(self):
        """Get the current connection status."""
        return {
            "connected": self.connected,
            "config": self.config.get_connection_string()
        }


def create_azure_client(subscription_id=None, resource_group=None):
    """
    Create and configure an Azure service client.
    
    Args:
        subscription_id: Azure subscription ID
        resource_group: Azure resource group name
        
    Returns:
        Configured AzureService instance
    """
    config = AzureConfig(subscription_id, resource_group)
    service = AzureService(config)
    return service

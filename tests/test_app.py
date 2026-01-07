"""
Unit tests for the sample application.

This module demonstrates test patterns that copilot can help generate.
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import DataProcessor, process_data
from azure_utils import AzureConfig, AzureService, create_azure_client


class TestDataProcessor(unittest.TestCase):
    """Test cases for DataProcessor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = DataProcessor("test")
    
    def test_initialization(self):
        """Test processor initialization."""
        self.assertEqual(self.processor.name, "test")
        self.assertEqual(len(self.processor.data), 0)
    
    def test_add_item(self):
        """Test adding items to processor."""
        count = self.processor.add_item(10)
        self.assertEqual(count, 1)
        self.assertEqual(len(self.processor.get_items()), 1)
    
    def test_get_items(self):
        """Test retrieving items."""
        self.processor.add_item(1)
        self.processor.add_item(2)
        self.processor.add_item(3)
        items = self.processor.get_items()
        self.assertEqual(items, [1, 2, 3])
    
    def test_calculate_average(self):
        """Test average calculation."""
        self.processor.add_item(10)
        self.processor.add_item(20)
        self.processor.add_item(30)
        avg = self.processor.calculate_average()
        self.assertEqual(avg, 20.0)
    
    def test_calculate_average_empty(self):
        """Test average calculation with empty data."""
        avg = self.processor.calculate_average()
        self.assertEqual(avg, 0)


class TestAzureUtils(unittest.TestCase):
    """Test cases for Azure utilities."""
    
    def test_azure_config_initialization(self):
        """Test Azure configuration initialization."""
        config = AzureConfig("sub-123", "rg-test")
        self.assertEqual(config.subscription_id, "sub-123")
        self.assertEqual(config.resource_group, "rg-test")
    
    def test_azure_config_defaults(self):
        """Test Azure configuration defaults."""
        config = AzureConfig()
        self.assertEqual(config.subscription_id, "default-subscription")
        self.assertEqual(config.resource_group, "default-rg")
    
    def test_azure_config_validation(self):
        """Test configuration validation."""
        config = AzureConfig("sub-123", "rg-test")
        is_valid, message = config.validate()
        self.assertTrue(is_valid)
        self.assertEqual(message, "Configuration is valid")
    
    def test_azure_service_connect(self):
        """Test Azure service connection."""
        config = AzureConfig("sub-123", "rg-test")
        service = AzureService(config)
        success, message = service.connect()
        self.assertTrue(success)
        self.assertTrue(service.connected)
    
    def test_create_azure_client(self):
        """Test client creation utility."""
        client = create_azure_client("sub-123", "rg-test")
        self.assertIsInstance(client, AzureService)
        self.assertFalse(client.connected)


class TestProcessData(unittest.TestCase):
    """Test cases for data processing functions."""
    
    def test_process_data(self):
        """Test the process_data function."""
        test_data = [1, 2, 3, 4, 5]
        results = process_data(test_data)
        
        self.assertEqual(results["total_count"], 5)
        self.assertEqual(results["average"], 3.0)
        self.assertEqual(results["items"], [1, 2, 3, 4, 5])
    
    def test_process_empty_data(self):
        """Test processing empty data."""
        results = process_data([])
        self.assertEqual(results["total_count"], 0)
        self.assertEqual(results["average"], 0)


if __name__ == "__main__":
    unittest.main()

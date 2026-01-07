"""
Sample Python application for testing Azure and GitHub Copilot integration.

This module demonstrates various programming patterns that can be enhanced
with copilot assistance.
"""

class DataProcessor:
    """A sample data processor class for testing copilot suggestions."""
    
    def __init__(self, name):
        """Initialize the data processor with a name."""
        self.name = name
        self.data = []
    
    def add_item(self, item):
        """Add an item to the data collection."""
        self.data.append(item)
        return len(self.data)
    
    def get_items(self):
        """Retrieve all items in the collection."""
        return self.data
    
    def filter_items(self, condition):
        """Filter items based on a condition function."""
        return [item for item in self.data if condition(item)]
    
    def calculate_average(self):
        """Calculate the average of numeric items."""
        numeric_items = [item for item in self.data if isinstance(item, (int, float))]
        if not numeric_items:
            return 0
        return sum(numeric_items) / len(numeric_items)


def process_data(input_data):
    """
    Process input data and return results.
    
    Args:
        input_data: List of items to process
        
    Returns:
        Dictionary containing processed results
    """
    processor = DataProcessor("main")
    
    for item in input_data:
        processor.add_item(item)
    
    return {
        "total_count": len(processor.get_items()),
        "average": processor.calculate_average(),
        "items": processor.get_items()
    }


def main():
    """Main entry point for the application."""
    # Sample data for testing
    test_data = [1, 2, 3, 4, 5, 10, 20, 30]
    
    # Process the data
    results = process_data(test_data)
    
    # Display results
    print(f"Total items: {results['total_count']}")
    print(f"Average value: {results['average']}")
    print(f"All items: {results['items']}")


if __name__ == "__main__":
    main()

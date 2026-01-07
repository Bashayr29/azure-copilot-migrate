"""
Example: Data transformation pipeline with copilot assistance.

This demonstrates how copilot can help with data processing tasks.
"""

from typing import List, Dict, Any, Callable
from datetime import datetime, timedelta
import json


class DataTransformer:
    """Transformer for various data processing tasks."""
    
    def __init__(self):
        """Initialize the transformer."""
        self.transformations: List[Callable] = []
    
    def add_transformation(self, func: Callable):
        """Add a transformation function to the pipeline."""
        self.transformations.append(func)
    
    def transform(self, data: Any) -> Any:
        """Apply all transformations in sequence."""
        result = data
        for transform_func in self.transformations:
            result = transform_func(result)
        return result
    
    def reset(self):
        """Clear all transformations."""
        self.transformations = []


def filter_by_date(records: List[Dict], 
                   date_field: str, 
                   start_date: datetime, 
                   end_date: datetime) -> List[Dict]:
    """Filter records by date range."""
    filtered = []
    for record in records:
        record_date = datetime.fromisoformat(record[date_field])
        if start_date <= record_date <= end_date:
            filtered.append(record)
    return filtered


def aggregate_by_field(records: List[Dict], 
                       group_field: str, 
                       value_field: str) -> Dict[str, float]:
    """Aggregate values grouped by a field."""
    aggregates = {}
    for record in records:
        key = record[group_field]
        value = record[value_field]
        
        if key not in aggregates:
            aggregates[key] = 0
        aggregates[key] += value
    
    return aggregates


def normalize_values(records: List[Dict], field: str) -> List[Dict]:
    """Normalize numeric values to 0-1 range."""
    if not records:
        return records
    
    # Find min and max
    values = [record[field] for record in records]
    min_val = min(values)
    max_val = max(values)
    
    # Normalize
    range_val = max_val - min_val
    if range_val == 0:
        return records
    
    normalized = []
    for record in records:
        normalized_record = record.copy()
        normalized_record[field] = (record[field] - min_val) / range_val
        normalized.append(normalized_record)
    
    return normalized


def enrich_with_metadata(records: List[Dict], metadata: Dict) -> List[Dict]:
    """Add metadata fields to each record."""
    enriched = []
    for record in records:
        enriched_record = record.copy()
        enriched_record.update(metadata)
        enriched.append(enriched_record)
    return enriched


def convert_to_csv_format(records: List[Dict]) -> str:
    """Convert records to CSV format string."""
    if not records:
        return ""
    
    # Get headers
    headers = list(records[0].keys())
    csv_lines = [",".join(headers)]
    
    # Add data rows
    for record in records:
        values = [str(record.get(header, "")) for header in headers]
        csv_lines.append(",".join(values))
    
    return "\n".join(csv_lines)


def demo_pipeline():
    """Demonstrate a data processing pipeline."""
    # Sample data
    sample_data = [
        {"id": 1, "date": "2024-01-15T10:00:00", "category": "A", "value": 100},
        {"id": 2, "date": "2024-01-16T10:00:00", "category": "B", "value": 150},
        {"id": 3, "date": "2024-01-17T10:00:00", "category": "A", "value": 200},
        {"id": 4, "date": "2024-01-18T10:00:00", "category": "C", "value": 120},
        {"id": 5, "date": "2024-01-19T10:00:00", "category": "B", "value": 180},
    ]
    
    print("Original data:")
    print(json.dumps(sample_data, indent=2))
    
    # Filter by date
    start = datetime(2024, 1, 16)
    end = datetime(2024, 1, 18)
    filtered = filter_by_date(sample_data, "date", start, end)
    print(f"\nFiltered data ({len(filtered)} records):")
    print(json.dumps(filtered, indent=2))
    
    # Normalize values
    normalized = normalize_values(filtered, "value")
    print("\nNormalized data:")
    print(json.dumps(normalized, indent=2))
    
    # Aggregate by category
    aggregates = aggregate_by_field(sample_data, "category", "value")
    print("\nAggregates by category:")
    print(json.dumps(aggregates, indent=2))
    
    # Enrich with metadata
    enriched = enrich_with_metadata(filtered, {
        "processed_at": datetime.now().isoformat(),
        "source": "demo_pipeline"
    })
    print("\nEnriched data:")
    print(json.dumps(enriched, indent=2))
    
    # Convert to CSV
    csv_output = convert_to_csv_format(filtered)
    print("\nCSV output:")
    print(csv_output)


if __name__ == "__main__":
    demo_pipeline()

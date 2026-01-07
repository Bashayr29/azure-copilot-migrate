# GitHub Copilot Testing Guide

## Overview

This document provides guidance on how to test GitHub Copilot features with this repository.

## Test Scenarios

### 1. Code Completion

Try typing incomplete code and observe suggestions:

```python
def calculate_
# Copilot should suggest function completions
```

### 2. Function Generation

Write a comment describing what you want:

```python
# Function to validate email address format
# Copilot should generate the implementation
```

### 3. Documentation Generation

Place cursor above a function and type `"""`:

```python
def my_function(param1, param2):
    """
    # Copilot should generate docstring
```

### 4. Test Generation

Write a test class name:

```python
class TestMyNewFeature:
    # Copilot should suggest test methods
```

### 5. Refactoring

Highlight code and ask Copilot to refactor or improve it.

## Best Practices

1. **Write Clear Comments**: The clearer your comments, the better suggestions you'll get
2. **Use Descriptive Names**: Function and variable names help guide suggestions
3. **Provide Context**: Include imports and related code in the same file
4. **Iterate**: Review and refine suggestions rather than accepting blindly

## Azure Integration Testing

When working with Azure code:

1. Copilot understands Azure SDK patterns
2. Provide import statements for Azure libraries
3. Use standard Azure naming conventions
4. Include configuration objects in context

## Common Use Cases

### Database Queries
```python
# Query to get all users created in the last 30 days
# Copilot can generate appropriate SQL or ORM queries
```

### API Endpoints
```python
# REST endpoint for creating a new user
# Copilot can generate Flask, FastAPI, or other framework code
```

### Error Handling
```python
try:
    # Your code here
# Copilot can suggest appropriate except clauses
```

## Tips

- Use Tab to accept suggestions
- Use Alt+] to cycle through alternatives
- Use Ctrl+Enter to see all suggestions
- Provide examples for better results

## Evaluating Suggestions

Always review suggestions for:
- Security implications
- Performance considerations
- Code style consistency
- Correctness and logic

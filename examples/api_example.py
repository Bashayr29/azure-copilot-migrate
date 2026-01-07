"""
Example: Using GitHub Copilot to generate a REST API with Azure integration.

This example demonstrates how copilot can assist in creating API endpoints.
"""

from typing import Dict, List, Optional
from datetime import datetime


class User:
    """User model for the API."""
    
    def __init__(self, user_id: str, username: str, email: str):
        """Initialize a user."""
        self.user_id = user_id
        self.username = username
        self.email = email
        self.created_at = datetime.utcnow()
        self.is_active = True
    
    def to_dict(self) -> Dict:
        """Convert user to dictionary."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "is_active": self.is_active
        }


class UserRepository:
    """Mock repository for user management."""
    
    def __init__(self):
        """Initialize the repository."""
        self.users: Dict[str, User] = {}
    
    def create_user(self, user_id: str, username: str, email: str) -> User:
        """Create a new user."""
        user = User(user_id, username, email)
        self.users[user_id] = user
        return user
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Get a user by ID."""
        return self.users.get(user_id)
    
    def list_users(self) -> List[User]:
        """List all users."""
        return list(self.users.values())
    
    def update_user(self, user_id: str, username: Optional[str] = None, 
                    email: Optional[str] = None) -> Optional[User]:
        """Update user details."""
        user = self.users.get(user_id)
        if not user:
            return None
        
        if username:
            user.username = username
        if email:
            user.email = email
        
        return user
    
    def delete_user(self, user_id: str) -> bool:
        """Delete a user."""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False


class APIEndpoints:
    """Sample API endpoints."""
    
    def __init__(self):
        """Initialize API with repository."""
        self.repo = UserRepository()
    
    def handle_create_user(self, data: Dict) -> Dict:
        """Handle POST /users - Create a new user."""
        try:
            user = self.repo.create_user(
                data["user_id"],
                data["username"],
                data["email"]
            )
            return {
                "status": "success",
                "data": user.to_dict()
            }
        except KeyError as e:
            return {
                "status": "error",
                "message": f"Missing required field: {e}"
            }
    
    def handle_get_user(self, user_id: str) -> Dict:
        """Handle GET /users/{user_id} - Get user by ID."""
        user = self.repo.get_user(user_id)
        if user:
            return {
                "status": "success",
                "data": user.to_dict()
            }
        return {
            "status": "error",
            "message": "User not found"
        }
    
    def handle_list_users(self) -> Dict:
        """Handle GET /users - List all users."""
        users = self.repo.list_users()
        return {
            "status": "success",
            "data": [user.to_dict() for user in users]
        }
    
    def handle_update_user(self, user_id: str, data: Dict) -> Dict:
        """Handle PUT /users/{user_id} - Update user."""
        user = self.repo.update_user(
            user_id,
            data.get("username"),
            data.get("email")
        )
        if user:
            return {
                "status": "success",
                "data": user.to_dict()
            }
        return {
            "status": "error",
            "message": "User not found"
        }
    
    def handle_delete_user(self, user_id: str) -> Dict:
        """Handle DELETE /users/{user_id} - Delete user."""
        if self.repo.delete_user(user_id):
            return {
                "status": "success",
                "message": "User deleted"
            }
        return {
            "status": "error",
            "message": "User not found"
        }


def demo():
    """Demonstrate the API usage."""
    api = APIEndpoints()
    
    # Create users
    print("Creating users...")
    result1 = api.handle_create_user({
        "user_id": "1",
        "username": "alice",
        "email": "alice@example.com"
    })
    print(result1)
    
    result2 = api.handle_create_user({
        "user_id": "2",
        "username": "bob",
        "email": "bob@example.com"
    })
    print(result2)
    
    # List users
    print("\nListing users...")
    result3 = api.handle_list_users()
    print(result3)
    
    # Get specific user
    print("\nGetting user 1...")
    result4 = api.handle_get_user("1")
    print(result4)
    
    # Update user
    print("\nUpdating user 1...")
    result5 = api.handle_update_user("1", {"email": "alice.new@example.com"})
    print(result5)
    
    # Delete user
    print("\nDeleting user 2...")
    result6 = api.handle_delete_user("2")
    print(result6)
    
    # List users again
    print("\nListing users after deletion...")
    result7 = api.handle_list_users()
    print(result7)


if __name__ == "__main__":
    demo()

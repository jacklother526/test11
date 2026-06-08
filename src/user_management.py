#!/usr/bin/env python3
"""
Advanced example showing a simple user management system.
"""


class User:
    """Represents a user in the system."""
    
    # Class variable to track user IDs
    user_count = 0
    
    def __init__(self, username, email):
        """
        Initialize a new user.
        
        Args:
            username (str): The user's username
            email (str): The user's email address
        """
        User.user_count += 1
        self.id = User.user_count
        self.username = username
        self.email = email
        self.is_active = True
        self.posts = []
    
    def __str__(self):
        """Return string representation of user."""
        return f"User(id={self.id}, username={self.username}, email={self.email})"
    
    def __repr__(self):
        """Return developer-friendly representation."""
        return self.__str__()
    
    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
        return f"User {self.username} has been deactivated"
    
    def activate(self):
        """Activate the user account."""
        self.is_active = True
        return f"User {self.username} has been activated"
    
    def update_email(self, new_email):
        """Update user email address."""
        if '@' not in new_email:
            raise ValueError("Invalid email format")
        self.email = new_email
        return f"Email updated to {new_email}"
    
    def add_post(self, title, content):
        """Add a new post by this user."""
        post = {
            'title': title,
            'content': content,
            'author': self.username
        }
        self.posts.append(post)
        return post
    
    def get_posts(self):
        """Get all posts by this user."""
        return self.posts
    
    def get_info(self):
        """Get user information."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active,
            'post_count': len(self.posts)
        }


class UserManager:
    """Manages a collection of users."""
    
    def __init__(self):
        """Initialize the user manager."""
        self.users = {}
    
    def create_user(self, username, email):
        """Create a new user."""
        if username in self.users:
            raise ValueError(f"User {username} already exists")
        
        user = User(username, email)
        self.users[username] = user
        return user
    
    def get_user(self, username):
        """Get a user by username."""
        if username not in self.users:
            raise ValueError(f"User {username} not found")
        return self.users[username]
    
    def delete_user(self, username):
        """Delete a user."""
        if username not in self.users:
            raise ValueError(f"User {username} not found")
        del self.users[username]
        return f"User {username} deleted"
    
    def list_all_users(self):
        """List all users."""
        return list(self.users.values())
    
    def list_active_users(self):
        """List only active users."""
        return [user for user in self.users.values() if user.is_active]
    
    def get_user_count(self):
        """Get total number of users."""
        return len(self.users)


def main():
    """
    Main demonstration of the user management system.
    """
    print("=" * 60)
    print("User Management System - Demonstration")
    print("=" * 60)
    print()
    
    # Create manager
    manager = UserManager()
    
    # Create users
    print("📝 Creating users...")
    user1 = manager.create_user('alice', 'alice@example.com')
    user2 = manager.create_user('bob', 'bob@example.com')
    user3 = manager.create_user('charlie', 'charlie@example.com')
    print(f"✓ Created: {user1}")
    print(f"✓ Created: {user2}")
    print(f"✓ Created: {user3}")
    print()
    
    # Add posts
    print("📝 Adding posts...")
    user1.add_post("First Post", "Hello everyone!")
    user1.add_post("Second Post", "Python is awesome")
    user2.add_post("Introduction", "Hi, I'm Bob")
    print(f"✓ {user1.username} created {len(user1.posts)} posts")
    print(f"✓ {user2.username} created {len(user2.posts)} posts")
    print()
    
    # Display user info
    print("📊 User Information:")
    for user in manager.list_all_users():
        info = user.get_info()
        print(f"  - {info['username']}: {info['post_count']} posts, Active: {info['is_active']}")
    print()
    
    # Deactivate user
    print("❌ Deactivating user...")
    print(f"✓ {user2.deactivate()}")
    print()
    
    # Show active users
    print("✅ Active Users:")
    active = manager.list_active_users()
    for user in active:
        print(f"  - {user.username}")
    print()
    
    # Update email
    print("✉️  Updating email...")
    print(f"✓ {user1.update_email('alice.new@example.com')}")
    print()
    
    # Show all posts
    print("📚 All Posts by Alice:")
    for i, post in enumerate(user1.get_posts(), 1):
        print(f"  {i}. {post['title']}: {post['content']}")
    print()
    
    print("=" * 60)
    print(f"Total Users Created: {User.user_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()

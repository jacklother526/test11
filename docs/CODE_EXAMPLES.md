# Code Examples

This file shows more complex code examples for your project.

## Example 1: User Class

```python
class User:
    """Represents a user in the system."""
    
    def __init__(self, username, email):
        """
        Initialize a new user.
        
        Args:
            username (str): The user's username
            email (str): The user's email address
        """
        self.username = username
        self.email = email
        self.created_at = None
        self.is_active = True
    
    def __str__(self):
        """Return string representation of user."""
        return f"User({self.username}, {self.email})"
    
    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
        print(f"{self.username} has been deactivated")
    
    def update_email(self, new_email):
        """Update user email address."""
        self.email = new_email
        print(f"Email updated to {new_email}")
```

## Example 2: Database Connection

```python
import sqlite3
from contextlib import contextmanager

class Database:
    """Handle database operations."""
    
    def __init__(self, db_path='app.db'):
        self.db_path = db_path
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"Database error: {e}")
        finally:
            conn.close()
    
    def create_tables(self):
        """Create necessary database tables."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
```

## Example 3: Error Handling

```python
def divide_numbers(a, b):
    """Divide two numbers with proper error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers!")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def process_user_data(user_dict):
    """Process user data safely."""
    try:
        username = user_dict.get('username')
        if not username:
            raise ValueError("Username is required")
        
        email = user_dict.get('email')
        if not email or '@' not in email:
            raise ValueError("Valid email is required")
        
        return {'status': 'success', 'data': user_dict}
    
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}
```

## Example 4: List Comprehensions

```python
# Simple list comprehension
squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8]

# Dictionary comprehension
user_map = {user['id']: user['name'] for user in users}

# Nested comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
# Result: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

## Example 5: Decorators

```python
def timing_decorator(func):
    """Decorator to measure function execution time."""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(2)
    return "Done!"

# Usage
slow_function()  # Prints: slow_function took 2.0005 seconds
```

## Example 6: API Response Handler

```python
def fetch_user_data(user_id):
    """
    Fetch user data from API.
    
    Returns:
        dict: User data or error message
    """
    try:
        # This would be a real API call
        response = {
            'id': user_id,
            'username': 'john_doe',
            'email': 'john@example.com',
            'status': 'active'
        }
        
        if not response:
            return {'error': 'User not found', 'status_code': 404}
        
        return {'data': response, 'status_code': 200}
    
    except Exception as e:
        return {'error': str(e), 'status_code': 500}
```

## Example 7: Configuration Management

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration."""
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    
    # API
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    
    # Security
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
```

## Example 8: Unit Tests

```python
import unittest

class TestUserClass(unittest.TestCase):
    """Test cases for User class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.user = User('testuser', 'test@example.com')
    
    def test_user_creation(self):
        """Test that user is created correctly."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.is_active)
    
    def test_user_deactivation(self):
        """Test that user can be deactivated."""
        self.user.deactivate()
        self.assertFalse(self.user.is_active)
    
    def test_email_update(self):
        """Test email update functionality."""
        self.user.update_email('newemail@example.com')
        self.assertEqual(self.user.email, 'newemail@example.com')

if __name__ == '__main__':
    unittest.main()
```

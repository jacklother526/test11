#!/usr/bin/env python3
"""
Advanced tests demonstrating testing best practices.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from user_management import User, UserManager


class TestResults:
    """Simple test result tracker."""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []
    
    def test(self, name, condition):
        """Run a test assertion."""
        if condition:
            print(f"✓ {name}")
            self.passed += 1
        else:
            print(f"✗ {name}")
            self.failed += 1
            self.errors.append(name)
    
    def summary(self):
        """Print test summary."""
        total = self.passed + self.failed
        percentage = (self.passed / total * 100) if total > 0 else 0
        print(f"\n{'='*50}")
        print(f"Tests Passed: {self.passed}/{total} ({percentage:.1f}%)")
        if self.failed > 0:
            print(f"Tests Failed: {self.failed}")
            for error in self.errors:
                print(f"  - {error}")
        print(f"{'='*50}")


def test_user_creation():
    """Test User class creation."""
    print("\n📝 Test: User Creation")
    print("-" * 50)
    results = TestResults()
    
    user = User('testuser', 'test@example.com')
    
    results.test("User username is correct", user.username == 'testuser')
    results.test("User email is correct", user.email == 'test@example.com')
    results.test("User is active by default", user.is_active == True)
    results.test("User has empty posts list", len(user.posts) == 0)
    results.test("User has ID", user.id > 0)
    
    results.summary()
    return results


def test_user_methods():
    """Test User class methods."""
    print("\n📝 Test: User Methods")
    print("-" * 50)
    results = TestResults()
    
    user = User('alice', 'alice@example.com')
    
    # Test email update
    user.update_email('alice.new@example.com')
    results.test("Email update works", user.email == 'alice.new@example.com')
    
    # Test deactivation
    user.deactivate()
    results.test("Deactivation works", user.is_active == False)
    
    # Test activation
    user.activate()
    results.test("Activation works", user.is_active == True)
    
    # Test adding posts
    post = user.add_post("Test Title", "Test Content")
    results.test("Post creation works", len(user.posts) == 1)
    results.test("Post has correct title", post['title'] == "Test Title")
    results.test("Post has correct content", post['content'] == "Test Content")
    
    results.summary()
    return results


def test_user_manager():
    """Test UserManager class."""
    print("\n📝 Test: User Manager")
    print("-" * 50)
    results = TestResults()
    
    manager = UserManager()
    
    # Test user creation
    user1 = manager.create_user('user1', 'user1@example.com')
    results.test("User creation in manager", user1 is not None)
    
    user2 = manager.create_user('user2', 'user2@example.com')
    results.test("Multiple user creation", manager.get_user_count() == 2)
    
    # Test user retrieval
    retrieved = manager.get_user('user1')
    results.test("User retrieval works", retrieved.username == 'user1')
    
    # Test listing users
    all_users = manager.list_all_users()
    results.test("List all users works", len(all_users) == 2)
    
    # Test user deactivation and active list
    user1.deactivate()
    active_users = manager.list_active_users()
    results.test("List active users works", len(active_users) == 1)
    
    # Test user deletion
    manager.delete_user('user2')
    results.test("User deletion works", manager.get_user_count() == 1)
    
    results.summary()
    return results


def test_error_handling():
    """Test error handling."""
    print("\n📝 Test: Error Handling")
    print("-" * 50)
    results = TestResults()
    
    manager = UserManager()
    manager.create_user('alice', 'alice@example.com')
    
    # Test duplicate user
    try:
        manager.create_user('alice', 'alice2@example.com')
        results.test("Duplicate user prevention", False)
    except ValueError:
        results.test("Duplicate user prevention", True)
    
    # Test invalid email
    user = User('bob', 'bob@example.com')
    try:
        user.update_email('invalid-email')
        results.test("Invalid email prevention", False)
    except ValueError:
        results.test("Invalid email prevention", True)
    
    # Test non-existent user
    try:
        manager.get_user('nonexistent')
        results.test("Non-existent user handling", False)
    except ValueError:
        results.test("Non-existent user handling", True)
    
    results.summary()
    return results


def main():
    """
    Run all tests.
    """
    print("\n" + "=" * 50)
    print("Advanced Test Suite - User Management System")
    print("=" * 50)
    
    all_results = []
    all_results.append(test_user_creation())
    all_results.append(test_user_methods())
    all_results.append(test_user_manager())
    all_results.append(test_error_handling())
    
    # Calculate total
    total_passed = sum(r.passed for r in all_results)
    total_failed = sum(r.failed for r in all_results)
    total = total_passed + total_failed
    
    print(f"\n{'='*50}")
    print(f"OVERALL RESULTS: {total_passed}/{total} tests passed")
    print(f"{'='*50}")
    
    if total_failed == 0:
        print("\n🎉 All tests passed! 🎉\n")
    else:
        print(f"\n⚠️  {total_failed} test(s) failed\n")


if __name__ == "__main__":
    main()

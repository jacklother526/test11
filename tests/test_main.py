#!/usr/bin/env python3
"""
Unit tests for the main application.

This demonstrates how to write basic tests for your Python code.
"""

import sys
import os

# Add src directory to path so we can import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import greet


def test_greet():
    """
    Test the greet function.
    """
    result = greet("Alice")
    assert result == "Hello, Alice! Welcome to Test11 project."
    print("✓ test_greet passed")


def test_greet_with_different_name():
    """
    Test the greet function with a different name.
    """
    result = greet("Bob")
    assert result == "Hello, Bob! Welcome to Test11 project."
    print("✓ test_greet_with_different_name passed")


if __name__ == "__main__":
    test_greet()
    test_greet_with_different_name()
    print("\nAll tests passed! ✨")

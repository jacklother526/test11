#!/usr/bin/env python3
"""
Main application file for the Test11 project.

This is a simple example showing how to structure a Python application.
"""


def greet(name):
    """
    Greet a person with their name.
    
    Args:
        name (str): The person's name
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to Test11 project."


def main():
    """
    Main entry point of the application.
    """
    print("="*50)
    print("Welcome to Test11 Project")
    print("="*50)
    print()
    
    # Get user input
    name = input("What is your name? ")
    
    # Call greet function
    message = greet(name)
    print(message)
    
    print()
    print("This is a beginner-friendly example!")
    print()


if __name__ == "__main__":
    main()

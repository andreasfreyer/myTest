#!/usr/bin/env python3
"""
Demo file for testing conflict resolution.
Feature branch version with enhanced greeting.
"""

def greet(name: str, formal: bool = False) -> str:
    """Return a greeting message with optional formal style."""
    if formal:
        return f"Good day, {name}. How do you do?"
    return f"Hey there, {name}!"


def calculate(a: int, b: int, operation: str = "add") -> int:
    """Calculate with multiple operations."""
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    return 0


def main():
    print(greet("World", formal=True))
    print(f"Sum: {calculate(5, 3)}")
    print(f"Product: {calculate(5, 3, 'multiply')}")


if __name__ == "__main__":
    main()

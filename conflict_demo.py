#!/usr/bin/env python3
"""
Demo file for testing conflict resolution.
"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def calculate(a: int, b: int) -> int:
    """Calculate sum of two numbers."""
    return a + b


def main():
    print(greet("World"))
    print(f"Result: {calculate(5, 3)}")


if __name__ == "__main__":
    main()

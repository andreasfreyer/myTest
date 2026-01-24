#!/usr/bin/env python3
"""
Demo file for testing conflict resolution.
<<<<<<< HEAD
Feature branch version with enhanced greeting.
"""

def greet(name: str, formal: bool = False) -> str:
    """Return a greeting message with optional formal style."""
    if formal:
        return f"Good day, {name}. How do you do?"
    return f"Hey there, {name}!"
=======
Master branch version with logging.
"""

import logging
>>>>>>> 91d281f05263d7094f0f6a971d032195618bdbaf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calculate(a: int, b: int, operation: str = "add") -> int:
    """Calculate with multiple operations."""
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    return 0


def main():
<<<<<<< HEAD
    print(greet("World", formal=True))
    print(f"Sum: {calculate(5, 3)}")
    print(f"Product: {calculate(5, 3, 'multiply')}")
=======
    logger.info("Starting application")
    print(greet("World"))
    print(f"Result: {calculate(5, 3)}")
    logger.info("Done")
>>>>>>> 91d281f05263d7094f0f6a971d032195618bdbaf


if __name__ == "__main__":
    main()
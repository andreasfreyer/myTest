#!/usr/bin/env python3
"""
Demo file for testing conflict resolution.
Master branch version with logging.
"""

import logging

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
    logger.info("Starting application")
    print(greet("World"))
    print(f"Result: {calculate(5, 3)}")
    logger.info("Done")


if __name__ == "__main__":
    main()
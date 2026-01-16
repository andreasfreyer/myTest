#!/usr/bin/env python3
"""
Demo file for testing conflict resolution.
Master branch version with logging.
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def greet(name: str) -> str:
    """Return a greeting message with logging."""
    logger.info(f"Greeting {name}")
    return f"Welcome, {name}!"


def calculate(a: int, b: int) -> int:
    """Calculate sum with logging."""
    logger.info(f"Calculating {a} + {b}")
    result = a + b
    logger.info(f"Result: {result}")
    return result


def main():
    logger.info("Starting application")
    print(greet("World"))
    print(f"Result: {calculate(5, 3)}")
    logger.info("Done")


if __name__ == "__main__":
    main()

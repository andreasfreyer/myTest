#!/usr/bin/env python3
"""
Example module for testing merge conflicts.
This file demonstrates various code structures.
"""

import os
import sys
from typing import List, Optional, Dict


# Configuration constants
DEBUG_MODE = False
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30
DEFAULT_BUFFER_SIZE = 4096


class DataProcessor:
    """Processes data from various sources."""

    def __init__(self, name: str, buffer_size: int = DEFAULT_BUFFER_SIZE):
        self.name = name
        self.buffer_size = buffer_size
        self.data: List[str] = []
        self.errors: List[str] = []
        self._initialized = False

    def initialize(self) -> bool:
        """Initialize the processor."""
        if self._initialized:
            return True

        try:
            self._setup_buffers()
            self._initialized = True
            return True
        except Exception as e:
            self.errors.append(f"Init failed: {e}")
            return False

    def _setup_buffers(self) -> None:
        """Setup internal buffers."""
        self.data = []
        self.errors = []

    def process_item(self, item: str) -> Optional[str]:
        """Process a single item."""
        if not item:
            return None

        result = item.strip().upper()
        self.data.append(result)
        return result

    def process_batch(self, items: List[str]) -> List[str]:
        """Process multiple items."""
        results = []
        for item in items:
            processed = self.process_item(item)
            if processed:
                results.append(processed)
        return results

    def get_statistics(self) -> Dict[str, int]:
        """Get processing statistics."""
        return {
            "total_items": len(self.data),
            "total_errors": len(self.errors),
            "buffer_size": self.buffer_size,
        }

    def reset(self) -> None:
        """Reset the processor state."""
        self.data = []
        self.errors = []
        self._initialized = False


def calculate_checksum(data: bytes) -> int:
    """Calculate a simple checksum."""
    total = 0
    for byte in data:
        total += byte
        total = total % 65536
    return total


def format_output(items: List[str], prefix: str = "") -> str:
    """Format items for output."""
    lines = []
    for i, item in enumerate(items):
        lines.append(f"{prefix}{i+1}. {item}")
    return "\n".join(lines)


def validate_input(value: str) -> bool:
    """Validate input string."""
    if not value:
        return False
    if len(value) > 1000:
        return False
    return True


def main():
    """Main entry point."""
    processor = DataProcessor("test")
    processor.initialize()

    test_data = ["hello", "world", "test", "data"]
    results = processor.process_batch(test_data)

    print("Processing complete")
    print(f"Results: {results}")
    print(f"Stats: {processor.get_statistics()}")


if __name__ == "__main__":
    main()

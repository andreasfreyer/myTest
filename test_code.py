#!/usr/bin/env python3
"""
Example module for testing merge conflicts.
This file demonstrates various code structures.
<<<<<<< HEAD
Updated: Added async support
=======
Version 2.0 - Enhanced with logging
>>>>>>> feature/logging-changes
"""

import os
import sys
<<<<<<< HEAD
import asyncio
=======
import logging
>>>>>>> feature/logging-changes
from typing import List, Optional, Dict


# Configuration constants
<<<<<<< HEAD
DEBUG_MODE = False
MAX_RETRIES = 3
TIMEOUT_SECONDS = 60
DEFAULT_BUFFER_SIZE = 4096
ASYNC_ENABLED = True
=======
DEBUG_MODE = True
MAX_RETRIES = 5
TIMEOUT_SECONDS = 30
DEFAULT_BUFFER_SIZE = 8192


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
>>>>>>> feature/logging-changes


class DataProcessor:
    """Processes data from various sources."""

    def __init__(self, name: str, buffer_size: int = DEFAULT_BUFFER_SIZE):
        self.name = name
        self.buffer_size = buffer_size
        self.data: List[str] = []
        self.errors: List[str] = []
        self._initialized = False
        logger.info(f"Created processor: {name}")

    def initialize(self) -> bool:
        """Initialize the processor."""
        if self._initialized:
            logger.warning("Already initialized")
            return True

        try:
            self._setup_buffers()
            self._load_config()
            self._initialized = True
            logger.info("Initialization complete")
            return True
        except Exception as e:
            self.errors.append(f"Init failed: {e}")
            logger.error(f"Init failed: {e}")
            return False

    def _setup_buffers(self) -> None:
        """Setup internal buffers."""
        self.data = []
        self.errors = []
        logger.debug("Buffers initialized")

    def _load_config(self) -> None:
        """Load configuration from environment."""
        self.config = {
            "debug": os.getenv("DEBUG", "false").lower() == "true",
            "timeout": int(os.getenv("TIMEOUT", "30")),
        }

    def _load_config(self) -> None:
        """Load configuration from environment."""
        self.config = {
            "debug": os.getenv("DEBUG", "false").lower() == "true",
            "timeout": int(os.getenv("TIMEOUT", "30")),
        }

    def process_item(self, item: str) -> Optional[str]:
        """Process a single item with validation."""
        if not item:
            logger.warning("Empty item received")
            return None

        if not validate_input(item):
            logger.error(f"Invalid item: {item[:50]}")
            return None

        if not validate_input(item):
            return None

        result = item.strip().upper()
        self.data.append(result)
        logger.debug(f"Processed: {result}")
        return result

    async def process_item_async(self, item: str) -> Optional[str]:
        """Process a single item asynchronously."""
        await asyncio.sleep(0.01)
        return self.process_item(item)

    def process_batch(self, items: List[str]) -> List[str]:
        """Process multiple items with progress tracking."""
        results = []
        total = len(items)
        for idx, item in enumerate(items):
<<<<<<< HEAD
=======
            logger.info(f"Processing {idx+1}/{total}")
>>>>>>> feature/logging-changes
            processed = self.process_item(item)
            if processed:
                results.append(processed)
        logger.info(f"Batch complete: {len(results)}/{total} successful")
        return results

    async def process_batch_async(self, items: List[str]) -> List[str]:
        """Process multiple items asynchronously."""
        tasks = [self.process_item_async(item) for item in items]
        results = await asyncio.gather(*tasks)
        return [r for r in results if r is not None]

    def get_statistics(self) -> Dict[str, int]:
        """Get processing statistics."""
        return {
            "total_items": len(self.data),
            "total_errors": len(self.errors),
            "buffer_size": self.buffer_size,
            "async_enabled": ASYNC_ENABLED,
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


<<<<<<< HEAD
async def calculate_checksum_async(data: bytes) -> int:
    """Calculate checksum asynchronously."""
    await asyncio.sleep(0)
    return calculate_checksum(data)


def format_output(items: List[str], prefix: str = "") -> str:
    """Format items for output."""
=======
def format_output(items: List[str], prefix: str = "", numbered: bool = True) -> str:
    """Format items for output with options."""
>>>>>>> feature/logging-changes
    lines = []
    for i, item in enumerate(items):
        if numbered:
            lines.append(f"{prefix}{i+1}. {item}")
        else:
            lines.append(f"{prefix}{item}")
    return "\n".join(lines)


def validate_input(value: str) -> bool:
    """Validate input string with extended checks."""
    if not value:
        return False
    if len(value) > 1000:
        return False
    if any(char in value for char in ['<', '>', '&']):
        return False
    return True


<<<<<<< HEAD
async def main_async():
    """Async main entry point."""
=======
def main():
    """Main entry point."""
    logger.info("Starting application")
>>>>>>> feature/logging-changes
    processor = DataProcessor("test")
    processor.initialize()

    test_data = ["hello", "world", "test", "data"]
    results = await processor.process_batch_async(test_data)

<<<<<<< HEAD
    print("Async processing complete")
    print(f"Results: {results}")
=======
    print("Processing complete")
    print(format_output(results, prefix="  "))
>>>>>>> feature/logging-changes
    print(f"Stats: {processor.get_statistics()}")
    logger.info("Application finished")


def main():
    """Main entry point."""
    if ASYNC_ENABLED:
        asyncio.run(main_async())
    else:
        processor = DataProcessor("test")
        processor.initialize()
        test_data = ["hello", "world", "test", "data"]
        results = processor.process_batch(test_data)
        print("Processing complete")
        print(f"Results: {results}")
        print(f"Stats: {processor.get_statistics()}")


if __name__ == "__main__":
    main()

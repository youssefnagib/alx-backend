# 0x01-caching

## Description
This project is focused on caching algorithms and concepts, implemented in Python. Caching is a technique that stores frequently accessed data temporarily, allowing for faster retrieval and optimized performance in applications. By implementing various caching strategies, we aim to understand the advantages and trade-offs associated with each approach.

## Learning Objectives
- Understand the concept of caching and why it's used
- Explore different caching policies (e.g., LRU, MRU, FIFO)
- Implement caching strategies to optimize performance in applications
- Evaluate the efficiency and limitations of different caching mechanisms

## Project Structure
- **BasicCache**: A caching class that does not remove items (no limit on cache size).
- **FIFOCache**: A caching class implementing First-In-First-Out (FIFO) policy.
- **LRUCache**: A caching class implementing Least Recently Used (LRU) policy.
- **MRUCache**: A caching class implementing Most Recently Used (MRU) policy.
- **LFUCache**: A caching class implementing Least Frequently Used (LFU) policy.

## Requirements
- Python 3.6+
- `pytest` for unit testing (optional but recommended)

## Usage
Each caching class has a defined maximum size. When the limit is reached, items are removed from the cache according to the respective policy.

### Example Usage
```python
from caching import LRUCache

cache = LRUCache(max_size=3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
print(cache.get("a"))  # Output: 1
cache.put("d", 4)  # This will evict "b" from the cache
print(cache.get("b"))  # Output: None

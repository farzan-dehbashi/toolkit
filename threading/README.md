# Threading

Python threading examples for concurrent execution.

| File | Description |
|------|-------------|
| [threading_.py](threading_.py) | Basic two-thread example |
| [multi.py](multi.py) | Multiple threads |

## Key concepts
- `threading.Thread(target=func)` — creates a thread
- `.start()` — starts the thread
- `.join()` — waits for thread to finish
- Use `threading.Lock()` to prevent race conditions on shared resources

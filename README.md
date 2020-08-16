# Set up project

- Create virtual environment: `python -m venv .venv`
- Set up project: `pip install -e .`
- Run unit tests: `pytest`

# Run project from console

```
Usage: algorithms [OPTIONS]

Options:
  -a, --algorithm [SelectionSort|InsertionSort|BubbleSort|QuickSort|MergeSort|HeapSort|RadixSort]
                                  [required]
  -l, --array TEXT                [required]
  --help                          Show this message and exit.
```

Array to be sorted has to be passed as string, in `json` format. Make sure it's quoted.

Example usage:
```
algorithms -a BubbleSort -l "[1, 5, -10]"
```
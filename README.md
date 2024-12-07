
# File Hasher

## Overview
**File Hasher** is a Python command-line tool designed to generate and compare hash values for files. This tool leverages Python's `hashlib` library to ensure secure and consistent hashing. It is user-friendly and supports a variety of hashing algorithms.

## Features
- Generate a file's hash using any supported hashing algorithm.
- Save generated hashes to a file for future reference.
- Compare a file's hash with previously saved hash values.
- Simple command-line interface (CLI) for ease of use.

## Requirements
- Python 3.8 or higher
- No external dependencies (uses Python standard library)

## Usage

### General Syntax
```bash
python file_hasher.py <file_path> [options]
```

### Options
- `-a`, `--algorithm`: Specify the hashing algorithm (default: `sha256`).
- `-o`, `--output`: Save the generated hash to the specified file.
- `-c`, `--compare`: Compare the generated hash with saved hashes in the specified file.

### Examples

#### Generate and Print a File Hash
```bash
python file_hasher.py example.txt
```
Output:
```
Hash (sha256): 2d711642b726b04401627ca9fbac4c4aed94e3d52f2d6bde9f8e12c7fcdc8a0e
```

#### Generate a Hash Using a Specific Algorithm
```bash
python file_hasher.py example.txt -a sha1
```

#### Save the Hash to a File
```bash
python file_hasher.py example.txt -o hashes.txt
```
This appends the file path and its hash to `hashes.txt`:
```
example.txt: 2d711642b726b04401627ca9fbac4c4aed94e3d52f2d6bde9f8e12c7fcdc8a0e
```

#### Compare a File's Hash
```bash
python file_hasher.py example.txt -c hashes.txt
```
Output:
```
Hash matches!
```
or
```
Hash does not match.
```

## Supported Algorithms
This tool supports all algorithms available in Python's `hashlib` library. Common algorithms include:
- `md5`
- `sha1`
- `sha256`
- `sha512`

You can view all available algorithms on your system by running:
```python
import hashlib
print(hashlib.algorithms_available)
```

## Error Handling
The script handles common errors such as:
- File not found
- Unsupported hashing algorithm
- Missing or incorrect arguments

## Project Structure
- `file_hasher.py`: The main script containing all the functionality.
- `README.md`: Documentation for the project.

## License
This project is created for Mohawk College. Feel free to use, modify, and distribute it as needed.

## Author
Created by Jainam Shah - 000930038. Contributions are welcome!

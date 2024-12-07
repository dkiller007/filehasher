import hashlib
import argparse
import os

def generate_hash(file_path, algorithm="sha256"):
    """Generate a hash for the given file using the specified algorithm."""
    try:
        hash_func = hashlib.new(algorithm)
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return None

def save_hash(file_path, hash_value, output_file):
    """Save the file path and hash value to a file."""
    try:
        with open(output_file, 'a') as f:
            f.write(f"{file_path}: {hash_value}\n")
        print(f"Hash saved to '{output_file}'.")
    except Exception as e:
        print(f"Error saving hash: {e}")

def compare_hash(file_path, hash_value, hashes_file):
    """Check if the file's hash matches any entry in the hashes file."""
    try:
        with open(hashes_file, 'r') as f:
            for line in f:
                stored_file, stored_hash = line.strip().split(": ")
                if stored_file == file_path:
                    return hash_value == stored_hash
        print(f"No matching hash found for '{file_path}'.")
        return False
    except FileNotFoundError:
        print(f"Error: File '{hashes_file}' not found.")
        return None

def main():
    parser = argparse.ArgumentParser(description="File Hashing Tool")
    parser.add_argument("file", help="File to process")
    parser.add_argument("-a", "--algorithm", default="sha256", help="Hashing algorithm (default: sha256)")
    parser.add_argument("-o", "--output", help="Save hash to a file")
    parser.add_argument("-c", "--compare", help="Compare hash with saved values")
    args = parser.parse_args()

    hash_value = generate_hash(args.file, args.algorithm)
    if hash_value:
        print(f"Hash ({args.algorithm}): {hash_value}")
        if args.output:
            save_hash(args.file, hash_value, args.output)
        if args.compare:
            is_match = compare_hash(args.file, hash_value, args.compare)
            if is_match is None:
                print("Comparison failed.")
            elif is_match:
                print("Hash matches!")
            else:
                print("Hash does not match.")

if __name__ == "__main__":
    main()

# Software Name: Photo_Duplicate_Finder
# Category: Photo
# Description: A software that scans and identifies duplicate photos in a user

import os
import hashlib
from collections import defaultdict

def find_duplicate_photos(directory):
    """
    Finds duplicate photos within a given directory.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        dict: A dictionary where keys are duplicate photo groups (lists of file paths)
              and values are the hash of the duplicate photo.
              Returns an empty dictionary if no duplicates are found.
    """

    file_hashes = defaultdict(list)
    duplicate_groups = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)

            try:
                with open(filepath, 'rb') as f:
                    file_content = f.read()
                    file_hash = hashlib.md5(file_content).hexdigest()
                    file_hashes[file_hash].append(filepath)
            except (IOError, OSError) as e:
                print(f"Error processing file {filepath}: {e}")
                continue

    for file_hash, filepaths in file_hashes.items():
        if len(filepaths) > 1:
            duplicate_groups[tuple(filepaths)] = file_hash

    return duplicate_groups


if __name__ == '__main__':
    directory_to_scan = input("Enter the directory to scan for duplicate photos: ")

    if not os.path.isdir(directory_to_scan):
        print("Invalid directory path.")
    else:
        duplicates = find_duplicate_photos(directory_to_scan)

        if duplicates:
            print("Duplicate photos found:")
            for filepaths, file_hash in duplicates.items():
                print(f"Hash: {file_hash}")
                for filepath in filepaths:
                    print(f"  - {filepath}")
        else:
            print("No duplicate photos found in the specified directory.")
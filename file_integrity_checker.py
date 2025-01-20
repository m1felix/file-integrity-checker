import hashlib
import os

# Function to calculate the hash of a file
def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of the given file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):  # Read the file in chunks
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print("File not found! Please provide a valid file path.")
        return None

# Function to save the hash to a record file
def save_hash(file_path, hash_value):
    """Save the hash value to a record file."""
    record_file = "file_hash_records.txt"
    with open(record_file, 'a') as f:
        f.write(f"{file_path} : {hash_value}\n")
    print(f"Hash for '{file_path}' saved to {record_file}.")

# Function to verify the integrity of a file
def verify_file(file_path):
    """Check if the file's hash matches the stored hash."""
    record_file = "file_hash_records.txt"
    if not os.path.exists(record_file):
        print("No hash records found! Please save a hash first.")
        return

    try:
        with open(record_file, 'r') as f:
            records = f.readlines()
        # Find the hash for the given file in the record file
        for record in records:
            saved_file, saved_hash = record.strip().split(" : ")
            if saved_file == file_path:
                current_hash = calculate_file_hash(file_path)
                if current_hash == saved_hash:
                    print("The file is intact. No changes detected.")
                else:
                    print("WARNING: The file has been modified or tampered with!")
                return
        print("No hash found for this file. Please save a hash first.")
    except FileNotFoundError:
        print("Hash record file not found!")

# Main menu
def main():
    while True:
        print("\nFile Integrity Checker")
        print("1. Save file hash")
        print("2. Verify file integrity")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the file path to save its hash: ")
            hash_value = calculate_file_hash(file_path)
            if hash_value:
                save_hash(file_path, hash_value)
        elif choice == '2':
            file_path = input("Enter the file path to verify: ")
            verify_file(file_path)
        elif choice == '3':
            print("Exiting File Integrity Checker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()


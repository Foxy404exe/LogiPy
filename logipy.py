
from pathlib import Path


def preview_rename(folder, prefix):
    """Preview file renaming without changing anything."""
    folder = Path(folder)

    if not folder.is_dir():
        print("Error: folder not found.")
        return

    files = sorted(
        file for file in folder.iterdir()
        if file.is_file()
    )

    if not files:
        print("No files found in this folder.")
        return

    print("\nLogiPy - Rename Preview")
    print("-" * 35)

    for number, file in enumerate(files, start=1):
        new_name = f"{prefix}_{number}{file.suffix}"
        print(f"{file.name}  ->  {new_name}")

    print("\nPreview only. No files were changed.")


def main():
    print("Welcome to LogiPy!")
    print("File automation made simple.\n")

    folder = input("Enter the folder path: ").strip().strip('"')
    prefix = input("Enter the new file prefix: ").strip()

    if not prefix:
        print("Error: prefix cannot be empty.")
        return

    preview_rename(folder, prefix)


if __name__ == "__main__":
    main()

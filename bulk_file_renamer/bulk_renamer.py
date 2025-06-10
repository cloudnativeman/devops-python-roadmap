import os

directory = input("Enter directory path: ").strip()
pattern = input("Enter new filename pattern (e.g., file): ").strip()
file_list = os.listdir(directory)

for idx, filename in enumerate(file_list, 1):
    old_path = os.path.join(directory, filename)
    if os.path.isdir(old_path):
        continue
    _, ext = os.path.splitext(filename)
    new_name = f"{pattern}{idx}{ext}"
    new_path = os.path.join(directory, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed '{filename}' to '{new_name}'")

print("All files renamed.")
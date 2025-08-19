src=input("Enter the source file name: ")
dest=input("Enter the destination file name: ")
try:
    with open(src, 'r') as source_file:
        content = source_file.read()
    with open(dest, 'w') as dest_file:
        dest_file.write(content)
    print(f"File copied successfully from {src} to {dest}.")
except FileNotFoundError:
    print(f"Error: The file {src} does not exist.")
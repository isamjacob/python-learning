with open("test.txt", "w") as file:
#     file.write("Hello, this is my first file!\n")
#     file.write("Python makes file handling easy.\n")
#     file.write("This is line 3.\n")
# print("File written successfully")

# # What is with ?
# # With automatically closes the file when done. Without it you'd have to manually call
# # file.close() - and if you forget this, it causes bugs.

# # File modes
# # "w" - Write - creates/overwrites
# # "r" - Read - reads existing file
# # "a" - Append - adds to end 
# # "x" - create - fails if exists

# # Reading file 

# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)

# # Reading line by line
# with open("test.txt", "r") as file:
#     for line in file:
#         print(line.strip())         # strip() removes \n at end 

# # Reading all lines into a list
# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)
#     print(f"Total lines: {len(lines)}")

# # Append mode adds to end, dosen't overwrite
# with open("test.txt", "a") as file:
#     file.write("This line was added later\n")
#     file.write("Appending is useful for logs\n")

# print("Lines appended!")

# # Verify
# with open("test.txt", "r") as file:
#     print(file.read())
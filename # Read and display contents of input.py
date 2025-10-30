# Read and display contents of input.txt

with open('input.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()
    
    # Print each line with line number
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# Alternative method using read()
print("\nReading entire file at once:")
with open('input.txt', 'r') as file:
    content = file.read()
    print(content)
#count all words in the file
with open('input.txt', 'r') as file:
    content = file.read()
    words = content.split()
    print(f"\nTotal number of words: {len(words)}")
#convert all text to uppercase and display
with open('input.txt', 'r') as file:
    content = file.read()
    print("\ncontent in uppercase:")
    print(content.upper())
#write the processed text and word count to new file output.txt
with open('output.txt', 'w') as file:
    file.write("Content in Uppercase:\n")
    file.write(content.upper())
    file.write(f"\nTotal number of words: {len(words)}\n")  
print("\nProcessed content written to output.txt") 
try:
    with open("sway.txt", "w") as file:
        file.write("This is a test file for Sway integration.\n")
        file.write("It contains multiple lines of text.\n")
        file.write("Each line serves to demonstrate file writing capabilities.\n")
except FileNotFoundError:
    print("File not found error occurred.")
finally:
    print("File operation completed.")
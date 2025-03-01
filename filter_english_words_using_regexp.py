import re

def remove_symbols_translate(input_string):
    # Symbols to remove
    symbols_to_remove = '<>:/\\\"?*!@#$%&'  # Symbols that should not be assigned to a file name (Linux & Windows)
    # Create a translation table to remove the symbols
    translation_table = str.maketrans('', '', symbols_to_remove)
    # Apply the translation table
    cleaned_string = input_string.translate(translation_table)
    return cleaned_string

# Function to filter words using a regular expression
def filter_words(line, pattern):
    words = line.split()  # Split the line into words
    filtered_words = [word for word in words if re.search(pattern, word)]
    return filtered_words

# MODIFY THIS: Regular expression to filter words
pattern = r'\b\w*a{2}\w*\b'  # Example pattern: words with 'aa'
pattern_for_file_name = remove_symbols_translate(pattern)
print(f"\n{pattern_for_file_name}\n")

# Input and output file paths
input_file = 'english_words.txt'
output_file = f'english_words_filtered_by_{pattern_for_file_name}.txt'

# Read the input file and process
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Filter words and write to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    for line in lines:
        filtered_words = filter_words(line, pattern)
        if filtered_words:
            file.write(' '.join(filtered_words) + '\n')

print("Process completed. The filtered words have been saved in", output_file)

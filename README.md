# Filter English Words Using RegExp

## Overview
This project contains a Python script that filters English words from a given text using regular expressions (RegExp). The script is designed to identify and extract words that match specific patterns defined by regular expressions.

## Code Explanation
The main functionality is implemented in a Python script. Below is an explanation of the key parts of the code:

1. **Import the `re` module**: The script begins by importing the `re` module, which provides support for working with regular expressions in Python.

2. **Define the `filter_english_words` function**: This function takes a string `text` as input and returns a list of English words found in the text. It uses a regular expression pattern to identify sequences of English letters.

3. **Regular expression pattern**: The pattern used in the script is `r'\b[a-zA-Z]+\b'`. This pattern matches sequences of English letters, where `\b` denotes word boundaries, ensuring that only whole words are matched.

4. **Find all matching words**: The script uses the `re.findall` function to find all substrings in the text that match the defined pattern. This function returns a list of all matching words.

5. **Save the list of words to a file**: The function saves the list of words that match the regular expression pattern to a new `.txt` file, effectively filtering out non-English words and other characters from the input text and storing the results.

## License
This project is licensed under the MIT License.

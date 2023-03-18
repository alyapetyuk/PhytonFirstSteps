def string_operations(s):
    words = s.split()
    num_words = len(words)
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    reversed_string = s[::-1]
    return {"number_of_words": num_words, "longest_word": longest_word, "reversed_string": reversed_string}

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    results = string_operations(input_string)
    print(f"Number of words: {results['number_of_words']}")
    print(f"Longest word: {results['longest_word']}")
    print(f"Reversed string: {results['reversed_string']}")

from text_processing import count_words, unique_words, count_unique_characters, count_characters, reverse_string

# Test String
test_string = "hello world Hello"

# Using word_count module
print("Word count is:", count_words(test_string))
print("Unique Words:", unique_words(test_string))

# Using char_count module
print("Character Count:", count_characters(test_string))
print("Unique Character Count:", count_unique_characters(test_string))

# Using reverse module
print("Reversed string:", reverse_string(test_string))
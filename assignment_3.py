# Take input sentence
m = input('please enter a sentence:')
# Create empty list to contain all unique words
unique_words = []
# Run a for loop over a list of words in input sentence
for i in m.split():
    # Add to unique words list if unique
    if i not in unique_words:
        unique_words.append(i)
# Print the number of unique words
print(str(len(unique_words)) + '\n' + str(sorted(unique_words)))
# Print the unique words alphabetically sorted
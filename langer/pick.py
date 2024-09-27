import json
import random

# Load sentences from a JSON file
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Pick random letters from words whose length is between 1 to 10
def pick_random_letters_from_words(sentences, num_words_to_pick):
    formed_word = ''
    
    for _ in range(num_words_to_pick):
        # Pick a random integer between 1 and 10 to represent the word length
        random_length = random.randint(1, 10)
        
        # Filter words from all sentences that match the random length
        matching_words = []
        for sentence in sentences:
            words = sentence.split()
            matching_words.extend([word for word in words if len(word) == random_length])
        
        # If we find any words of the matching length
        if matching_words:
            # Pick a random word from the matching list
            random_word = random.choice(matching_words)
            # Pick a random letter from that word
            random_letter = random_word[random.randint(0, len(random_word) - 1)]
            # Add the letter to form the final word
            formed_word += random_letter
    
    return formed_word

# Path to your JSON file
file_path = 'C:\Users\\alihu\gram-hacks-team-x\genrtd_sentences.json'

# Load the JSON file
data = load_json_file(file_path)

# Extract the sentences (assuming they are under a key "10" as in your previous example)
sentences = data["10"]

# Pick random letters from words with lengths between 1 to 10 and form a new word
# Adjust the number of random words to pick based on your preference
num_words_to_pick = 10  # Number of words to pick random letters from
random_word = pick_random_letters_from_words(sentences, num_words_to_pick)

print("Randomly formed word:", random_word)


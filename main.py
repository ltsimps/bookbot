letter_occurrences = {}
words = []
letters = []
with open("books/frankenstein.text") as f: 
  file_contents = f.read()
  words = file_contents.split(" ")
  letters = list(file_contents.lower())


def get_word_count(words):
    return len(words)


for letter in letters:
    if letter in letter_occurrences:
      letter_occurrences[letter] += 1
    else:
      letter_occurrences[letter] = 1
  
  # print(letter_occurrences['p'])
  # print(letter_occurrences['c'])
  # print(letter_occurrences[' '])


def print_report(words, letter_occurrences):
  print(f"--- Begin report of books/frankenstein.txt ---")
  print(f"{get_word_count(words)} words found in the document")
  for letter in letter_occurrences:
    if letter.isalpha():
       print(f"The '{letter}' character was found {letter_occurrences[letter]} times")
  print(f"--- End report ---")


print_report(words, letter_occurrences)
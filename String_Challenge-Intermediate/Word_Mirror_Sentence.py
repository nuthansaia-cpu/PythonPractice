"""Reverse word order in a sentence and print mirrored result."""

sentence = input("Enter a sentence: ").strip()
words = sentence.split()

# Reverse word order using slicing.
reversed_words = words[::-1]

print("Original words:", words)
print("Reversed words:", reversed_words)
print("Mirrored sentence:", " ".join(reversed_words))

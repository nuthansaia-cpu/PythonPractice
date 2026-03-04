"""Demonstrate startswith, endswith, remove prefix/suffix, partition."""

sentence = "python is very easy"
print(sentence.startswith("python"))
print(sentence.startswith("is"))
print(sentence.startswith("is", 7))
print(sentence.endswith("easy"))

print("-" * 50)

email = "abc@gmail.com"
print(email.endswith("gmail.com"))
print(email.endswith(".com"))
print(email.endswith("yahoo.com"))

print("-" * 50)

text = "python programming"
print(text.removeprefix("py"))
print(text.removeprefix("java"))

print("-" * 50)

print(text.removesuffix("ing"))

print("-" * 50)

print("python is easy".partition("is"))
print("python is easy".rpartition("s"))

# 07_lists.py
# Python Lists

languages = ["Python", "Java", "C++", "JavaScript"]

print("Programming Languages:")
print(languages)

print("\nFirst language:", languages[0])
print("Second language:", languages[1])

print("\nAll languages:")

for language in languages:
    print("-", language)

languages.append("SQL")

print("\nAfter adding SQL:")
print(languages)

print("\nTotal languages:", len(languages))

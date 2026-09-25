# Andre Pereira
# Chapter 3
languages = ["Python", "JavaScript", "Rust", "Go", "C++"]
print("Initial list:", languages)
print(f"First language: {languages[0]}")

languages[1] = "TypeScript"
print("After modifying index 1:", languages)

languages.append("Swift")
print("After append('Swift'):", languages)

languages.insert(2, "Java")
print("After insert(2, 'Java'):", languages)

del languages[3]

print("After del languages[3]:", languages)
popped_language = languages.pop()
print(f"Popped language: {popped_language}")
print("After pop():", languages)
languages.remove("Java")
print("After remove('Java'):", languages)
print("Temporarily sorted:", sorted(languages))
print("List remains original after sorted():", languages)
print("Temporarily sorted in reverse:", sorted(languages, reverse=True))
languages.reverse()
print("After reverse():", languages)
languages.sort()
print("After sort():", languages)
languages.sort(reverse=True)
print("After sort(reverse=True):", languages)
print("Number of languages in list:", len(languages))
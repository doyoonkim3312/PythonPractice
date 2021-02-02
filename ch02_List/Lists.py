# Declare List
languages: list = ['Python', 'Java', 'Kotlin', 'Swift']
print(languages)
counter = 0

for element in languages:
    print(element)

    # Python does not have ++ or -- operators
    counter += 1

print(counter)

# Accessing Element in Lists
# Index for accessing element in lists can be negative.
element1 = languages[0]
element2 = languages[1]
element3 = languages[-1]  # This indicates language[3] in this lists.

print(f"{element1} {element2} {element3}")

# Modifying Lists
fruits: list = ['Apple', 'Banana', 'Peach', 'Watermelon', 'Orange']

# Edit element
fruits[-1] = 'Mandarin Orange'
print(fruits)

# Add Element to the End of list
fruits.append('Blueberry')
print(fruits)

# Add Element to specific location
fruits.insert(1, 'Raspberry')
print(fruits)

# Remove Element from list (Using 'del' statement)
del fruits[-1]
print(fruits)

# Remove Element from list (Using 'pop()' method)
# The pop() method removes the last item in a list, but it lets removed element can be used later on.
# If parentheses is left blank, it will automatically removes very last element. If certain index is placed inside of
# parentheses, element in that location will be popped.
poppedElement = fruits.pop(0)
print(fruits)
print(f"Popped Element: {poppedElement}")

# Remove Element by Value
fruits.remove('Peach')
print(fruits)

# Organizing Lists

# Sorting List Permanently with sort() method
states: list = ['IN', 'IL', 'GA', 'NY', 'CA', 'MA', 'NH']
states.sort()
print(states)

# Sorting list in reverse
states.sort(reverse=True)
print(states)

# Sorting list temporarily with sorted() method
print(f"\nTemporarily Sorted (Descending): {sorted(states)}")
print(f"\nTemporarily Sorted (Ascending): {sorted(states, reverse=True)}")



scores = []

# Append scores
scores.append(85)
scores.append(90)
scores.append(78)
scores.append(92)
scores.append(88)

print("Scores after appending:", scores)

#Insert 80 at index 2
scores.insert(2, 80)
print("After inserting 80 at index 2:", scores)

#  Remove 92
scores.remove(92)
print("After removing 92:", scores)

# Sort ascending
scores.sort()
print("Sorted list (ascending):", scores)

# Reverse the list
scores.reverse()
print("Reversed list:", scores)

#  Find maximum and minimum score
print("Maximum score:", max(scores))
print("Minimum score:", min(scores))

# Check if 90 is in the list
if 90 in scores:
    print("90 is in the list")
else:
    print("90 is not in the list")

#  Print total number of scores
print("Total number of scores:", len(scores))

#  Slice and print first three scores
print("First three scores:", scores[:3])

# Iterate and print each score
print("All scores:")
for score in scores:
    print(score)

print("Original scores:", scores)

# Find the last element
last_element = scores[-1]
print("Last element in the list:", last_element)

#  Replace the score at index 2 with a new score (say 95)
scores[2] = 95
print("After replacing index 2 with 95:", scores)

# Create a new copied list
copied_scores = scores.copy()
print("Copied list:", copied_scores)
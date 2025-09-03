
scores = []
 
# question1
scores.append(85)
scores.append(90)
scores.append(78)
scores.append(92)
scores.append(88)
 
print("Scores after appending:", scores)
 
# question2
scores.insert(2, 80)
print("After inserting:", scores)
 
# question3
scores.remove(92)
print("After removing 92:", scores)
 
# question4
scores.sort()
print("Sorted list (ascending):", scores)
 
# question5
scores.reverse()
print("Reversed list:", scores)
 
# question6
print("Maximum score:", max(scores))
print("Minimum score:", min(scores))
 
# question7
if 90 in scores:
    print("90 is in the list")
else:
    print("90 is not in the list")
 
# question8
print("Total number of scores:", len(scores))
 
# question9
print("First three scores:", scores[:3])
 
# question10
print("All scores:")
for i in scores:
    print(i)
#question 11
last_element=scores[-1]
print("last element",last_element)
#question12
scores[2]=89
print("after replacing",scores)
#question13
copy_scores=scores.copy()
print("copied list",copy_scores)
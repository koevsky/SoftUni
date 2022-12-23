age = int(input())
text = "drink"
if age <= 14:
    text += " toddy"
elif age <= 18:
    text += " coke"
elif age <= 21:
    text += " beer"
elif age > 21:
    text += " whisky"
print(text)
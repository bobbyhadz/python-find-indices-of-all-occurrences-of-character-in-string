# Find all indexes of a substring using startswith()

string = 'bobby hadz bobbyhadz.com'

indexes = [
    index for index in range(len(string))
    if string.startswith('bobby', index)
]

print(indexes)  # 👉️ [0, 11]
import re
# # 1
# string = input()
#
# if re.search(r'a[b]*', string):
#     print("Match found!")
# else:
#     print("Match not found.")

# # 2
# string = input("Enter a string: ")
#
# if re.search(r'a[b]{2,3}', string):
#     print("Match found!")
# else:
#     print("Match not found.")

# # 3
# string = input("Enter a string: ")
#
# pattern = '[a-z]+_[a-z]+'
#
# print(re.findall(pattern, string))

# # 4
# string = input("Enter a string: ")
#
# pattern = r'[A-Z][a-z]+'
# print(re.findall(pattern, string))

# # 5
# string = input("Enter a string: ")
#
# if re.search(r'a.*b$', string):
#     print("Match found!")
# else:
#     print("Match not found.")

# # 6
# string = input("Enter a string: ")
#
# pattern = r'[ ,.]'
#
# print(re.sub(pattern, ':', string))
#
# # 7
# s = input()
# s2 = ""
# if re.search("_", s):
#     k = re.split("_", s)
#     for j in k:
#         s2 += j.capitalize()
# print(s2)
#
# # 8
# string = input("Enter a string: ")
#
# pattern = r'[A-Z][a-z]*'
#
# print(re.findall(pattern, string))
# # 9
# string = input("Enter a string: ")
#
# pattern = r'([A-Z][a-z]*)'
#
# spaced_string = re.sub(pattern, r'\1 ', string)
# print(spaced_string)
#
# # 10
# string = input("Enter a camel case string: ")
#
# pattern = r'([A-Z])'
#
# snake_str = re.sub(pattern, r'_\1', string).lower()
#
# print(snake_str)

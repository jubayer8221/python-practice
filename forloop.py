# # # # fruits = ["apple", "banana", "cherry"]
# # # # for x in fruits:
# # # #     print(x)
# # # # print("Done")
# # # #
# # # # fruits = ["apple", "banana", "cherry"]
# # # # for f in fruits:
# # # #     print(f)
# # #
# # # # fruits = ["apple", "banana", "cherry"]
# # # # for x in fruits:
# # # #     if x == "banana":
# # # #         break
# # # #     print(x)
# # #
# # # # Dectionary
# # #
# # # customer = {
# # #     "name": "John Smith",
# # #     "age": 30,
# # #     "is_verified": True
# # # }
# # # customer["name"] = "Jubayer Al Mahmud"
# # # print(customer["name"])
# # #
# # #
# #
# #
# # phone = input("Phone: ")
# #
# # digits_mapping = {
# #     "1": "One",
# #     "2": "Two",
# #     "3": "Three",
# #     "4": "Four",
# #     "5": "Five"
# # }
# # output = ""
# # for char in phone:
# #     output += digits_mapping.get(char, "!") + " "
# # print( output )
#
#
# message = input(">")
# words = message.split(' ')
#
# emojis = {
#     ":)": "😊",
#     ":(": "😢"
# }
# output = ""
# for word in words:
#     emojis.get(word, word)
#     output += emojis.get(word, word) + " "
# print(output)



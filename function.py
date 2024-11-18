# # # def greet_user(name):
# # #     print("Hi there!")
# # #     print(f"Are you {name}?")
# # #     print("I'm so Fucked up! I need your help.")
# # #
# # #
# # # print("Start")
# # # greet_user("Jhon")
# # # print("Finish")
# # #
# # #
# # def greet_user(first_name, last_name):
# #     print(f"Hi {first_name} {last_name}!")
# #     print("Welcome!")
# #
# # print("Start")
# # greet_user(first_name="Jubayer", last_name="Al Mahmud")
# # print("Finish")
# #
# #
# #
#
# def square(number):
#     print(number*number)
#     # return number*number
# print(square(3))
# # result = square(3)
# # print(result)

message = input(">")

def emoji_converter(message):
    words = message.split(" ")

    emojis = {
        ":)": "😄",
        ":(": "😥"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


result = emoji_converter(message)
print(result)
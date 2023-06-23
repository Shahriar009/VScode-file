

'''numbers=[1,2,3,1,4,5,6,9,6,4,2]
print(numbers[7])'''
'''
coordinates = [7,5,9]
a,b,c = coordinates
print(b)
'''
'''
students = {
    "Name":"Shahriar Rahman",
    "ID":192_50_009,
    "is_regular": True
}
students["Name"]="RRR"
students["Section"]="A1"
print(students["Name"])
print(students["Section"])
print(students["ID"])
print(students["is_regular"])
print(students.get("CGPA", '4'))

'''
'''
phone=input("phone:")
digit_mapping={

    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "7":"Seven",
    "9":"Nine"
}
output=" "
for ch in phone:
    output+=digit_mapping.get(ch,"!") + " "
print(output)


'''
'''
phone=input("Phone:")
dictionary={

    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven"
}
output=""
for value in phone:
    output+=dictionary.get(value,'!')+" "
print(output)

'''
'''
message=input("--")
words=message.split(' ')
emojis ={
    ":)": " 😊",
    ":(": "😢 ",
    ":<": " 😎"
}
output=""
for word in words:
    output+=emojis.get(word,word)+" "

print(output)

message=input(":-")
words=message.split(" ")
emojis={
    "12":"😁╰(*°▽°*)╯╰(*°▽°*)╯:-D(*/ω＼*)",
    "YYY":"019817567889",
    "____":"😣"
}
output=" "
for word in words:
    output+=emojis.get(word,word)+" "
print(output  )
'''
def emoji_converter (message):
    words=message.split(" ")
    emojis={
        ":)":"😊",
        ":(":"😣"

    }
    output=" "
    for word in words:
        output+=emojis.get(word,word)+" "
    return output

message=input("---")

print(emoji_converter(message))
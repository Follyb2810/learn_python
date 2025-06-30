def square(num):
    return num * num

result =square(2)
print(result)

emoji = {
    ":)": "😀",
    ":(": "😌"
}

def emoji_converter(words: str):
    output = ''
    msg = words.split(' ')
    for word in msg:
        output += emoji.get(word, word) + ' '
    return output

arg = input('enter greeting >? ')
result = emoji_converter(arg)
print(result)

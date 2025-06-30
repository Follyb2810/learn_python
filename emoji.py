message = input('>')
word =message.split(' ')
print(word)

emoji ={
    ":)":"😀",
    ":(":"😌"
}
output=''
for chr in word:
    if(emoji.get(chr,chr)):
        output+= emoji.get(chr,chr)+' '
print(output)


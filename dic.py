customer ={
    "name":"folly",
    "age":2,
    "is_verified":True
}

print(customer["age"])
print(customer['is_verified'])
print(customer.get('name'))


word =input('Enter a number? ')
number_in_words ={
    "1":"one","2":"two","3":"three","4":"four"
}
ans =''
for chr in word:
    if(number_in_words.get(chr,'')):
        ans += number_in_words.get(chr,'') +' '
    else:
        continue
print(ans)

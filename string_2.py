
e = "Hari Yadav"
count = 0
for character in e:

    # if character  == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
    #     count = count +1

    if character in 'aeiou':
        count = count +1

    print(character)
print(count)

counter = 0
for vowel in 'aeiou':
    counter += e.count(vowel)
print(counter)
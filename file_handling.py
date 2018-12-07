# read -> r
# write -> w
# modify -> r+
# reading mechanism is sequential

sample_file = open('hello.txt', 'w')
# sample_file.write('Testing Testing')


# writing list of data in file
sample_file.writelines([
    '1st line\n'
    '2nd line\n'
])


# serialization, json, pickle

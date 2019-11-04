with open('working_in_text_file.txt', 'w') as text_file:
    text_file.write('This is python class')

with open('working_in_text_file.txt', 'r') as reading_text_file:
    for line in reading_text_file:
        print(line)

with open('working_in_text_file.txt', 'r+') as appending_text_file:
    for line in appending_text_file:
        pass
    appending_text_file.write('\ncurrently running\n')



## merge two file
file_content = ''
with open('working_in_txt.txt', 'r') as reading_file:
    for line in reading_file:
        file_content += line

with open('sample.txt', 'r') as reading_file:
    for line in reading_file:
        file_content += line

with open('merged_file.txt', 'w') as merge_file:
    merge_file.write(file_content)

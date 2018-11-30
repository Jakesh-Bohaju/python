
#Calculate percentage and total marks
marks = '90, 80, 70, 60, 55'
marks_list = marks.split(',')
total_marks = 0
for i in marks_list:
    markss = int(i)
    print(type(markss))
    total_marks = total_marks + markss

percentage = total_marks/5
print("Percentage : ", percentage)
print("Total marks : ",total_marks)



#output : ['Mr Ram','Mr Shyam','Mr Hari']
names = 'Ram , Shyam, Hari'
name_list = names.split(',')
another_name_list = []
for name in name_list:
    name_with_mr = 'Mr ' + name.strip()
    another_name_list.append(name_with_mr)
print(another_name_list)
another_names = ','.join(another_name_list)
print(
    another_names
)


#count the gmail address
email = 'abc@gmail.com, xyz@yahoo.com, sde@gmail.com, dfg@gmail.com, wed@hotmail.com, xash@gmail.com'
email_list = email.split(',')
# new_email_list = []
count = 0
for mail in email_list:
    # print(type(mail))
    # print(mail)
    if '@gmail.com' in mail:
        # new_email_list.append(email_list)
        count = count + 1
print(count)
# print(new_email_list.count())

#print first name only, applicable only for name without middle name
# full_name = 'John Doe,Jakesh Bohaju,Hari Yadav,Sita Shrestha'
# full = full_name.replace(' ',',')
# full_name_list = full.split(',')
# # print(full_name_list)
# first_name = full_name_list[0::2]
# print(first_name)

#print first name only
full_name = 'John Doe,Jakesh Bohaju,Hari Bahadur Yadav,Sita Shrestha'
full_name_list = full_name.split(',')
new_first_name = []
for first_name in full_name_list:
    print("Full name in loop : ", first_name)
    print("Data type come inside loop : ", type(first_name))
    a = first_name.replace(' ',',')
    print("After replace : ", a)
    print("Data type after replace : ", type(a))
    b = a.split(',')
    print("After split : ", b)
    print("Data type after split : ",type(b))
    c = b[0]
    print("First name : ",c)
    print("Data type of first name result : ", type(c))
    new_first_name.append(c)
print(','.join(new_first_name))


#Another method for first name
full_names = 'Ram han,Erlic bhattrai,hari kanda'
full_names_split = full_names.split(',')
first_names_list = []
for name in full_names_split:
    first_names_list.append(name.split(' ')[0])
print(','.join(first_names_list))
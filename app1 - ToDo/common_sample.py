# file = open('members.txt', 'r')
# members = file.readlines()
# file.close()
# members.append(input('Enter new member: ') + '\n')
#
# file = open('members.txt', 'w')
# file.writelines(members)
# file.close()
################################
# i = 5
# while i != 0:
#     i = i - 1
#     file = open(f"{i}", 'w')
#     file.write('Hello world' + '\n')
#     file.close()
#################################
# files = ['a.txt', 'b.txt', 'c.txt']
# for file_name in files:
#     file = open(file_name, 'r')
#     print(file.read())
#################################
# names = ["john smith", "jay santi", "eva kuki"]
# print([i.title() for i in names])

# usernames = ["john 1990", "alberta1970", "magnola2000"]
# print([len(i) for i in usernames])

# user_entries = ['10', '19.1', '20']
# print([float(i) for i in user_entries])

# user_entries = ['10', '19.1', '20']
# user_entries = [float(i) for i in user_entries]
# print(sum(user_entries))
#################################
# name = '1'
# thought = input('how you have thoughts?\n')
# with open(f'files/{name}.txt', 'a') as file:
#     file.write(thought + '\n')
#################################
# grades = [9.6, 9.2, 9.7]
#
#
# def get_max(grades):
#     max_list = max(grades)
#     min_list = min(grades)
#     print(f'Max: {max_list}')
#     print(f'Min : {min_list}')
#     return max_list, min_list
#
#
# maxi, mini = get_max(grades)
#################################

# def calculate_birth(current_year=2023):
#     year_of_birth = int(input('What is your of brith? '))
#     cnt_year = current_year - year_of_birth
#     if cnt_year > 120:
#         print('you should be dead')
#         return cnt_year
#     print(cnt_year)
#     return cnt_year
# calculate_birth()
#################################
# def separate_name(names:str):
#     cnt_names = len(names.split(','))
#     print(cnt_names)
#     return cnt_names
# separate_name('Nikita,Masha,Sasha')
#################################
# stgg = 'ffffggggfgdfgdfgdf'
# print(stgg.count('f'))
#################################
import time
now = time.strftime('%Y, %b, %d %H:%M:%S')
print(now)
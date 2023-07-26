import glob

my_files = glob.glob('../files/*.txt')

for filepatn in my_files:
    print(filepatn + '\n' + '-------------------')
    with open(filepatn, 'r') as file:
        print(file.read().upper())

'''///////////////////////////////////////////'''
import webbrowser
user_term = input('Enter a search term: ')
webbrowser.open('https://www.google.com/search?q=' + user_term)

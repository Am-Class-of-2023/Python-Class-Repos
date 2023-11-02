import requests
# API KEY and URL

API_KEY = 'iuhhPyMAUZiVawZs4WdNeDvxCVh7ht6qJVisccWu'

URL = "https://api.nasa.gov/planetary/apod?api_key=" + API_KEY

response = requests.get(URL).json()

def make_file(thing):
    with open('link.txt', 'w') as fp:       #fp means file pointer
        fp.write(thing)


def open_file(name = 'link.txt'):
    with open(name, 'r') as text:
        line = text.read()
        return line


make_file(response['hdurl'])


# Ask for an Astronomy picture of the day
e = input('Would you like Astronomy picture of the day?: ')
if e == 'yes':
    print(open_file() + '\n' +
          ' Here you go!!')
else:
    print('eRrOr')

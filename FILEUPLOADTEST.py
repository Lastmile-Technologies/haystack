import requests
import os
url = 'http://localhost:8000/file-upload'
headers = {'Accept': 'application/json'}
folder_path= 'uploadDocs'
files = {}
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        print(filename)
        # with open(file_path, 'rb') as file:
        files = {'files': (filename, open(file_path, 'rb'))}
        response = requests.post(url, headers=headers, files=files)

# files = {'files': ('one.txt', open('one/Common questions1.txt', 'rb'))}

# response = requests.post(url, headers=headers, files=files)

print(f'Status Code: {response.status_code}')
print('Response Content:')
print(response.text)
print(files)
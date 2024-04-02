import requests

url = 'http://127.0.0.1:5000/process_file'
file_path = r'D:\Tobetested\Python_API_test'
data = {'file_path':file_path}
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()['result']
    print(result)

else:
    print('Error:', response.text)

url = 'http://127.0.0.1:5000/calculate'
value_a = 100
value_b = 200
data = {'value_a': value_a, 'value_b': value_b}
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()['result']
    print(result)

else:
    print('Error:', response.text)

url = 'http://127.0.0.1:5000/calculate_sub'
value_a = 20
value_b = 0
data = {'value_a': value_a, 'value_b': value_b}
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()['result']
    print(result)

else:
    print('Error:', response.text)

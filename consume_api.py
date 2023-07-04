import requests


response = requests.get('https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

#print(response.status_code) # will return status code 200 

# print(response.json()['items'])

# loop over json notation key:value pairs 

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print("skipped")
    print()

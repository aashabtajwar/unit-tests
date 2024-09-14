import time
import requests

def get_feed():
    data =  '''
    <h1>Title</h1>
    <p>Sample paragram that explains the title</p>
    '''
    delay()
    return data

def delay():
    time.sleep(5)



def get_user(user_id):
    url = f'https://jsonplaceholder.typicode.com/todos/{user_id}'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return 'Could not fetch user'

get_user(1)

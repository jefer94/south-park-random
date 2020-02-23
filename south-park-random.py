from bs4 import BeautifulSoup
from requests import get
import webbrowser
import re

url = 'https://southpark.cc.com'

def random_url():
  response = get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  path = soup.select_one('[class="random-episode"]')['href']
  return url + path

def get_episode_url(code):
  response = get('https://southpark.cc.com/episodios-en-espanol/' + code)
  return response.url

def open_random_episode(page):
  response = get(page)

  if response.status_code == 200:
    return get_code(response.url)

def get_code(text):
  return re.search(r'(s[0-9]+e[0-9]+)', text).group(1)

if __name__ == '__main__':
  random_url = random_url()

  code = open_random_episode(random_url)

  if isinstance(code, str):
    episode_url = get_episode_url(code)
    webbrowser.open(episode_url, new=0)
    print('Done! ' + episode_url)
    
  else:
    print('Server is busy')
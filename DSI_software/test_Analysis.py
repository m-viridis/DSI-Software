import pytest
import Analysis
from user_config import usertoken

test_names = []
test_stars = []
star = ['3', '6'] #use variable to test error message

def test_load_data() -> dict:
  res = requests.get(url='https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={'Authorization': 'Bearer' + usertoken})

  res_json = res.json()
  res_dicts = res_json['items']
  #return res_json

  for item in res_dicts:
    test_names.append(item['name'])
    test_stars.append(item['stargazers_count'])
    pass

test_load_data()

if all(type(item) is int for item in stars):
  print('The GitHub data for the stars variable is the correct type.')
else:
  raise TypeError ('The stars variable can only contain integers.')
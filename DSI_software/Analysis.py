#import libraries

import requests
import json
import matplotlib.pyplot as plt
import numpy as np

from google.colab import userdata #for personal testing

#import yaml user_config; extract user token

import yaml
with open('/configs/user_config.yml', 'r') as user_config:
  ghtoken = yaml.safe_load(user_config)

usertoken = list(ghtoken.values())[0]

#create empty lists for GitHub data
names = []
stars = []

def load_data() -> dict:
  '''Extract data for the most starred repos from GitHub and store data in the above lists'''
  res = requests.get(url='https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={'Authorization': 'Bearer' + usertoken})

  res_json = res.json()
  res_dicts = res_json['items']
  #return res_json

  for item in res_dicts:
    names.append(item['name'])
    stars.append(item['stargazers_count'])
    pass

load_data()
print(stars)

def compute_analysis(x, y, ax=None):
  '''Use extracted GitHub data to plot a bar chart with a line for the mean for total stars'''
  plt.figure()
  plt.barh(names, stars)
  plt.title("Most starred GitHub repos")
  plt.axvline(np.mean(y), color='red', label='mean')
  plt.legend(bbox_to_anchor = (1.0, 1), loc = 'upper right')
  plt.show()

compute_analysis(names, stars)

import requests
import json
import numpy as np
from typing import Any, Optional
import yaml
from google.colab import userdata #for personal testing

# n.b. this module will not read in system_config because we will not be plotting anything with this package
# however, there is a system_config.yml file in the package for you to review
# to see homework related plotting of GitHub data, please see https://github.com/m-viridis/DSI-SQL/blob/main/DSI-HomeworkSummary-2024-01-16.ipynb 

# import and read user_config with yaml to extract user token as a global variable
with open(r"..\configs\user_config.yml") as user_config:
  ghtoken = yaml.safe_load(user_config)

usertoken = list(ghtoken.values())[0]
print(usertoken)

class Analysis():

  def __init__(self, analysis_config:str):
    '''stick usertoken to self'''
    config = []
    config.append(usertoken)

    self.config = config

  def load_data(self):
     '''extract data for the most starred repos from GitHub and store data in 'stars' variable'''

     res = requests.get(url='https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={'Authorization': 'Bearer' + usertoken})
     res_json = res.json()
     res_dicts = res_json['items']

     stars = []

     for item in res_dicts:
       stars.append(item['stargazers_count'])
     return stars


  def compute_analysis(self): #creates local variable
    '''calculate mean for stars'''

    return sum(stars)/len(stars)


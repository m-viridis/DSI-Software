import requests
import json
import numpy as np
from typing import Any, Optional
import yaml
import argparse

# this version runs in a shell wherein you need to provide your API token

parser = argparse.ArgumentParser(description='ask for user API token',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('APIToken', help='API Token')
args = parser.parse_args()
usertoken = vars(args[0])

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
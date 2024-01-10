#INTRO<br>

A basic package with GitHub API code that returns data on the top starred repos.<br>

NOTE: This code will not successfully execute as instructed. Please refer to https://github.com/m-viridis/DSI-SQL/blob/main/DSI-Final-2024-01-16.ipynb to see how the code ran in Google Colab. <br>

#API TOKEN INSTRUCTIONS<br>

In order to run this package, you need to change the value of user_config.yml to include your personal GitHub API Token. It should start with 'github_' followed by a long alphanumeric string. <br>

For more instructions on generating your own Github API token, please see https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens<br>

#CLASS OBJECTS<br>

Thank you for being so forthcoming in the structure of the code you are expecting to receive. Unfortunately, being able to successfully execute that structure requires an understanding of Class objects which we only glanced over in the python course. I tried to figure out class objects on my own beyond a rudimentary level and haven't received any feedback - understandable given the tight time frame - as such, I am submitting my code without using class objects. I can see how incredibly powerful these objects could be and wish that there had been time to cover them in more detail, livecode multiple examples and practice writing them. Given their general importance, ideally there would have been an exercise or assignment using Objects. <br>

#UNIT TEST <br>

I understand the concept of unit testing conceptually and can reproduce variations of the livecoding exercises. However, given that the data being pulled from GitHub is live and therefore changing, I opted to verify data type instead of data value. If the data type is incorrect, an error message is raised. It's possible to verify the top repo name as that spot appears to outrank the other repos by a significant margin but if a user executes this code 5 years later or after a different repo "goes viral" the top spot might be taken by a different repo.  <br>

#INCORRECT PATH FOR CONFIG FILES <br>

I tried three different variations of the package file structure for the yaml files - in \DSI-Software, in \DSI_software and \configs. Unfortunately, when I pip install the package and try to call the function, python cannot find the user_config file. I'd hard code the path in but that would create another problem for the user. <br>

#EARLY SUBMISSION <br>

I have reviewed the SQL course, its exercises and assignments, and if it is anything like this course, I absolutely will not have time to work on this assignment past today. <br>

#INTRO<br>

A basic package with GitHub API code that returns data on the top starred repos.<br>

NOTE: This code will not successfully execute in the shell (see INCORRECT PATH FOR USER_CONFIG) Please refer to https://github.com/m-viridis/DSI-SQL/blob/main/DSI-FINALAssignment-Analysis_Class.ipynb to see how the code ran in Google Colab. <br>
To review the course homework including a previous version of Analysis that included plotting data, please refer to https://github.com/m-viridis/DSI-SQL/blob/main/DSI-HomeworkSummary-2024-01-16.ipynb.<br>

#API TOKEN INSTRUCTIONS<br>

In order to run this package, you need to manually edit the value of user_config.yml to include your personal GitHub API Token. It should appear to be a long alphanumeric string. <br>

For more instructions on generating your own Github API token, please see https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens<br>

#RUNNING ANALYSIS MODULE INSTRUCTIONS<br>

You may use the following code to determine the mean of total stars for the top starred GitHub repos:

analysis = Analysis(usertoken)
Analysis.load_data(analysis)
stars = Analysis.load_data(analysis)
Analysis.compute_analysis(stars)

#UNIT TEST <br>

NOTE: I understand the concept of unit testing conceptually and can reproduce variations of the livecoding exercises. However, given that the data being pulled from GitHub is live and therefore changing, I opted to verify data type instead of data value. If the data type is incorrect, an error message is raised. It's possible to verify the top repo name as that spot appears to outrank the other repos by a significant margin but if a user executes this code 5 years later or after a different repo "goes viral" the top spot might be taken by a different repo.  <br>

#INCORRECT PATH FOR USER_CONFIG.YML <br>

I tried many different variations of a path to point to user_config.yml including by changing the package file structure and the code directly according to https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-when-writing-windows. Unfortunately, when I pip install the package and try to call the function, python simply cannot find the user_config file. I'd hard code the path in but (1) that would mean the user would need to manually edit Analysis.py and (2) I wouldn't know the path in Google Colab anyway. <br>

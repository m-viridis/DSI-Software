#INTRO<br>

A basic package with GitHub API code that returns data on the top starred repos.<br>

NOTE: There are two versions of Analysis: Analysis.py and Analysis_shell.py. Please refer to https://github.com/m-viridis/DSI-SQL/blob/main/DSI-FINALAssignment-Analysis_Class.ipynb to see how Analysis.py and ran in Google Colab. <br>
To review the course homework including a previous version of Analysis that included plotting data, please refer to https://github.com/m-viridis/DSI-SQL/blob/main/DSI-HomeworkSummary-2024-01-16.ipynb.<br>

#API TOKEN INSTRUCTIONS<br>

In order to run this package, you need to manually edit the value of user_config.yml to include your personal GitHub API Token. It should appear to be a long alphanumeric string. <br>

For more instructions on generating your own Github API token, please see https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens<br>

#RUNNING ANALYSIS.PY MODULE INSTRUCTIONS<br>

You may use the following code to determine the mean of total stars for the top starred GitHub repos:<br>

analysis = Analysis(usertoken)<br>
Analysis.load_data(analysis)<br>
stars = Analysis.load_data(analysis)<br>
Analysis.compute_analysis(stars)<br>

#ANALYSIS_SHELL.PY MODULE<br>

This is an alternate version of Analysis.py provided solely for grading purposes. The main difference is that instead of reading in an API token with user_config.yml, running Analysis_Shell.py in a shell means the user can enter their API token directly into the shell without having to manually open and edit any files. A little prompt appears if the user tries to run the program without entering their token. The rest of the program is the same as Analysis.py.<br>

#UNIT TEST <br>

NOTE: I understand the concept of unit testing conceptually and can reproduce variations of the livecoding exercises. However, given that the data being pulled from GitHub is live and therefore changing, I opted to verify data type instead of data value. If the data type is incorrect, an error message is raised. It's possible to verify the top repo name as that spot appears to outrank the other repos by a significant margin but if a user executes this code 5 years later or after a different repo "goes viral" the top spot might be taken by a different repo.  <br>

#INCORRECT PATH FOR USER_CONFIG.YML <br>

After a pip install, Analysis.py is unable to point correctly to the config.yml file. I tried many different solutions. Changing variations of the path in Analysis.py. Changing the package file structure. Changing how the file path itself is represented according to https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-when-writing-windows. I can verify that Google Colab stores the config files to /local/lib/python3.10/dist-packages/DSI_software and retrieves Analysis.py properly from there, I can't get it to read the yaml files in local/configs without hardcoding - which would break the code in different environments. Again, I've provided examples of the code properly running in the DSI-SQL repo. <br>

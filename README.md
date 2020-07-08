# article-analysis
For Larsen's sentiment analysis of articles


## poll_project
#### based on this tutorial (https://prettyprinted.com/tutorials/creating-a-poll-app-in-django) and the djangoproject online tutorial
- Currently, this code creates a website with django (requires installation) that can be run through the command line (python manage.py runserver)
- The website has a home page and a create page. The create page can create polls by inputing a quesiton and three options; the poll then appears on the home page
- Anyone with access to the website (currently only local access) can then vote on the polls. Results can be viewed on the website but also through the django API, and can be stored to a database later
- THE PROBLEM: right now, we could pull article samples and manually paste them into each new poll, but that would be really slow and inefficient. However, I don't know how to create a python script that can interact with the website and create polls from the SQL query sample-pull
- IDEA: I think a solution is to create a method (method.py) that can create a form from the SQL query -- then the method could be called from the command line and create polls that way. Right now, the only method in the code is one that stores option and option_count variables.
- There are many tutorials and the django online guide is pretty comprehensive but it is difficult for me to follow having never done something like this before

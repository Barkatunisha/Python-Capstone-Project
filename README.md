# Python-Capstone-Project
Final assessment of Python Training 
I have created templates folder and added html in a separate template using "render template" to avoid messy code. 
Add py and html files inside the folder in vs code like i showed in screenshot and run the program
Website: http://127.0.0.1:5000

Steps:
1. Imported libraries of flask,request,render template, pandas,random
2. intialized flask app and gave API key. Generated from TMDB by giving all details like phone num, email and address. IMDB requires AWS server details, OMDB only has 1000 daily limit hence unable to get API key from those websites.
Created function to get movies data using base URL from IMDB documentation.
Created another function to get random movie data and sorted by popularity desc
created homepage route using render template created for html file and to handle movie and random movie search
last 70 and 71 code is to run the flask app. 


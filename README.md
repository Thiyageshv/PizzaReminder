# PizzaReminder
This is the Django backend of an app that alerts you whenever you want pizza or groceries as soon as it finds your flatmate or friend near the right kind of store. REST framwork is used and YELP API is employed for getting results based on search term and location coordinates. The app also comes with a location simulation tool that we used for testing. 
The tool relies solely on Javascript and uses Jquery AJAX to contact with the server. 
 #Execution
 The Django server can be established as 
 python manage.py runserver 
 
 In your local system go to http://127.0.0.1:8000/static/map.html to access the simulation tool. 
 
 If you want to execute the tool in a different system, make sure to run the django server on any other interface than local interface and include that URL in the Jquery requests. 
 


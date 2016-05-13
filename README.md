# PizzaReminder
This is the Django backend of an app that alerts you whenever you want pizza or groceries as soon as it finds your flatmate or friend near the right kind of store. REST framwork is used and YELP API is employed for getting results based on search term and location coordinates. The app also comes with a location simulation tool that we used for testing. 
The tool relies solely on Javascript and uses Jquery AJAX to contact with the server. 
 
## Execution
The Django server can be established as 
python manage.py runserver 
 
In your local system go to http://127.0.0.1:8000/static/map.html to access the simulation tool. 
If you want to execute the tool in a different system, make sure to run the django server on any interface other than local interface and include that URL in the JQuery requests. 
For instance, PUT or POST requests ahve the following structure 
 
```
 $.ajax({
			    type: "PUT",
			    url: "http://127.0.0.1:8000/users/" '' Change URL. ,
			    contentType: "application/json",
			    data: dataobject,
				success: function (msg) {console.log(msg);} //call back fucntion
			});
		
```
```
var url = "http://127.0.0.1:8000/tasks/?"+"term=" + search + "&groupid=" + groupid + "&userid=" + userid;
var searchrequest = $.get(url, function(data, status){// callback function}
```
## REST Endpoints
The Rest URLs support three end points. users, sets and tasks

endpoint users: GET,PUT and POST access. 
Fucntionality: GEt requests returns the userid, username, current location coordinates of the users in the databse in form of json messages.. POST and PUT requests lets one modify the table. 
Example url: curl -X PUT http://127.0.0.1:8000/users/ -d ‘{“userid”:”rakhi", “Lat”:”0”,”Long”:”0”}’ -H "Content-Type: application/json"
n

endpoint sets: GET,PUT and POST access
Fucntionality: GET request accepts groupid as the parameter and returns all the users who are in the group with their userids. PUT request modifies the tuples corresponding to particular row in the table. These requests are used when removing a member from the group or adding a member to a group. POST requests are used to create groups. It passes a groupid as a parameter and an array of all memebers of the to-be created group. The groupid is a randomly generated id using the userid's of the group and current timestamp. This is to make sure that they are distinguished. 
These requests can be sued whenever a user wants to create a group (just like in Whatsapp ot Splitwise).


endpoint tasks: GET access only. 
Functionality: Accepts search term, userid and groupid as parameters, and returns the restaurants or stores that are near each user in the group. If the user is not moving, for isntance if there is no update in their locations to the database for more than some time then those users are not considered for the search. 
Example url: "http://127.0.0.1:8000/tasks/?term=pizza&groupid=123456&userid=9655208893"


Note that for PUT requests one need not pass all paramters. However for POST, all the parameters should be passed to the endpoint. 



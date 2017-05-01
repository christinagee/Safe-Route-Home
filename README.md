
# Safe-Route-Home
Route Home is an application that allows you to get from Point A to Point B without hassle. To visit our website
please go to: 

[https://safe-route-home.herokuapp.com/]

## How does it work?
We pulled from the Boston Crime data set located on the boston.gov website. We were fortunate that the dataset was clean so we did not have to format the data further. When the user fills out the location form all the data points are passed through the URL parameters, and the crime database is filtered based on the user's safety requirements indicated by the checkboxes. The database is then iterated through into a python dictionary which is passed to MapQuest as a JSON object of crime points to avoid along with the start and end location. Map Quest then returns to Django another JSON object which contains various navigation information and step by step directions. We then parsed through that data and iterate over it into our HTML template.


## Developer Guide

  <br />Open your command line and navigate to the folder you want to install the program. 
  
  #### In your command line:

  `mkdir Safe-Route-Home`

  `virtualenv .`

  #### Go to the github repository and clone it: 
  <a href="https://github.com/christinagee/Safe-Route-Home">https://github.com/christinagee/Safe-Route-Home</a>
  
  `git clone https://github.com/christinagee/Safe-Route-Home`

  #### Navigate to the subfolder:
  
  `cd Safe-Route-Home`

  #### Install all the necessary programs:  

  `pip install -r requirements.txt`

  ####  Run the webpage using Django:  

  `python manage.py runserver`
  
### Usage


Once you run the program in your terminal, click on the link http://127.0.0.1:8000/, or the link posted in the terminal.  

You will be directed to the website, and can navigate through the website via the home page, about, team, and readme pages (where you are now!).   


The inputs the webpage gets is location a, b, and events to avoid. You will not need to input any other data or files.  

  <p>If you ever return to the file to run the program again, go to the Safe-Route-Home folder, and in your terminal, activate your virtual environment by writing:</p>
 
 `source bin/activate`



## License
We are licensed by the MIT Creative Commons.

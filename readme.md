
# VinSauvage
This is a submission for the 3rd milestone project of the [codeinstitute](codeinstitute.net) Full Stack Developer bootcamp. The aim of the project is to showcase skills gained from following the Datacentric Development Module as well as the use of other coding skills. The project brief calls for an interactive datacentric recipe website able to demonstrate ability to effect CRUD functionality (CREATE, READ, UPDATE, DELETE) using MongoDB. 

##Design choices
This website has developed following mobile first principles though for speed it began using a preformed bootstrap template. This was then customised to accomodate design for a small device then progressively styled responsively for other device sizes. There are many similar websites to use as models for this principle and many were consulted for inspiration. I sought to use mobile first principles to produce a fresh looking website that would inspire users to wish to try and share recipes using wild produce available in the beautiful Savoie region. 

## Database Schema
I used the non-relational db engine [MongoDB]() which .... . Database scheme that I used is very simple. It connected users with recipes as one to many relationship. It means that one user could make as many recipes as he can, but one recipe can belong only to one user. 

USER ===> [recipe1, recipe2,recipe3] 
recipe1 ===> USER
recipe2 ===> USER

## UX/UI
### UI
The project wireframes were produced using [figma]() and are provided here:

Considering the natural produce used in the recipes I chose to mirror tones found in Savoie coutryside and the produce used for making VinSauvage. A colour palette was generated using the [coolors](https://coolors.co/) app. 
![palette]()

For ease of UI the fonts chosen were ones that are fresh and appealing 'Roboto 'and 'Ubuntu' was chosen for the site.

### UX
##### User stories
I use websites of this type to find recipes for foraged produce so I have considered the UX from my own perspective. A user can:
-   see purpose and goal of the website to promote enjoyment of natural produce
-   browse the site without being logged in as a registered user
-   navigate to recipes 
    - by category
    - filtering by main ingredient
    - filtering by author 
-   see the details of recipes
-   create a user profile, and log in and log out
-   via user profile can; add, edit and delete own recipes
-   change profile picture, first name, last name and username, email,
-   access the site in a responsive fashion on mobile, tablet or desktop device


## Features

##### Existing Features

The site can be used as a guest or as a logged in user, however, some features are only available to logged in users.

Any visitor of the site can view three latest recipes in the homepage,  by pressing menu button user can choose BROWSE option and see all recipes that is created on the website. There is also a possibility to filter recipes by author by clicking on author name.

Visitors have the option of create an account. Information required to create an account is First name, Last name, Username (which must be unique), password and profile picture(which is set to default), but after registration should be updated in account section . The First name, Last name and Username are stored as plain text but the password is stored in a hashed format using bcrypt. Profile picture can be saved as .svg or .jpg format.

When a visitor has created an account and logged in they are given the option to Add a recipe to the system, Edit their recipes or Delete their recipe from the system. Users can view recipes they have added to the site by filtering recipe by author.

A user has the option to edit or delete a recipe that they have added to the site only. Editing the recipe allows the user to update/or add to the existing recipe information. Deleting the recipe permanently removes the recipe from the system.

The site features custom error pages for both 403 and 404 errors.

##### Future Features

**Images** - could be improved by letting the user to upload an image from their computer. Also a gallery of images for a smoothie would be a nice feature. Now it is only possible to add URL to youtube.com video with recipe guidlines.

**Reviews/Comments** - Add the system to allow users to leave a detailed review/comment about a recipe.

**User accounts** - Passwords are currently stored in a hash format but it is an important requirement to make sure that user logins are made more secure. Possibility to remind password.

**User Dashboard** - A dashboard where the user could update their details including password.


## Technologies Used

The website is designed using following technologies:

-   HTML
-   CSS
-   JavaScript
-   [Python](https://www.python.org/)
-   [Flask](http://flask.pocoo.org/)
-   [MongoDB]()
-   [jQuery](https://code.jquery.com/jquery-3.2.1.js)
-   [GitHub]()
-   [Heroku]()
-   [Line Awesome library](https://icons8.com/line-awesome)
-   [Bootstrap](https://getbootstrap.com/)
-   [Google Fonts](https://fonts.google.com/)

## Testing

Automated testing

Tests 

**Responsiveness Testing:**

Chrome and Firefox (Mozilla) Developer Tools were used extensively, as well as 

**User Testing:**

Manual tests were carried out and the testing process was as follows:

**Landing page**

-   

**Contact page**

-  

**User Account**

###### Register Page



###### Login Page
 -
 
###### Add Recipe

- 
###### Edit Recipe

-   
###### Delete Recipe

-   
###### My Recipes

-   
###### Logout

-  
**Recipe Page**

**Error Pages**

-  
## Test Findings

## Deployment

Deployment and version control was carried out using GitHub and Heroku. The repository location is as follows:


###Heroku Deployment 

To deploy Family Hub to heroku, take the following steps:

    Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

    Create a Procfile with the terminal command echo web: python app.py > Procfile.

    git add and git commit the new requirements and Procfile and then git push the project to GitHub.

    Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

    From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

    Confirm the linking of the heroku app to the correct GitHub repository.

    In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

    Set the following config vars:

Key 	Value
DEBUG 	FALSE
IP 	0.0.0.0
MONGO_URI 	mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT 	5000
SECRET_KEY 	<your_secret_key>

    To get your MONGO_URI read the MongoDB Atlas documentation here

    In the heroku dashboard, click "Deploy".

    In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

    The site is now successfully deployed.



## Credits

**Content**

All site images are royalty free from [unsplash](https://unsplash.com/) or [pixabay](https://pixabay.com/) and [unsplash](https://unsplash.com/).

**Code References**

-
-   [Side navbar](https://bootstrapious.com/p/bootstrap-sidebar)
-   [Project structure](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/)
-   [bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
-   [pagination](https://www.youtube.com/watch?v=hkL9pgCJPNk)
-   [profile picture](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars-legacy)
-   [blueprints](https://realpython.com/flask-blueprint/)
-   [picture handler](https://github.com/jmportilla) - code was taken from his course on [periendata](https://www.pieriandata.com/)
-   [Heroku deployment](https://github.com/AJGreaves/familyhub/blob/master/README.md#heroku-deployment)

**Acknowledgements**
 Thanks to my mentor Ignatius Ukwuoma for inspiring me to try to do this project.



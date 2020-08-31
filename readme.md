
# VinSauvage
This is a submission for the 3rd milestone project of the [codeinstitute](codeinstitute.net) Full Stack Developer bootcamp. The aim of the project is to showcase skills gained from following the Datacentric Development Module as well as the use of other coding skills. The project brief calls for an interactive datacentric recipe website able to demonstrate ability to effect CRUD functionality (CREATE, READ, UPDATE, DELETE) using MongoDB. 

##Design choices
This website has developed following mobile first principles though for speed it began using a preformed bootstrap template. This was then customised to accomodate design for a small device then progressively styled responsively for other device sizes. There are many similar websites to use as models for this principle and many were consulted for inspiration. I sought to use mobile first principles to produce a website balancing natural images with modern looking design in a website that would inspire users to wish to try and share recipes using wild produce available in the beautiful Savoie region. 

## Database Schema
I used the database engine [MongoDB](https://www.quackit.com/mongodb/tutorial/about_mongodb.cfm) MongoDB is a document-oriented NoSQL database used for high volume data storage. Instead of using tables and rows as in the traditional relational databases, MongoDB makes use of collections and documents. Documents consist of key-value pairs which are the basic unit of data in MongoDB. Database scheme that I used is very simple. It connected users with recipes as one to many relationship. It means that one user could make as many recipes as he can, but one recipe can belong only to one user. 

USER ===> [recipe1, recipe2,recipe3] 
recipe1 ===> USER
recipe2 ===> USER

## UX/UI
### UI
The project wireframes were produced using [figma]() and are provided here:

Considering the natural produce used in the recipes I chose to mirror tones found in Savoie coutryside and the produce used for making VinSauvage. A colour palette was generated using the [coolors](https://coolors.co/) app. 
![palette]()

For ease of UI the fonts chosen were ones that are stylish and appealing 'Raleway'and 'Lora' were deliberately retained for the site.

### UX
##### User stories
I use websites of this type to find recipes for foraged produce so I have considered the UX from my own perspective. A user can:
-   see purpose and goal of the website to promote enjoyment of natural produce
-   browse the site without being logged in as a registered user
-   navigate to recipes 
    - by category
    - filtering by author 
-   see the details of recipes
-   can; add, edit and delete recipes
-   access the site in a responsive fashion on mobile, tablet or desktop device


## Features

##### Existing Features

- The site can be used as a guest. 

- Guests can navigate between landing, about, recipe and contact pages, forms open to allow submission and updating of recipes, recipes can be deleted.

- Any visitor can view recipes on the recipe page. By pressing the add button they can add their own recipe.

- Clicking a recipe card opens the recipe for reading and offers options to update/delete.

- By pressing search by buttons user can choose to filter recipes by category and author.

- Users can edit categories by pressing the edit categories button. 

- By filling in a contact form users can contact the site owner, form requires fields to be completed. 



##### Future Features

**Simplify Navigation** - some aspects of navigation are not ideal/intuitive these shuld be addressed by new links and better positioning of buttons.

**Filtering** - add fitlering by recipe name and/or ingredients,
 
**Sign up/Sign in** - implement sign up and sign in pages and functions to register users and limit editing rights to registered users

**Reviews/Comments** - Add the system to allow users to leave a detailed review/comment about a recipe.

**User Dashboard** - A dashboard where the user could update their details including password. Passwords to be encrypted appropriately. 

**Error Pages**  The site should feature custom error pages for 403, 404 and 405 errors.
## Technologies Used

The website is designed using following technologies:

-   [HTML5](https://en.wikipedia.org/wiki/HTML5) is a software solution stack that defines the properties and behaviours of web page content
-   [CSS3](http://www.css3.info/) Cascading Style Sheets (CSS) is a style sheet language used for describing the look and formatting of a document written in a markup
-   [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/About_JavaScript) JavaScript is a light-weight, interpreted, object-oriented programming language used primarily for making interactive elements on web pages and applications. It was initially only used for browsers and web pages, but it has spread to many other environments and applications
-   [Python](https://www.python.org/) a versatile coding language
-   [Flask](http://flask.pocoo.org/) Flask is a micro web framework written in Python, providing tools to build web-applications
-   [MongoDB](https://account.mongodb.com/) a non-relational database
-   [jQuery](https://code.jquery.com/jquery-3.2.1.js) a Javascript library allowing ease of coding and manipulation of the DOM
-   [GitHub](https://github.com/) for version control during development
-   [Heroku](https://id.heroku.com/) platform for hosting website
-   [FontAwesome library](https://fontawesome.com) popular set of icons for use in CSS
-   [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/download/) Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development - provides new functions and can be accessed via CDN rather than using a library
-   [Bootstrap templates](https://getbootstrap.com/) source of web-template ideas
-   [Google Fonts](https://fonts.google.com/) source of wide range of convenient to use fonts

## Testing

Automated testing

Did not allow automated testing other than routine validation of cose at WS3, minor issues raised by this were corrected. 
Tests 

**Responsiveness Testing:**

Chrome and Firefox (Mozilla) Developer Tools were used extensively, as well as confriming the result of this testing using real devices of various display sizes and using different browsers. 

**User Testing:**

Manual tests were carried out and the testing process was as follows:

**Landing page**

- Check that page opens in common browsers 
- check that appearance is appropriate;
    - all content visible or accessible by scrolling
    - correct postions and sizing of elements for display size
- check that dropdown navigation responds appropriately to hover, unhover and click  
- check that other link buttons respond appropriately to hover, unhover and click
- confirm all links work

**Contact page**
- Check that page opens in common browsers 
- check that appearance is appropriate;
    - all content visible or accessible by scrolling
    - correct postions and sizing of elements for display size
- check that dropdown navigation responds appropriately to hover, unhover and click  
- check that other link buttons respond appropriately to hover, unhover and click
- confirm all links work
- confirm that form alerts user if send button is pressed without typing information in field
- confirm that successful send launches message sent page

**About page**
- Check that page opens in common browsers 
- check that appearance is appropriate;
    - all content visible or accessible by scrolling
    - correct postions and sizing of elements for display size
- check that dropdown navigation responds appropriately to hover, unhover and click  
- check that other link buttons respond appropriately to hover, unhover and click
- confirm all links work

**Recipe page**
- Check that page opens in common browsers 
- check that appearance is appropriate;
    - all content visible or accessible by scrolling
    - correct postions and sizing of elements for display size
- check that dropdown navigation responds appropriately to hover, unhover and click  
- check that other link buttons respond appropriately to hover, unhover and click
- confirm all links to recipes work

**Add recipe page**
- Check that page opens in common browsers 
- check that appearance is appropriate;
    - all content visible or accessible by scrolling
    - correct postions and sizing of elements for display size
- check that dropdown navigation responds appropriately to hover, unhover and click  
- check that other link buttons respond appropriately to hover, unhover and click
- confirm all links work 
- confrim that category drop down responds correctly
- confirm that on pressing 'add' button the information saves to database.
- confirm that cancel button does not add info and returns to recipe page

**Show recipe page**
- Check that page opens in common browsers 
- check that appearance is appropriate;
    - all content visible or accessible by scrolling
    - correct postions and sizing of elements for display size
- check that dropdown navigation responds appropriately to hover, unhover and click  
- check that other link buttons respond appropriately to hover, unhover and click
- confirm all links work 
- confirm that search dropdowns respond appropriately to hover, unhover and click and that each selection delivers appropriate content
- check that delete button leads to deletion of entry from MongoDB 

**Message sent page**
- Check that page opens in common browsers - only after successful messgae form submission (otherwise see ) 
- check that appearance is appropriate;
    - all content visible or accessible by scrolling
    - correct postions and sizing of elements for display size
- check that dropdown navigation responds appropriately to hover, unhover and click  
- check that other link buttons respond appropriately to hover, unhover and click
- confirm all links work
 -
 
###### Results of testing

This site was tested across multiple browsers (Chrome, Safari, Microsoft Edge, FireFox, Ecosia) and on multiple mobile devices (iPhone 5, OnePlus5 and OnePlus7 iPadMini and iPad-pro, Chrome/Firefox/Safari; MacBook Air, Asus and Jumper laptops; Chrome/Safari/Firefox) to ensure compatibility and responsiveness. A range of other devices including pixel2+pixel2XL, Galaxy S9, Nexus 4, iPhoneX and various desktop display sizes were simulated using [Responsive Design Checker](https://responsivedesignchecker.com/) and [The Responsinator](https://www.responsinator.com/). As a result of these tests:

- adjustments were made to the positions of page headings to ensure correct positioning below header bar on small devices.
- adjustments were also made to adjust the postion of recipe images and text on small and large devices

###### Outstanding issues

The navigation of the site is not as intuitive as I would like notably the use of two distinct recipe pages I would like to combine these in future to give a single consistent page whatever route of navigation is used.
I would have liked to add further search capabilities to the database.  


## Deployment

Deployment and version control was carried out using GitHub and Heroku. The repository location is as follows:

the sites are;


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

All site images are royalty free from [unsplash](https://unsplash.com/) or [pixabay](https://pixabay.com/).

**Code References**
This code draws heavily on that in the Code Institute Datacentric development module which has often been followed precisely. Additionally I have used other coding resources for snippets or ideas. 
-   [Project structure](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/)
-   [blueprints](https://realpython.com/flask-blueprint/)
-   [bootstrap theme](https://startbootstrap.com/themes/clean-blog/)
-   [Heroku deployment](https://github.com/AJGreaves/familyhub/blob/master/README.md#heroku-deployment)

**Acknowledgements**
 Thanks to my mentor Ignatius Ukwuoma who thoughtime did not allow him to review this project was greatly responsible for inspiring me to try to tackle it in such a short time.


##On Reflection

This project was achived in a very short time (approx. 1 week) against the deadline of the expiry of my Code Institute studentship, it is therefore rough around the edges but has served as a satisfying demonstration that I can achieve a working CRUD implementation with MongoDB under pressure. 

##Disclaimer

This is for educational use.
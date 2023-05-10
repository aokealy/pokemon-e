Pokemon Ecommerce
========
Welcome to my Pokemon Website where we will sell Pokemon items such as Graded cards and sealed products. 
I have always wanted to create a Pokemon Website and sell Pokemon stuff.
https://pokemon-e.herokuapp.com/

UX Design
========
The layout is simple where it makes it easy for users to see everything and have easy access in any view 


FEATURES 
========

* Django allows us to create a full functioning websites
* Postgres was used for static files 
* Allauth was used for Autentication 
* stripe was used for the payment system. 
* Website is design using mobile-first approach.
* SEO for good search optimisation 
* Sort by function 
* add to cart function 



TECHNOLOGIES 
=============
The following languages, frameworks, libraries, and tools were used to construct this project. 
* HTML
* CSS
* Bootstrap (https://getbootstrap.com/) : This project uses Bootstrap to simplify the development of the webpage
* Python 
* Django
* Sqlite3
* Heroku
* stripe 
* Postgres 

Frameworks:
=============
Bootstrap
==========

This is a front-end framework which is built using HTML and CSS. It makes it easy to create responsive websites using a grid system with screen-width breakpoints.
The homepage 'Most Popular' and 'New Products' functionality is partially provided by the Bootstrap Carousel feature.
Badges are used to provide the item count above the basket; they are also used to detail the status of each individual item status on the Order History page.

JQuery
==========

This is a JavaScript framework which enables easy manipulation of the Document Object Model (DOM) using JQuery syntax.
This was used to provide the interactive functionality for the homepage carousels. I customised some JavaScript code I found on the internet (see credits) in order to have multiple carousels on one page.

Font Awesome
==========

This is a font library which I have used to provide some context appropriate icons throughout the application. For example, the Basket icon.

Django
==========

This is a high-level python framework which provides advanced functionality with minimal effort from the developer.
The application is developed using Django and extensively uses built-in functionality and custom packages.

Django-allauth
==========

This package is an add-on app for Django which implements a third-party authentication system. It provides advanced functionality, such as the integration of external social authentication, e.g. allowing users to authenticate with your website using their Google account, in addition to local authentication.
For this application I have used this package for its additional security, as it will only permit a user to attempt to login with incorrect details 5 times before restricting their ability to do so. This is important given it is an ecommerce application. It also enabled me to develop the application using email address as the user login and remove the unneccessary username field in the custom user model.
Django-crispy-forms

This package renders Django forms using Bootstrap conventions and classes, effectively making the forms responsive and mobile-first.
It also permits customisation of form rendering, from layout, to individual field styles.
I have used this package throughout to provide better structured forms with responsive design.

Reference 
=============
- <https://wallpapersafari.com/w/qBP3Q1> Pokemon background
- <https://www.pngitem.com/middle/iRhoToh_pokemon-ex-cards-png-transparent-png/> Deoxys Image
- <https://d16hw7tbcsk68f.cloudfront.net/s3/cgccards-production/research/subcategories/pok_pop-series.png> Espeon Gold Star Graded
- <https://d16hw7tbcsk68f.cloudfront.net/s3/cgccards-production/research/subcategories/pok_e-series-v2.png> Celebi Graded
- <https://d16hw7tbcsk68f.cloudfront.net/s3/cgccards-production/research/subcategories/pok_promotional>
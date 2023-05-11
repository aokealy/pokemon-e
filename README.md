Pokemon Ecommerce
========
Welcome to my Pokemon Website where we will sell Pokemon items such as Graded cards and sealed products. 
I have always wanted to create a Pokemon Website and sell Pokemon stuff.
https://pokemon-e.herokuapp.com/

UX Design:
========
The layout is simple where I took layout of Project 5 walkthrough project but addded my own blend to it to make it feel like my own project.

Wireframes:
========
 - https://wireframe.cc/u9GpTB - Home Page
 - https://wireframe.cc/xLmyUQ - Products Page
 - https://wireframe.cc/dV5USk - cart
 - https://wireframe.cc/d71ubI - checkout

 
 
 
colours:
=========
The colours that were used in this webiste were to match the colours of pikachu.
- We have the colour yellow which matches the colour of pikachu's fur.
- The red colour was used to match pikachu's red cheeks.
- The black colour was use to match the ears, tail and eyes of pikachu.
- ![#f6e652](https://placehold.co/15x15/f6e652/f6e652.png) `#f6e652`
- ![#FF0000](https://placehold.co/15x15/FF0000/FF0000.png) `#FF0000`
- ![#000000](https://placehold.co/15x15/000000/000000.png) `#000000`

Typography:
========
The Typography that was used during this project was Bruno Ace.
- Bruno Ace draws inspiration from modern automotive logos. This techno geometric sans has a wide stance with a tall x-height for a strong look and appeal. Both a normal case and small caps font exists.
<img src="media/text-style.PNG">

Site Structure
========
The structure of the website opens up with the home page giving you an overview of everything you need on the page. 

front page
====
<img src="media/frontpage.PNG">

Products Page
====
<img src="media/products.PNG">

Product Item
====
<img src="media/productItem.PNG">

Profile
====
<img src="media/profile.PNG">

FEATURES:
========

* Django allows us to create a full functioning websites
* Postgres was used for static files 
* Allauth was used for Autentication 
* stripe was used for the payment system. 
* Website is design using mobile-first approach.
* SEO for good search optimisation 
* Sort by function 
* add to cart function 



TECHNOLOGIES:
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

Facebook Page:
========
- <img src="media/facebook-page.PNG"> Pictures of facebook page
- <img src="media/facebook-post.PNG">

References: 
=============
- <https://wallpapersafari.com/w/qBP3Q1> Pokemon background
- <https://www.pngitem.com/middle/iRhoToh_pokemon-ex-cards-png-transparent-png/> Deoxys Image
- <https://d16hw7tbcsk68f.cloudfront.net/s3/cgccards-production/research/subcategories/pok_pop-series.png> Espeon Gold Star Graded
- <https://d16hw7tbcsk68f.cloudfront.net/s3/cgccards-production/research/subcategories/pok_e-series-v2.png> Celebi Graded
- <https://www.pngitem.com/middle/owRRwJ_pokemon-cards-png-pokemon-alakazam-ex-transparent-png/> Alakazam ungraded
- <https://www.pngitem.com/middle/iTmmhRo_volcanion-ex-pokemon-card-hd-png-download/> Volcanion ungraded
- <https://www.pngitem.com/middle/hmmTooo_m-latias-ex-pokemon-card-hd-png-download/> Heatron ungraded
- <https://www.pngitem.com/middle/ihTmJwT_pokemon-cards-jumbo-pack-hd-png-download/> Melmetal sealed box
- <https://www.pngitem.com/middle/xbTxwJ_pokemon-tcg-booster-packs-and-promo-cards-kingdra/> Kingdra Ex sealed box
- <https://www.pngitem.com/middle/ihTmwRw_image-pokemon-tcg-hidden-fates-hd-png-download/> Motres, Zapdos and Articuno ungraded
- <https://www.pngitem.com/middle/iTmmiTo_burning-spark-theme-deck-pokemon-theme-decks-hd/> Burning Sparks theme deck sealed
- <https://www.pngitem.com/middle/iTmmiRT_pokemon-tcg-burning-shadows-hd-png-download/> Burning Shadows booster pack
- <https://www.pngitem.com/middle/wwoRho_mega-lucario-pokemon-cards-ex-and-gx-hd/> Lucaio Ex ungraded
- <https://d16hw7tbcsk68f.cloudfront.net/s3/cgccards-production/research/subcategories/pok_neo-v2.png> Japanese Lugia graded
- <https://d16hw7tbcsk68f.cloudfront.net/s3/cgccards-production/research/subcategories/pok_promotional-v2.png> Ash and Pikachu graded
- <https://www.cgccards.uk/Resources/images/grading/trading-cards/why-cgc-trading-cards-pokemon-crop.png?cb=2021-07-30> Trophy Pikachu graded
- <https://d16hw7tbcsk68f.cloudfront.net/s3/cgccards-production/research/subcategories/pok_original-series.png> Charizard graded
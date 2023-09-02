# AutoMarket
[Link to deployed site](https://automarket-2a9033a7b561.herokuapp.com/)
<hr>
AutoMarket is a full stack project allowing users to postlistings with their vehicle for sale. The project is built using Django framework for the backend and HTML, CSS, Bootstrap and JavaScript on the frontend. Automarket allows the users to create an account and perform CRUD functionality on their profile and listings. This project was created as part of Code Institute full-stack developer course.

![automarket Image](./assets/readme-images/main-image.PNG)

# Table Of Content

-   [User Experience](#user-experience)
    -   [User Stories](#user-stories)
    -   [Site Goals](#site-goals)
    -   [Scope](#scope)
-   [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
         -   [Overview](#overview)
         -   [EPICS(Milestones)](#epicsmilestones)
         -   [User Stories issues](#user-stories-issues)
         -   [MoSCoW prioritization](#moscow-prioritization)
         -   [GitHub Projects](#github-projects)
-   [Features](#features)
    -   [Navbar](#Navbar)
    -   [Footer](#Footer)
    -   [Home](#Home)
        -   [Hero Section](#hero-section)
        -   [Search Form](#search-form)
        -   [Recent Listings](#recent-listings)
        -   [Listing Card](#listing-card)
    -   [Listings Page](#listings-page)
    -   [Create Listing](#create-listing)
    -   [Profile Page](#profile-page)
    -   [My Listings](#my-listings)
    -   [My Favourites](#my-favourites)
    -   [Remove From Favourites](#remove-from-favourites)
    -   [Edit Listing](#edit-listing)
    -   [Delete Listing](#delete-listing)
    -   [View Listing](#view-listing)
    -   [User account and User account listings](#user-account-and-user-account-listings)
    -   [Sign In Page](#sign-in-page)
    -   [Sign Up Page](#sign-up-page)
    -   [Sign Out Confirmation](#sign-out-confirmation)
    -   [Edit Profile](#edit-profile)
    -   [Delete Profile Confirmation](#delete-profile-confirmation)
    -   [We are sorry to see you go](#we-are-sorry-to-see-you-go)
    -   [Password reset](#password-reset)
    -   [Password reset email sent](#password-reset-email-sent)
    -   [Enter a new password](#enter-a-new-password)
    -   [Password Reset Completed](#password-reset-completed)
    -   [Error Pages](#error-pages)
-   [Future Features](#future-features)
-   [Testing](#testing)
-   [Bugs](#Bugs)
-   [Technologies And Languages](#technologies-and-languages)
    -   [Languages Used](#languages-used)
    -   [Python Modules](#python-modules)
    -   [Technologies and programs](#technologies-and-programs)
-   [Deployment](#deployment)
    -   [Before Deployment](#before-deployment)
    -   [Deployment on Heroku](#deployment-on-heroku)
    -   [Creating A Fork](#creating-a-fork)
    -   [Cloning Repository](#cloning-repository)
-   [Credits](#credits)
    -   [Media](#media)
    -   [Code](#code)
    -   [Acknowledgements](#acknowledgements)
    -   [Comments](#comments)


## User Experience

### User Stories

1. As a developer I can set up a new Django project so that I can create the project's structure
2. As a developer I can connect database and media storage so that the user's stored data is stored successfully
3. As a developer I can deploy the application early so that I can confirm that the initial setup is working and can continue testing the application during development
4. As a developer I can create wireframes so that the layout of the website is clear for desktop and mobile
5. As a user I want the website to be responsive so I can view it on my mobile
6. As a user I want to be able to register an account so that I can have access to all functionality of AutoMarket.
7. As a registered user I want to be able to log in to my account so I can view my profile page, my listings, and my favourites.
8. As a registered user I want to be able to see my profile page so that I can update my information
9. As a registered user I want to be able to reset my password so that I can regain access to my account in case I forget my password
10. As a user I want to be able to view other user’s profiles so that I can get more information about the seller/buyer like location and phone number
11. As a registered user I want to be able to delete my profile and all my listings if I do not wish to use the services of AutoMarket.
12. As a user, I want to be able to see the most recent listings on the landing page so that I can quickly and easily discover the latest items available for sale
13. As a user I want to be able to see details about the listing such as a description, image, and seller’s details so that I can find suitable car options and make informed decisions before I contact the seller
14. As a user I want to be able to easily navigate through pages of listings so that I can view all the listings in an organised way (pagination)
15. As a registered user I want to be able to create a listing so that I can advertise my vehicle for sale.
16. As a registered user I want to be able to edit a listing so that I can correct any mistakes or adjust the listed price
17. As a registered user I want to be able to delete a listing so that it is not available for other users to view.
18. As a registered user I want to be able to see all of the listings I have created so that I can manage and keep track of the vehicles I have listed for sale.
19. As a site owner I want to ensure that the user is prompted with a notification message when performing CRUD operations or login/logout, and signup so that the user is informed about the outcome of the action taken
20. As a registered user I want to be able to send messages to the seller of the listing so that I can arrange viewings and ask questions about the listing. (Won't Have)
21. As a registered user I want to be able to send messages to the seller of the listing so that I can arrange viewings and ask questions about the listing. (Won't Have)
22. As a registered user I want to be able to view any messages I may have received so that I can keep track of communication with other users. (Won't Have)
23. As a registered user I want to be able to reply to messages so that I can connect with other users.
24. As a registered user I want to be able to save listings to my favourites so that I can keep track of my favourite listings, making it easier to revisit and compare later.
25. As a registered user I want to be able to view my favourite listings so that I can easily revisit them later
26. As a registered user I want to be able to remove listings from favourites if I am not interested in the listing anymore
27. As a User I can navigate through the website so that I can access different sections efficiently
28. As a user I can visit the home page so that I can quickly browse and find relevant car listings based on my preferences
29. As a non-authenticated user, I want to access the user profile pages of listing owners, so that I can view their contact details and listings, and I can also mark listings as favorites without those being visible to other users.
30. As a registered user I want to be able to send emails to the seller of the listing so that I can arrange viewings and ask questions about the listing.

### Site Goals

1. To provide the users with a place to advertise their cars.
2. To provide a range of available cars for sale to potential buyers.
3. To provide a place for the users to browse vehicles and find out the vehicle's price range.
4. To make the website available and functional on every device.

### Scope
The project aims to develop an online car listing platform called "AutoMarket" that facilitates users in listing, viewing, and managing vehicle listings. The platform will be responsive and user-friendly, providing features for user registration, listing creation, profile management, messaging, favoriting listings, and seamless navigation.

Key Features:

1. Initial Project Setup:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. Responsive Design:
-The website will be responsive, allowing users to access it on both desktop and mobile devices.

3. User Authentication:
- Users can register an account, providing access to all functionality of AutoMarket.
- Registered users can log in to view their profile, listings, and favorites.

4. Profile Management:
- Registered users can view and edit their profiles, including personal details and profile pictures.
- Users can reset their passwords in case they forget them.
- Users can delete their profiles and associated listings.

5. Listing Management:
- Users can perform CRUD on their listings with vehicles for sale.
- The most recent listings will be displayed on the landing page.
- Listings will include details, descriptions, images, and seller's information.

6. Pagination:
- Pagination will be implemented for easy navigation through pages of listings.

7. Favorites and Messages:
Registered users can save listings to their favorites for later viewing.
Users can send emails to connect with sellers, arrange viewings, and ask questions.

8. Notification Messages:
- Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.

Benefits:

1. User-Centric Experience: The platform focuses on the user's needs, allowing efficient browsing, listing creation, and communication.
2. Efficient Navigation: Users can easily navigate through different sections of the website for seamless access.
3. Effective Communication: Sending emails and notification messages features, enhance user communication and interaction.

## Design
### Colour Scheme
The website features a calming and professional color palette that combines shades of blue, violet, and green with complementary neutrals. <br>
Overall, this color scheme creates a professional and user-friendly environment, with subtle variations in hue and transparency to guide users' attention and enhance the visual appeal of the website.
![Colour Scheme](./assets/readme-images/colour-palette.PNG)

### Database Schema
![database schema](./assets/readme-images/database-schema.png)

#### Models
1. Allauth User Model

The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, hence why changes directly to this model are not advisory. The User model is connected to the Profile model with one to one relationship. 

2. Profile Model

The Profile model is a custom custom-created model to handle the user profile details. Signals are used to reflect the changes between the User and Profile models. For example, if the Profile gets updated or deleted the changes will apply to the user model as well. 

3. Listing Model

The listing model is connected to the Profile with a ForeignKey field - owner. It is furthermore connected to the CarMake and CarModel models via ForeignKey field again

4. CarMake Model

This Model was created to store all of the car brands (car make) in the database 

5. CarModel Model

This model was created to store all of the car models in the database. It is connected to the CarMake model via ForeignKey field - car_make

6. Favourites

This model was created to store all of the favourite listings for each Profile. The model is connected to Listing and Profile models via ForeignKey fields - listing and owner.

### Fonts
The font used in this project is Roboto Slab, which compliments the design of the website. <br>
![Font](./assets/readme-images/font.PNG)

### Wireframes
### Agile Methodology
#### Overview
This project was created using agile principles. This was a big learning curve together with my very first full-stack project. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### EPICS(Milestones)
The user stories are grouped into eight EPICS or Milestones. An additional Milestone called Project Backlog was created to manage any additional features, bugs, or tasks that may arise during development. <br>
![Milestones](./assets/readme-images/agile-milestones.PNG)

#### User Stories issues
The structure of the user story issue consists of the user story, acceptance criteria, and tasks that outline the steps that are required for this issue to be completed. <br>
![User Story](./assets/readme-images/user-story-agile.PNG)
During development where possible, the commit messages are connected to their corresponding issues. <br>
![User Story](./assets/readme-images/user-story-commits.PNG)

#### MoSCoW prioritization
This prioritization technique was used to effectively prioritize the features and requirements of the project based on their importance. The acronym "MoSCoW" stands for "Must have, Should have, Could have, and Won't have." Each category helps categorize and prioritize features to guide the development process and ensure that the most critical elements are addressed first. <br>
![User Story](./assets/readme-images/user-story-moscow.PNG)

#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress, Done, and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow. <br>
![User Story](./assets/readme-images/github-projects.PNG)

## Features
### Navbar
The navbar is a component that is present on all pages. It was created using Bootstrap and is fully responsive. The AutoMarket logo which serves as a link to the homepage is located on the left side on the navbar. On the right are the nav links which allow the user to easily navigate through the website from any point. If the user is not authenticated the links displayed are Home, Listings, and Login/Signup.

![nav logged out](./assets/readme-images/features/nav-logged-out.PNG)

 If the user is authenticated they will see Home, Listings, Create Listing, Profile, and Logout. The profile link will have the user's username displayed to indicate that the user is logged in. For a better user experience, each nav link when active is underlined with a border to let the user know the page they are currently on.

 ![nav logged in](./assets/readme-images/features/nav-logged-in.PNG)
 ![nav mobile](./assets/readme-images/features/nav-mobile.PNG)

 ### Footer
 The footer consists of information about AutoMarket and their contact details. To help the users connect with AutoMarket there are icons with links to social media which open in a new tab. 

 ![Footer](./assets/readme-images/features/footer.PNG)

### Home
#### Hero Section
The choice of hero image for the website serves a specific purpose: it immediately communicates the main purpose of the website. The text overlay, "Find Your New Car," directly connects the image to the website's purpose. It encourages users to take action and search for their ideal vehicle, making the website's primary function clear right from the start. The high-end car image was carefully selected to create an immediate and powerful connection between the user and the website's mission, inviting them to explore the website further.

![Hero section](./assets/readme-images/features/nav-mobile.PNG)
#### Search Form
The search form allows the users to select via multiple filters like keywords, town, county, fuel type, year, and price. 
The view that handles the search form on the back end, pulls all of the listings from the database and then applies all the filters from the user's request. The results are passed to the listings page which also has the same search form at the top. The search parameters are preserved within the form for a better user experience.

![Search Form](./assets/readme-images/features/home-search.PNG)
#### Recent Listings
This section displays the six most recent listings added to the system.

![Recent Listings](./assets/readme-images/features/recent-listings.PNG)
#### Listing Card
The listing card is designed to present to the user the most important information about the listing. 
The card consists of a title, location, time ago posted, year, miles, price, and a button for more info. The card and the button are links to the single listing page.

![Listing Card](./assets/readme-images/features/listing-card.PNG)

### Listings Page
The listings page consists of the same search form as the home page. Further down are displayed all the listings starting from the most recent ones. Once the user applies filters from the search form the results are refined based on the filter applied. Six cards per page are displayed followed by pagination to allow the user to easily navigate through multiple pages of listings. The pagination works well with search results as well.

![Listings Page](./assets/readme-images/features/listing-results.PNG)
![Listings Page results](./assets/readme-images/features/listings-search-filter.PNG)

### Create Listing
This page can be accessed only by authenticated users. It provides the user with a listing creation form. During the planning process, the initial idea was to try and connect to an external API to fetch the car details based on the reg plate, however, all of the available APIs are paid. This is a future feature I would like to add. Implementing this will save time for the user and they won't have to fill out this very long form which will improve the user experience. Another idea to make the form more user-friendly was to break it into sections and make it dynamic. The only reason this wasn't completed was due to the timeframe for the project's deadline. 
The form fields limit wrong user input as much as possible by implementing select elements with drop-down options and using regex validation. The car model field is dynamically populated by using JavaScript and making a call to the back end. The model field is then populated with the appropriate options based on the car make selection. This helps to prevent users from creating listings with wrong details. Django widget tweaks was used to render the form in a more user-friendly version. The required fields are indicated by the * symbol after each label.
The Images section consists of 1 main image and six additional images. The main image input field is indicated so that the user can easily select the best possible main image for the card listing.

![Create Listing Form](./assets/readme-images/features/create-listing.PNG)

### Profile Page
This page can be accessed only by authenticated users. It consists of a sidebar menu with links for Profile, My Listings, and My favourite listings. 
The profile page is essentially a large card that includes the user's profile image and details like name, user name, email, and about me. Underneath, there are two buttons one for edit profile and one for delete profile.

![My Profile](./assets/readme-images/features/my-profile.PNG)

#### My listings
This page shows all of the listings that were created by this user. The cards have additional buttons for editing and deleting listings which allows each user to easily manage their listings. Maximum of 6 listings per page display and then pagination will appear at the bottom to help the user navigate through their listings.

![My Listings](./assets/readme-images/features/my-listings.PNG)

#### My Favourites
This page shows all the listings that have been saved to favourites by this user. The cards have buttons to remove from favourites or view the listing. Maximum of 6 listings per page display and then pagination will appear at the bottom to help the user navigate through their favourites.

![My favourites](./assets/readme-images/features/my-favourites.PNG)

#### Remove from Favourites
The user can easily remove a listing from favourites by pressing the remove button on the card listing from their favourites page. The user is then redirected to the confirmation page with a warning message and two buttons- one to go back and one to remove the listing. Once clicked the listing is removed. 
![Remove my favourites](./assets/readme-images/features/remove-favourites.PNG)

#### Edit Listing
This page displays the same form as create a listing, with already populated fields with the current details of the listing. The user can amend all of the details on the page and upload new images or just save the form as it is. Once submitted the user is redirected to my listings page.

![Edit Listing](./assets/readme-images/features/edit-listing.PNG)

#### Delete Listing
When the user visits my listings page they can delete listings using the delete button on each card, which redirects the user to confirmation page. The page consists of a warning message and two buttons - one to go back and one to delete listing, which is in red colour to clearly indicate danger.  Once the user confirms, the listing is deleted. The user is then redirected to my listings page.

![delete Listing](./assets/readme-images/features/delete-listing.PNG)

#### View Listing
This button leads to the single listing page. 
On the top left, there is a button to go back. Since this page can be accessed from multiple places, the path for a step back cannot be a link to a specific URL. This is why this button brings the user one step back. Below the button is the images section consisting of one large image and up to 6 smaller images below. To display the images in a more user-friendly way Lighbox2 was used. The button can easily navigate through the images with the buttons on the side.

![Gallery](./assets/readme-images/features/gallery.PNG)
Below that a description of the listing can be found. On the right side of the listing is where the most important information is presented to the user in a user-friendly manner. 
The listing's title (consisting of the car make and car model) followed by the price and then how long ago was this listing created.
Below that the relevant specifications are displayed, and by using icons the information is visually structured better.
If the user visits a listing that is not theirs there is a heart that they can click to save the listing into their favourites the action is clearly communicated with a flash message and the heart changing to a red heart. If the user clicks the heart again, they will remove the listing from favourites and will get a flash message letting them know that.

![add favourites](./assets/readme-images/features/save-favourites.PNG)

![remove favourites](./assets/readme-images/features/saved-listing.PNG)

Further down there is a card with the seller's details, consisting of their image, name, email, phone, and location if added. Their image is a link to their user account page. Below that is an email seller button which when clicked opens a modal with a form. The form is prepopulated with the user's details if they are authenticated. Once submitted, an email is sent to the listing's owner with the details within the form. 
![contact form](./assets/readme-images/features/contact-form.PNG)
![contact email](./assets/readme-images/features/contact-email.PNG)

#### User account and User account listings
This page renders other user's profiles. It has a very similar layout to my profile page with a few small changes. There are no favourites links in the sidebar menu. The profile page does not have edit and delete buttons as users should only be able to amend their profile pages. The link for my listings shows all of the listings this user has created. The cards display with a view button only.

![user account](./assets/readme-images/features/user-account.PNG)

![user account listings](./assets/readme-images/features/user-account-listings.PNG)

### Sign In page
Consist of a form with username and password. Below it has a link to reset password, followed by a sign in button which submits the form. The register link is position below that.

![Sign In](./assets/readme-images/features/sign-in.PNG)

### Sign Up page
Consists of a form with name, email, username, password, and password confirmation. Below it has a link to log in if the user already has an account. Below that is the signup button. The user is sent a welcome email to the email provided and is redirected to the profile page update form to customize their profile

![Sign Un](./assets/readme-images/features/signup.PNG)
![Welcome email](./assets/readme-images/features/welcome-email.PNG)

### Sign out confirmation
When the user clicks on the log out link in the nav, they are redirected to the confirmation page. This page consist of warning message and two buttons- one to go back and one to log out.

![log out confirmation](./assets/readme-images/features/log-out-confirmation.PNG)

### Edit Profile
The edit profie page renders a form with prefilled fields with the existing information for this user. It consists of profie image, name, username, email, phone, town, county and about me section. Below that is the submit button which will update the profile details once submitted. 

![edit profile](./assets/readme-images/features/edit-profile.PNG)

### Delete Profile Confirmation
This page consists of warning message with two buttons - one to go back and one to delete the profile. Delete profile is in red to indicate danger. Once clicked the profile is deleted and the user is redirected to We are sorry to see you go page

![delete profile](./assets/readme-images/features/delete-profile.PNG)

### We are sorry to see you go
This page confirms that the profile was deleted. The user is presented with a flash message confirming the profile was deleted successfully. Below that there is a button to go back to the home page.

![profile deleted](./assets/readme-images/features/profile-deleted.PNG)

### Password reset
This page prompts the user to enter their email address. An email with instructions is then sent to their email and the user is redirected to a page that informs them about the email being sent.

![pass reset](./assets/readme-images/features/pass-reset-enter-email.PNG)

### Password reset email sent
This page informs the user an email with instructions has been sent.

![pass reset email sent](./assets/readme-images/features/pass-reset-sent.PNG)

Email with instructions

![pass reset email](./assets/readme-images/features/pass-reset-email-instructions.PNG)

### Enter a new password
When the user follows the link from the email, they are sent to a page to set up their new password.

![pass reset new pass](./assets/readme-images/features/pass-reset-new-pass.PNG)

### Password Reset Completed
Once the form is submitted the user is redirected to a page advising them the password reset was completed followed by a log-in button.

![pass reset completed](./assets/readme-images/features/pass-reset-completed.PNG)

### Error Pages
- 404

![404](./assets/readme-images/features/404page.PNG)
- 403

![403](./assets/readme-images/features/403-page.PNG)
- 500

![500](./assets/readme-images/features/500-error.PNG)



## Future Features
## Testing
Testing documentation can be found [here.](./TESTING.md)
## Bugs
## Technologies And Languages

### Languages Used
- HTML
- CSS
- JavaScript
- Bootstrap
- Python
- Django
- Django Rest Framework

### Python Modules
- Boto3 is the Amazon Web Services (AWS) SDK for Python. It allows to interact with AWS services, such as S3

- dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

- django-resized - This package provides utilities for resizing images in Django. 

- django-storages - Django Storages is a collection of custom storage backends for Django, including support for storing files on remote services like AWS S3.

- django-widget-tweaks - Django Widget Tweaks is a package that simplifies working with form widgets and templates in Djang

- djangorestframework - Django REST framework is a toolkit for building Web APIs in Django.

- gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

- Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

- psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

- s3transfer - S3 Transfer is a library for managing file transfers to and from Amazon S3 storage.

- whitenoise - Whitenoise is a middleware for serving static files directly from your Django application.
- django humanize - A set of Django template filters useful for adding a “human touch” to data. Used to transform large numbers into easy to read numbers
### Technologies and programs
 - [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate Favicon
 - [Lightbox](https://lokeshdhakar.com/projects/lightbox2/) was used to display the listings images in a more user friendly way
 - [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as a starting point for the project.
- [Photoshop](https://www.adobe.com/ie/products/photoshop.html) was used for creating the mockup images of the website during planning stage.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used during the testing of the website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.
- [Online Convert](https://image.online-convert.com/convert-to-webp) used to convert images to webp format
- [Coolors.co](https://coolors.co/) was used to display the colour scheme.
- [Box Shadow Generator](https://cssgenerator.org/box-shadow-css-generator.html) was used to generate the shadows

## Deployment
### Before Deployment
To ensure the application is deployed correctly on Heroku it is mandatory to update the requirements.txt. This is a list of requirements that the application needs in order to run.

- To create the list of requirements we use the command pip3 freeze > requirements.txt. This will ensure the file with the requirements is updated.
- Then commit and push the changes to GitHub.
### Deployment on Heroku
### Creating a fork
1. Navigate to the [repository](https://github.com/Dayana-N/AutoMarket-PP4)
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description 
4. Choose to copy only the main branch or all branches to the new fork. 
5. Click Create a Fork. A repository should appear in your GitHub

### Cloning Repository
1. Navigate to the [repository](https://github.com/Dayana-N/AutoMarket-PP4)
2. Click on the Code button on top of the repository and copy the link. 
3. Open Git Bash and change the working directory to the location where you want the cloned directory. 
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.
## Credits
### Media
- [Default user image](https://res.cloudinary.com/dpmykpsih/image/upload/c_fill,f_auto,q_auto,w_360/tj-samson-site-251/media/5c7a249a36974d978322f386269f9c24.jpg)
- [Hero image](https://static1.hotcarsimages.com/wordpress/wp-content/uploads/2023/01/2023-bmw-4-series-coupe-featured.jpg)
- [Sorry to see you go image](https://charatoon.com/?id=5214)
- [Default Listing Image](https://png.pngtree.com/template/20220419/ourmid/pngtree-photo-coming-soon-abstract-admin-banner-image_1262901.jpg)

### Code
- Learned how to setup django project and deploy to Heroku from CI Django Blog walkthrough 
- [How to create dependant drop down](https://github.com/akjasim/cb_dj_dependent_dropdown) The code was later refactored to use Django Rest Api
- [The Car models list is from (back4app)](https://www.back4app.com/database/back4app/car-make-model-dataset) 
- [How to use Q objects for complex queries](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html)
- [Pagination fix for multiple search parameters](https://stackoverflow.com/questions/46026268/pagination-and-get-parameters)
- [How to catch email sending exceptions](https://stackoverflow.com/questions/41457565/how-to-catch-email-sending-exceptions-in-django-1-10)
- The search form was inspired visually by Brad Traversy's Python course
- How to setup AWS - CI instructions from PP5 walkthrough
- I learned how to use advanced Django concepts like signals, sending emails, how to use django rest framework and more from Dennis[ Ivy's Django course](https://dennisivy.teachable.com/p/django-beginners-course)
### Acknowledgements

### Comments
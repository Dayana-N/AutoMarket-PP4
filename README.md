# AutoMarket
[Link to deployed site](https://automarket-2a9033a7b561.herokuapp.com/)
<hr>
AutoMarket is a full stack project allowing users to postlistings with their vehicle for sale. The project is built using Django framework for the backend and HTML, CSS, Bootstrap and JavaScript on the frontend. Automarket allows the users to create an account and perform CRUD functionality on their profile and listings. This project was created as part of Code Institute full-stack developer course.

![automarket Image](./assets/readme%20images/main-image.PNG)

# Table Of Content

-   [User Experience](#user-experience)
    -   [User Stories](#user-stories)
    -   [Goals](#goals)
    -   [Scope](#scope)
-   [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
-   [Features](#features)
    -   [Home Page](#Home-Page)
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
![Colour Scheme](./assets/readme%20images/colour-palette.PNG)

### Database Schema
![database schema](./assets/readme%20images/database-schema.png)

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
![Font](./assets/readme%20images/font.PNG)

### Wireframes
### Agile Methodology
#### Overview
This project was created using agile principles. This was a big learning curve together with my very first full-stack project. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### EPICS(Milestones)
The user stories are grouped into eight EPICS or Milestones. An additional Milestone called Project Backlog was created to manage any additional features, bugs, or tasks that may arise during development. <br>
![Milestones](./assets/readme%20images/agile-milestones.PNG)

#### User Stories
The structure of the user story issue consists of the user story, acceptance criteria, and tasks that outline the steps that are required for this issue to be completed. <br>
![User Story](./assets/readme%20images/user-story-agile.PNG)
During development where possible, the commit messages are connected to their corresponding issues. <br>
![User Story](./assets/readme%20images/user-story-commits.PNG)

#### MoSCoW prioritization
This prioritization technique was used to effectively prioritize the features and requirements of the project based on their importance. The acronym "MoSCoW" stands for "Must have, Should have, Could have, and Won't have." Each category helps categorize and prioritize features to guide the development process and ensure that the most critical elements are addressed first. <br>
![User Story](./assets/readme%20images/user-story-moscow.PNG)

#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress, Done, and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow. <br>
![User Story](./assets/readme%20images/github-projects.PNG)
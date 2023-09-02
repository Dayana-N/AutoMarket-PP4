Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
- [User Story Testing](#user-story-testing)

## Code Validation
### HTML
|Page|Validator|Result|
| --- | --- | --- |
| Home |![home](./assets/testing/html-validator/home.PNG) | <mark>PASS<mark> |
| Listings |![listings](./assets/testing/html-validator/listings.PNG) | <mark>PASS<mark> |
| Single Listing |![Single Listing](./assets/testing/html-validator/single-listing.PNG) | <mark>PASS<mark> |
| Create And Edit Listing |![Create Listing](./assets/testing/html-validator/edit-listing.PNG) | <mark>PASS<mark> |
| My Profile |![My Profile](./assets/testing/html-validator/my-profile.PNG) | <mark>PASS<mark> |
| My Listings |![My Listings](./assets/testing/html-validator/my-listings.PNG) | <mark>PASS<mark> |
| My Favourites |![My Favourites](./assets/testing/html-validator/my-favourites.PNG) | <mark>PASS<mark> |
| User Account |![User Account](./assets/testing/html-validator/user-account.PNG) | <mark>PASS<mark> |
| User Listings |![User Listings](./assets/testing/html-validator/user-listings.PNG) | <mark>PASS<mark> |
| Edit Profile |![Edit Profile](./assets/testing/html-validator/edit-profile.PNG) | <mark>PASS<mark> |
| Delete Profile Conf|![Delete Profile](./assets/testing/html-validator/delete-profile-conf.PNG) | <mark>PASS<mark> |
| Profile Deleted |![Profile Deleted](./assets/testing/html-validator/profile-deleted.PNG) | <mark>PASS<mark> |
| Delete Listing Conf |![Delete Listing Conf](./assets/testing/html-validator/delete-listing-conf.PNG) | <mark>PASS<mark> |
| Remove Favourite |![Remove Favourite](./assets/testing/html-validator/delete-favourite.PNG) | <mark>PASS<mark> |
| Log In |![Log In](./assets/testing/html-validator/login.PNG) | <mark>PASS<mark> |
| Sign Up |![Sign Up](./assets/testing/html-validator/signup.PNG) | <mark>PASS<mark> |
| Sign Out Conf |![home](./assets/testing/html-validator/logout-conf.PNG) | <mark>PASS<mark> |
| Reset Password Enter email |![Reset Password Enter email](./assets/testing/html-validator/pass-reset.PNG) | <mark>PASS<mark> |
| Reset Password email sent |![Reset Password email sent](./assets/testing/html-validator/pass-reset-email-sent.PNG) | <mark>PASS<mark> |
| Reset Password Enter password |![Reset Password Enter password](./assets/testing/html-validator/pass-reset-new-pass.PNG) | <mark>PASS<mark> |
| Reset Password Complete |![Reset Password Complete](./assets/testing/html-validator/pass-reset-complete.PNG) | <mark>PASS<mark> |
| Error pages |![home](./assets/testing/html-validator/404.PNG) | <mark>PASS<mark> |


### CSS
Test Results CSS  <mark>PASS<mark> 

![css-validator](./assets/testing/css-validator.PNG)
### JavaScript
1. listing_form.js <mark>PASS<mark> 

![listing_form](./assets/testing/listing_form.PNG)

2. search.js <mark>PASS<mark>

The initial test showed variable not declared. This was fixed.
![search](./assets/testing/search.PNG)

### Python
1. Api app
- serializers.py <mark>PASS<mark>

![serializers](./assets/testing/api-serializers.PNG)

- urls.py <mark>PASS<mark>

![urls](./assets/testing/api-urls.PNG)

- views.py <mark>PASS<mark>

![views](./assets/testing/api-views.PNG)

2. Automarket app
- settings.py <mark>PASS<mark> 

(line too long is part of django standart settings file)

![settings](./assets/testing/automarket-settings.PNG)

- urls.py <mark>PASS<mark>

![urls](./assets/testing/automarket-urls.PNG)

- views.py <mark>PASS<mark>

![views](./assets/testing/automarket-views.PNG)

3. Listings
- admin.py <mark>PASS<mark>

![admin](./assets/testing/listings-admin.PNG)

- cars.py <mark>PASS<mark>

![cars](./assets/testing/listings-cars.PNG)

- choices.py <mark>PASS<mark>

![choices](./assets/testing/listings-choices.PNG)

- forms.py <mark>PASS<mark>

![forms](./assets/testing/listings-forms.PNG)

- models.py <mark>PASS<mark>

![models](./assets/testing/listings-models.PNG)

- urls.py <mark>PASS<mark>

![urls](./assets/testing/listings-urls.PNG)

- url_helpers.py <mark>PASS<mark>

![url_helpers](./assets/testing/listings-url_helper.PNG)

- utils.py <mark>PASS<mark>

![utils](./assets/testing/listings-utils.PNG)

- views.py <mark>PASS<mark>

![views](./assets/testing/listings-views.PNG)
4. Users
- admin.py <mark>PASS<mark>

![admin](./assets/testing/users-admin.PNG)

- apps.py <mark>PASS<mark>

![apps](./assets/testing/users-apps.PNG)

- emails.py <mark>PASS<mark> 

(there is a warning for line too long, however if amended the email sent to the user does not display correct. This is a string and does not affect the code.)

![emails](./assets/testing/users-emails.PNG)

- forms.py <mark>PASS<mark>

![forms](./assets/testing/users-forms.PNG)

- models.py <mark>PASS<mark>

![models](./assets/testing/users-models.PNG)

- urls.py <mark>PASS<mark>

![urls](./assets/testing/users-urls.PNG)

- signals.py <mark>PASS<mark>

![signals](./assets/testing/users-signals.PNG)

- views.py <mark>PASS<mark>

![views](./assets/testing/users-views.PNG)

## Responsiveness
During development each page was tested using dev tools in Google Chrome. The strategy involved ensuring that every page would adapt to various screen sizes beyond a width of 320px, as opposed to relying on fixed device-specific widths.
Further testing was done on mobile to confirm all is working as expected.

|Device|Screen Size|Pass/Fail|Comment|
| --- | --- | --- | ---|
| Iphone 4 | 320x480 | PASS | All sections are displayed correctly. All features work|
| Iphone 12 Pro | 390x844 | PASS | All sections are displayed correctly. All features work|
| Samsung Galaxy s20U | 412x915 | PASS | All sections are displayed correctly. All features work|
| Galaxy Tab S4 | 712x1138| PASS | All sections are displayed correctly. All features work|
| Nest Hub | 1024x600 | PASS | All sections are displayed correctly. All features work|


### Galaxy S20 Ultra
<details><summary>Home</summary> 
 <img src="./assets/testing/responsiveness/Home.jpg"> </details>

<details><summary>Listings</summary> <img src="./assets/testing/responsiveness/Listings.jpg"></details>
<details><summary>Single Listing</summary><img src="./assets/testing/responsiveness/single-listing-page.jpg"></details>
<details><summary>Gallery</summary><img src="./assets/testing/responsiveness/gallery.jpg"></details>
<details><summary>Create Listing</summary><img src="./assets/testing/responsiveness/Create-listing.jpg"></details>
<details><summary>My Profile</summary><img src="./assets/testing/responsiveness/my-profile.jpg"></details>
<details><summary>My Favourites</summary><img src="./assets/testing/responsiveness/my-favourites.jpg"></details>
<details><summary>My Listings</summary><img src="./assets/testing/responsiveness/my-listings.jpg"></details>
<details><summary>Remove Favourite</summary><img src="./assets/testing/responsiveness/remove-fav-conf.jpg"></details>
<details><summary>500 Page</summary><img src="./assets/testing/responsiveness/500-page.jpg"></details>
<details><summary>Log In</summary><img src="./assets/testing/responsiveness/Sign-in.jpg"></details>
<details><summary>Sign Up</summary><img src="./assets/testing/responsiveness/Sign-up.jpg"></details>


## Browser Compatibility


|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | During initial testing there was an issue with the hero image on Edge. The reason was that the browser does not support avif files. The file was converted to webp and tested again.  |

## Lighthouse


|Page|Validator|Result|
| --- | --- | --- |
| Home Desktop |![home](./assets/testing/lighthouse/home-d.PNG) | <mark>PASS<mark> |
| Home Mobile |![home](./assets/testing/lighthouse/home-m.PNG) | <mark>PASS<mark> |
| Listings Desktop|![listings](./assets/testing/lighthouse/listings-d.PNG) | <mark>PASS<mark> |
| Listings Mobile|![listings](./assets/testing/lighthouse/listings-m.PNG) | <mark>PASS<mark> |
| Single Listing Desktop|![Single Listing](./assets/testing/lighthouse/single-listing-d.PNG) | <mark>PASS<mark> |
| Single Listing Mobile|![Single Listing](./assets/testing/lighthouse/single-listing-m.PNG) | <mark>PASS<mark> |
| Create Listing Desktop|![Create Listing](./assets/testing/lighthouse/create-listing-d.PNG) | <mark>PASS<mark> |
| Create Listing Mobile|![Create Listing](./assets/testing/lighthouse/create-listing-m.PNG) | <mark>PASS<mark> |
| Edit Listing Desktop|![Create Listing](./assets/testing/lighthouse/edit-listing-d.PNG) | <mark>PASS<mark> |
| Edit Listing Mobile|![Create Listing](./assets/testing/lighthouse/edit-listing-m.PNG) | <mark>PASS<mark> |
| My Profile Desktop|![My Profile](./assets/testing/lighthouse/my-profile-d.PNG) | <mark>PASS<mark> |
| My Profile Mobile|![My Profile](./assets/testing/lighthouse/my-profile-m.PNG) | <mark>PASS<mark> |
| My Listings Desktop|![My Listings](./assets/testing/lighthouse/my-listings-d.PNG) | <mark>PASS<mark> |
| My Listings Mobile|![My Listings](./assets/testing/lighthouse/my-listings-m.PNG) | <mark>PASS<mark> |
| My Favourites Desktop|![My Favourites](./assets/testing/lighthouse/my-favourites-d.PNG) | <mark>PASS<mark> |
| My Favourites Mobile|![My Favourites](./assets/testing/lighthouse/my-favourites-m.PNG) | <mark>PASS<mark> |
| User Account Desktop|![User Account](./assets/testing/lighthouse/user-acc-d.PNG) | <mark>PASS<mark> |
| User Account Mobile|![User Account](./assets/testing/lighthouse/user-acc-m.PNG) | <mark>PASS<mark> |
| User Listings Desktop |![User Listings](./assets/testing/lighthouse/user-acc-listings-d.PNG) | <mark>PASS<mark> |
| User Listings Mobile |![User Listings](./assets/testing/lighthouse/user-acc-m.PNG) | <mark>PASS<mark> |
| Edit Profile Desktop|![Edit Profile](./assets/testing/lighthouse/edit-profile-d.PNG) | <mark>PASS<mark> |
| Edit Profile Mobile|![Edit Profile](./assets/testing/lighthouse/edit-profile-m.PNG) | <mark>PASS<mark> |
| Delete Profile Conf Desktop|![Delete Profile](./assets/testing/lighthouse/delete-profile-d.PNG) | <mark>PASS<mark> |
| Delete Profile Conf Mobile|![Delete Profile](./assets/testing/lighthouse/delete-profile-m.PNG) | <mark>PASS<mark> |
| Profile Deleted Desktop|![Profile Deleted](./assets/testing/lighthouse/profile-delete-success-d.PNG) | <mark>PASS<mark> |
| Profile Deleted Mobile|![Profile Deleted](./assets/testing/lighthouse/profile-delete-success-m.PNG) | <mark>PASS<mark> |
| Delete Listing Conf Desktop|![Delete Listing Conf](./assets/testing/lighthouse/delete-listing-d.PNG) | <mark>PASS<mark> |
| Delete Listing Conf Mobile|![Delete Listing Conf](./assets/testing/lighthouse/delete-listing-m.PNG) | <mark>PASS<mark> |
| Remove Favourite Desktop|![Remove Favourite](./assets/testing/lighthouse/remove-fav-d.PNG) | <mark>PASS<mark> |
| Remove Favourite Mobile|![Remove Favourite](./assets/testing/lighthouse/remove-fav-m.PNG) | <mark>PASS<mark> |
| Log In Desktop|![Log In](./assets/testing/lighthouse/sign-in-d.PNG) | <mark>PASS<mark> |
| Log In Mobile|![Log In](./assets/testing/lighthouse/sign-in-m.PNG) | <mark>PASS<mark> |
| Sign Up Desktop|![Sign Up](./assets/testing/lighthouse/sign-up-d.PNG) | <mark>PASS<mark> |
| Sign Up Mobile|![Sign Up](./assets/testing/lighthouse/sign-up-m.PNG) | <mark>PASS<mark> |
| Sign Out Conf Desktop|![home](./assets/testing/lighthouse/logout-d.PNG) | <mark>PASS<mark> |
| Sign Out Conf Mobile|![home](./assets/testing/lighthouse/logout-m.PNG) | <mark>PASS<mark> |
| Reset Password Enter email Desktop|![Reset Password Enter email](./assets/testing/lighthouse/pass-res-d.PNG) | <mark>PASS<mark> |
| Reset Password Enter email Mobile|![Reset Password Enter email](./assets/testing/lighthouse/pass-res-m.PNG) | <mark>PASS<mark> |
| Reset Password email sent Desktop|![Reset Password email sent](./assets/testing/lighthouse/pass-res-sent-d.PNG) | <mark>PASS<mark> |
| Reset Password email sent Mobile|![Reset Password email sent](./assets/testing/lighthouse/pass-res-sent-m.PNG) | <mark>PASS<mark> |
| Reset Password Enter password Desktop|![Reset Password Enter password](./assets/testing/lighthouse/pass-res-newpass-d.PNG) | <mark>PASS<mark> |
| Reset Password Enter password Mobile|![Reset Password Enter password](./assets/testing/lighthouse/pass-res-newpass-m.PNG) | <mark>PASS<mark> |
| Reset Password Complete Desktop|![Reset Password Complete](./assets/testing/lighthouse/pass-res-complete-d.PNG) | <mark>PASS<mark> |
| Reset Password Complete Mobile|![Reset Password Complete](./assets/testing/lighthouse/pass-res-complete-m.PNG) | <mark>PASS<mark> |
| Profile Deleted Success Desktop |![Profile Deleted Success](./assets/testing/lighthouse/profile-delete-success-d.PNG) | <mark>PASS<mark> |
| Profile Deleted Success Mobile |![Profile Deleted Success](./assets/testing/lighthouse/profile-delete-success-m.PNG) | <mark>PASS<mark> |
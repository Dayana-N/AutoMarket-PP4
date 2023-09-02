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

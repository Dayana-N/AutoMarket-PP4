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

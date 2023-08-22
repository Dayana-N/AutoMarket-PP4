// Add event listeners to dinamically update the page
document.addEventListener('DOMContentLoaded', function(){
    const profileBtn = document.getElementById('btn-profile');
    const listingsBtn = document.getElementById('btn-listings');

    const listingsContainer = document.getElementById('my-listings-container');
    const profileContainer = document.getElementById('my-profile-container');

    profileBtn.addEventListener('click',(e) => {
        profileContainer.style.display = 'block';
        listingsContainer.style.display = 'none';
    })

    listingsBtn.addEventListener('click',(e) => {
        profileContainer.style.display = 'none';
        listingsContainer.style.display = 'block';
    })

})

document.addEventListener('DOMContentLoaded', function(){
    const profileBtn = document.getElementById('btn-profile');
    const listingsBtn = document.getElementById('btn-listings');
    const favouritesBtn = document.getElementById('btn-favourites');
    const sidebarLinks = document.querySelectorAll('.btn-sidebar')

    const favouritesContainer = document.getElementById('my-favourites-container');
    const listingsContainer = document.getElementById('my-listings-container');
    const profileContainer = document.getElementById('my-profile-container');

    profileBtn.addEventListener('click',(e) => {
        profileContainer.style.display = 'block';
        listingsContainer.style.display = 'none';
        favouritesContainer.style.display = 'none';
    })

    listingsBtn.addEventListener('click',(e) => {
        profileContainer.style.display = 'none';
        listingsContainer.style.display = 'block';
        favouritesContainer.style.display = 'none';
    })

    favouritesBtn.addEventListener('click',(e) => {
        profileContainer.style.display = 'none';
        listingsContainer.style.display = 'none';
        favouritesContainer.style.display = 'block';
    })
})
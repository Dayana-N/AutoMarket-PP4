const carMakeDropdown = document.getElementById('id_car_make');
const carModelDropdown = document.getElementById('id_car_model');

carMakeDropdown.addEventListener('change', (e) => {
    const makeId = carMakeDropdown.value;
    // const url = `https://8000-dayanan-automarketpp4-018mrjwl7i9.ws-eu104.gitpod.io/load-models/${makeId}`;
    const url = `https://automarket-2a9033a7b561.herokuapp.com/load-models/${makeId}`;

    fetch(url)
    .then(response => response.json())
    .then(data=>{
        // Clear the existing options
        carModelDropdown.innerHTML = '<option value="" selected>---------</option>';

        data.forEach(model => {
            const option = document.createElement('option');
            for (const key in model) {
                option.value = key;
                option.textContent = model[key];
            }

            carModelDropdown.appendChild(option);
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error );
    });
});
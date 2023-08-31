const carMakeDropdown = document.getElementById("id_car_make");
const carModelDropdown = document.getElementById("id_car_model");

carMakeDropdown.addEventListener("change", (e) => {
  const makeId = carMakeDropdown.value;
  // const url = `https://8000-dayanan-automarketpp4-018mrjwl7i9.ws-eu104.gitpod.io/api/car-model/${makeId}`;

  const url = `https://automarket-2a9033a7b561.herokuapp.com/api/car-model/${makeId}`;
  if (makeId) {
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        // Clear the existing options
        carModelDropdown.innerHTML =
          '<option value="" selected>---------</option>';

        data.forEach((model) => {
          const option = document.createElement("option");
          option.value = model.id;
          option.textContent = model.name;

          carModelDropdown.appendChild(option);
        });
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  } else {
    carModelDropdown.innerHTML = '<option value="" selected>---------</option>';
  }
});

document.addEventListener('DOMContentLoaded', function() {
    // Get the min and max year options
    const minYear = document.getElementById('min_year');
    const maxYear = document.getElementById('max_year');
    const minYearOptions = minYear.getElementsByTagName("option");
    const maxYearOptions = maxYear.getElementsByTagName("option");

    // Get the min and max price options
    const minPrice = document.getElementById('min_price');
    const maxPrice = document.getElementById('max_price');
    const minPriceOptions = minPrice.getElementsByTagName("option");
    const maxPriceOptions = maxPrice.getElementsByTagName("option");

    // Add event listeners to year fields to disable options based on user's selection
    minYear.addEventListener('change', (e) => {
        const selectedMinValue = parseInt(minYear.value);

        for (const maxOption of maxYearOptions) {
            if (isNaN(selectedMinValue) || selectedMinValue > parseInt(maxOption.value)) {
                maxOption.disabled = true;
            } else {
                maxOption.disabled = false;
            }
        }
    });

    maxYear.addEventListener('change', (e) => {
        const selectedMaxValue = parseInt(maxYear.value);

        for (const minOption of minYearOptions) {
            if (isNaN(selectedMaxValue) || selectedMaxValue < parseInt(minOption.value)) {
                minOption.disabled = true;
            } else {
                minOption.disabled = false;
            }
        }
    });

    // Add event listeners to price fields to disable options based on user's selection
    minPrice.addEventListener('change', (e) => {
        const selectedMinValue = parseFloat(minPrice.value);

        for (const maxOptionPrice of maxPriceOptions) {
            if (selectedMinValue > parseFloat(maxOptionPrice.value)) {
                maxOptionPrice.disabled = true;
            } else {
                maxOptionPrice.disabled = false;
            }
        }
    });

    maxPrice.addEventListener('change', (e) => {
        const selectedMaxValue = parseFloat(maxPrice.value);

        for (const minOptionPrice of minPriceOptions) {
            if (selectedMaxValue < parseFloat(minOptionPrice.value)) {
                minOptionPrice.disabled = true;
            } else {
                minOptionPrice.disabled = false;
            }
        }
    });
});
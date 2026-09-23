const accidentSlider = document.getElementById("accidents");

const accidentValue = document.getElementById("accidentValue");

const locationSelect = document.getElementById("location");

const premiumDisplay = document.getElementById("premium");


accidentSlider.addEventListener("input", function () {

    const accidents = accidentSlider.value;

    accidentValue.textContent = accidents;

});
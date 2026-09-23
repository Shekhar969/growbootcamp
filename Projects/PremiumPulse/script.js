const SUPABASE_URL = "https://tmtdpxcypcrkvhjrooea.supabase.co";
const SUPABASE_KEY = "sb_publishable_llAM7FhHmGSLcnAZH_Qn4g_eR-G9eK2";

const supabase = window.supabase.createClient(
    SUPABASE_URL,
    SUPABASE_KEY
);


// Get HTML elements
const accidentSlider = document.getElementById("accidents");
const accidentValue = document.getElementById("accidentValue");
const locationSelect = document.getElementById("location");
const premiumDisplay = document.getElementById("premium");


// Load locations from Supabase
async function loadLocations() {

    const { data, error } = await supabase
        .from("locations")
        .select("*")
        .order("name");

    if (error) {
        console.error("Error loading locations:", error);
        return;
    }

    locationSelect.innerHTML = "";

    data.forEach(function (location) {

        const option = document.createElement("option");

        option.value = location.id;
        option.textContent = location.name;

        locationSelect.appendChild(option);

    });
}


// Update accident number when slider moves
accidentSlider.addEventListener("input", function () {

    const accidents = accidentSlider.value;

    accidentValue.textContent = accidents;

});


loadLocations();
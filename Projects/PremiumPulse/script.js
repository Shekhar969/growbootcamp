const accidentSlider = document.getElementById("accidents");
const accidentValue = document.getElementById("accidentValue");
const locationSelect = document.getElementById("location");

const supabaseUrl = window.SUPABASE_URL;
const supabaseAnonKey = window.SUPABASE_ANON_KEY;
const supabaseClient =
    window.supabase && supabaseUrl && supabaseAnonKey
        ? window.supabase.createClient(supabaseUrl, supabaseAnonKey)
        : null;

function showLocationError(message) {
    locationSelect.replaceChildren();
    const option = document.createElement("option");
    option.textContent = message;
    option.disabled = true;
    option.selected = true;
    locationSelect.append(option);
}

async function loadLocations() {
    if (!supabaseClient) {
        showLocationError(
            "Supabase is not configured. Set SUPABASE_URL and SUPABASE_ANON_KEY."
        );
        return;
    }

    const { data: locations, error } = await supabaseClient
        .from("locations")
        .select("id, name")
        .order("name");

    if (error) {
        console.error("Unable to load locations from Supabase:", error);
        showLocationError("Unable to load locations.");
        return;
    }

    locationSelect.replaceChildren();
    locations.forEach((location) => {
        const option = document.createElement("option");
        option.value = location.id;
        option.textContent = location.name;
        locationSelect.append(option);
    });
}

accidentSlider.addEventListener("input", () => {
    accidentValue.textContent = accidentSlider.value;
});

loadLocations();

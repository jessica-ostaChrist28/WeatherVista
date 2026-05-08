const form = document.getElementById("weatherForm");

const loading = document.getElementById("loading");

form.addEventListener("submit", () => {

    loading.classList.remove("hidden");
});
const locationBtn = document.getElementById("locationBtn");

locationBtn.addEventListener("click", () => {

    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(
            async(position) => {

                const lat = position.coords.latitude;

                const lon = position.coords.longitude;

                alert(
                    `Latitude: ${lat}, Longitude: ${lon}`
                );
            }
        );
    }
});
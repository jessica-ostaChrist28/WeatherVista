const form = document.getElementById("weatherForm");

const cityInput = document.getElementById("cityInput");

const weatherResult = document.getElementById("weatherResult");

const loading = document.getElementById("loading");

const themeToggle = document.getElementById("themeToggle");

const recentSearches = document.getElementById("recentSearches");

themeToggle.innerHTML = "🌙";

// ==============================
// WEATHER FETCH
// ==============================

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const city = cityInput.value.trim();

    if (!city) {
        return;
    }

    loading.classList.remove("hidden");

    weatherResult.innerHTML = "";

    try {

        const response = await fetch(
            `/api/weather/${city}`
        );

        const data = await response.json();

        loading.classList.add("hidden");

        if (data.error) {

            weatherResult.innerHTML = `
                <p class="error">${data.error}</p>
            `;

            return;
        }

        const weather = data.weather;

        const forecast = data.forecast;

        // ==============================
        // DYNAMIC BACKGROUND
        // ==============================

        changeBackground(weather.condition);

        // ==============================
        // SAVE RECENT SEARCH
        // ==============================

        saveRecentSearch(city);

        // ==============================
        // FORECAST HTML
        // ==============================

        let forecastHTML = "";

        forecast.forEach(item => {

            forecastHTML += `

                <div class="forecast-card">

                    <p>${new Date(item.time).toLocaleString()}</p>

                    <img
                        src="https://openweathermap.org/img/wn/${item.icon}@2x.png"
                    >

                    <p>${item.temp} °C</p>

                    <p>${weather.description}</p>

                </div>
            `;
        });

        // ==============================
        // WEATHER CARD HTML
        // ==============================

        weatherResult.innerHTML = `

            <div class="weather-card">

                <h2>${weather.city}</h2>

                <img
                    src="https://openweathermap.org/img/wn/${weather.icon}@2x.png"
                >

                <p>
                    Temperature: ${weather.temperature} °C
                </p>

                <p>
                    Feels Like: ${weather.feels_like} °C
                </p>

                <p>
                    Humidity: ${weather.humidity}%
                </p>

                <p>
                    Wind Speed: ${weather.wind} m/s
                </p>

                <p>
                    Condition: ${weather.condition}
                </p>

            </div>

            <div class="forecast-container">

                ${forecastHTML}

            </div>
        `;

    } catch (error) {

        loading.classList.add("hidden");

        weatherResult.innerHTML = `
            <p class="error">
                Something went wrong.
            </p>
        `;
    }
});



// ==============================
// DARK / LIGHT MODE
// ==============================

themeToggle.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {

        themeToggle.innerHTML = "☀️";

    } else {

        themeToggle.innerHTML = "🌙";
    }
});



// ==============================
// RECENT SEARCHES
// ==============================

function saveRecentSearch(city) {

    let searches = JSON.parse(
        localStorage.getItem("recentCities")
    ) || [];

    city = city.toLowerCase();

    if (!searches.includes(city)) {

        searches.unshift(city);

        if (searches.length > 5) {

            searches.pop();
        }

        localStorage.setItem(
            "recentCities",
            JSON.stringify(searches)
        );
    }

    renderRecentSearches();
}



function renderRecentSearches() {

    let searches = JSON.parse(
        localStorage.getItem("recentCities")
    ) || [];

    recentSearches.innerHTML = searches.map(city => `

        <button
            class="recent-btn"
            onclick="quickSearch('${city}')"
        >
            ${city}

        </button>

    `).join("");
}



function quickSearch(city) {

    cityInput.value = city;

    form.dispatchEvent(
        new Event("submit")
    );
}



// ==============================
// DYNAMIC BACKGROUND
// ==============================

function changeBackground(condition) {

    document.body.classList.remove(
        "Clear",
        "Clouds",
        "Rain",
        "Snow",
        "Thunderstorm"
    );

    document.body.classList.add(condition);
}



// ==============================
// GEOLOCATION
// ==============================

const locationBtn = document.getElementById("locationBtn");

locationBtn.addEventListener("click", () => {

    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(

            async (position) => {

                const lat = position.coords.latitude;

                const lon = position.coords.longitude;

                try {

                    loading.classList.remove("hidden");

                    const response = await fetch(
                        `/api/location/${lat}/${lon}`
                    );

                    const data = await response.json();

                    loading.classList.add("hidden");

                    if (data.error) {

                        weatherResult.innerHTML = `
                            <p class="error">
                                Unable to fetch location weather.
                            </p>
                        `;

                        return;
                    }

                    const weather = data.weather;

                    const forecast = data.forecast;

                    changeBackground(weather.condition);

                    let forecastHTML = "";

                    (forecast || []).forEach(item => {  

                        forecastHTML += `

                            <div class="forecast-card">

                                <p>${item.time}</p>

                                <img
                                    src="https://openweathermap.org/img/wn/${item.icon}@2x.png"
                                >

                                <p>${item.temp} °C</p>

                                <p>${item.condition}</p>

                            </div>
                        `;
                    });

                    weatherResult.innerHTML = `

                        <div class="weather-card">

                            <h2>${weather.city}</h2>

                            <img
                                src="https://openweathermap.org/img/wn/${weather.icon}@2x.png"
                            >

                            <p>
                                Temperature: ${weather.temperature} °C
                            </p>

                            <p>
                                Feels Like: ${weather.feels_like} °C
                            </p>

                            <p>
                                Humidity: ${weather.humidity}%
                            </p>

                            <p>
                                Wind Speed: ${weather.wind} m/s
                            </p>

                            <p>
                                Condition: ${weather.condition}
                            </p>

                        </div>

                        <div class="forecast-container">

                            ${forecastHTML}

                        </div>
                    `;

                } catch (error) {

                    loading.classList.add("hidden");

                    weatherResult.innerHTML = `
                        <p class="error">
                            Failed to get location weather.
                        </p>
                    `;
                }
            },

            () => {

                alert(
                    "Location access denied."
                );
            }
        );

    } else {

        alert(
            "Geolocation is not supported by this browser."
        );
    }
});



// ==============================
// INITIAL LOAD
// ==============================

renderRecentSearches();
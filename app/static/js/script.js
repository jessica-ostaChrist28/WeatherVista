const form = document.getElementById("weatherForm");

const loading = document.getElementById("loading");

form.addEventListener("submit", () => {

    loading.classList.remove("hidden");
});
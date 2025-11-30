const toggleBtn = document.querySelector(".menu-toggle");
const menu = document.querySelector(".menu");

toggleBtn.addEventListener("click", () => {
    menu.classList.toggle("active");
});

function toggleSearch() {
    const searchBar = document.getElementById("search-bar");
    searchBar.classList.toggle("active");
}
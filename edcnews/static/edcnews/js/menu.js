const toggleBtn = document.querySelector(".menu-toggle");
const menuList = document.querySelector(".menu ul");

toggleBtn.addEventListener("click", () => {
    menuList.classList.toggle("show");
});
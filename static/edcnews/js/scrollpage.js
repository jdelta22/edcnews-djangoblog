let page = 2;
let loading = false;

window.addEventListener("scroll", () => {
    if (loading) return;

    const scrollPos = window.innerHeight + window.scrollY;
    const nearBottom = document.body.offsetHeight - 300;

    if (scrollPos >= nearBottom) {
        loadMoreNews();
    }
});

function loadMoreNews() {
    loading = true;
    document.getElementById("loading").style.display = "block";

    fetch(`/load-more-news/?page=${page}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("loading").style.display = "none";

            // adiciona o HTML recebido
            document.getElementById("news-container")
                .insertAdjacentHTML("beforeend", data.html);

            if (data.has_next) {
                page++;
                loading = false;
            }
        });
}
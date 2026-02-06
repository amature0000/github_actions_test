document.getElementById("searchBox").addEventListener("input", function() {
    const keyword = this.value.toLowerCase();

    document.querySelectorAll("tbody tr, table tr").forEach(row => {
        const text = row.innerText.toLowerCase();
        row.style.display = text.includes(keyword) ? "" : "none";
    });
});
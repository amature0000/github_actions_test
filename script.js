document.getElementById("searchBox").addEventListener("input", function () {
    const keyword = this.value.toLowerCase();

    document.querySelectorAll("tbody tr, table tr").forEach(row => {
        const link = row.querySelector("td a");
        if (!link) return;

        const text = link.textContent.toLowerCase();
        row.style.display = text.includes(keyword) ? "" : "none";
    });
});

window.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll("tbody").forEach(tbody => {

        const rows = Array.from(tbody.querySelectorAll("tr"));

        rows.sort((a, b) => {
            const dateA = new Date(a.cells[1].textContent.trim());
            const dateB = new Date(b.cells[1].textContent.trim());

            return dateB - dateA;
        });

        rows.forEach(row => tbody.appendChild(row));
    });

});
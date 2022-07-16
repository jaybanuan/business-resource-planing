document.addEventListener('DOMContentLoaded', () => {
    fetch("/column/machine")
        .then(response => response.json())
        .then(columns => {
            var tabulator = new Tabulator("#example-table", {
                layout:"fitColumns",
                columnHeaderVertAlign:"middle", //align header contents to bottom of cell
                columns:columns.columns,
                ajaxURL:"http://localhost:8080/machine/", //ajax URL
            })
        });
});
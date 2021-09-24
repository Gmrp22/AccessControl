const url = "http://localhost:8000/QR/report/";
const table = document.getElementById("table");

(async () => {
    const rawResponse = await fetch(url);
    const content = await rawResponse.json();

    console.log(content);
    content.forEach(element => {
        table.innerHTML = `
    <tr>
    <td>${element.worked}</td>
    <td>${element.extra}</td>
    <td>${element.count}</td>
    <td>${element.status}</td>
    <td>${element.user}</td>
    </tr>`
    });
})();


// {
//     "worked": null,
//     "extra": null,
//     "count": null,
//     "status": "",
//     "user": null
// }
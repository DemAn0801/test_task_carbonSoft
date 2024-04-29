setInterval(async() => {
    let response = await doRequest(`${url}/get_new/`)
    let tbody = document.querySelector("#summary_table_body")
    tbody.innerHTML = '';
    response["result"]["agregate"].forEach(element => {
        var row = document.createElement("tr")
        var td1 = document.createElement("td")
        td1.appendChild(document.createTextNode(`${element["title"]}`))
        var td2 = document.createElement("td")
        td2.appendChild (document.createTextNode(`${element["cpu"]}`))
        row.appendChild(td1);
        row.appendChild(td2);
        tbody.appendChild(row);
    });
} , 1000);

const updateSummaryTable = async() => {
    let response = await doRequest(`${URL}/get_new/`);
    let tbody = document.querySelector("#summary_table_body");
    tbody.innerHTML = "";
    response["result"]["agregate"].forEach(element => {
        let row = document.createElement("tr");
        let td1 = document.createElement("td");
        td1.appendChild(document.createTextNode(`${element["title"]}`));
        let td2 = document.createElement("td");
        td2.appendChild (document.createTextNode(element["cpu"].toFixed(2)));
        row.appendChild(td1);
        row.appendChild(td2);
        tbody.appendChild(row);
    });
};

updateSummaryTable();
setInterval(async() => {
   updateSummaryTable();
} , 10000);

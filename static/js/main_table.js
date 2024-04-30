const updateMainTable = async() => {
    let response = await doRequest(`${URL}/get_new/`);
    let tbody = document.querySelector("#table_body");
    tbody.innerHTML = "";
    let counter = 1;
    let lsortedList = toSortList(sortMethod, response["result"]["rows"]);
    lsortedList.forEach(element => {
        let row = document.createElement("tr");
        let td1 = document.createElement("td");
        td1.appendChild(document.createTextNode(`${element["created"]}`));
        td1.id = `${counter}-created`
        let td2 = document.createElement("td");
        td2.appendChild (document.createTextNode(
            element["cpu"]?.toFixed(2)
        ));
        td2.id = `${counter}-cpu`
        row.appendChild(td1);
        row.appendChild(td2);
        tbody.appendChild(row);
        counter++;
    });
};

updateMainTable();
setInterval(async() => {
   updateMainTable();
} , 10000);



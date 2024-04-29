const url = "http://127.0.0.1:8000"

const doRequest = async(url) => {
    let response = await fetch(url);
    return await response.json();
}




const toSort = (how, list) => {
    switch(how) {
        case "lower":
            return list.sort((a, b) => a.cpu > b.cpu ? 1 : -1);
        case "upper":
            return list.sort((a, b) => a.cpu < b.cpu ? 1 : -1);
    }
}

setInterval(async() => {
    let response = await doRequest(`${url}/get_new/`)
    // updateTable(response["result"]);
    let tbody = document.querySelector("#table_body")
    tbody.innerHTML = '';
    response["result"]["rows"].forEach(element => {
        var row = document.createElement("tr")
        var td1 = document.createElement("td")
        td1.appendChild(document.createTextNode(`${element["created"]}`))
        var td2 = document.createElement("td")
        td2.appendChild (document.createTextNode(`${element["cpu"]}`))
        row.appendChild(td1);
        row.appendChild(td2);
        tbody.appendChild(row);
    });
} , 10000);

const updateTable = (list) => { 
     for (let i = 0; i < list.length; i++) {
        let created = document.getElementById(`${i+1}-created`);
        let cpu = document.getElementById(`${i+1}-cpu`);
        created.textContent = (list[i]["created"]);
        cpu.textContent = list[i]["cpu"].toFixed(2);
    }
}

const toSortDescending = async () => {
    let response = await doRequest(`${url}/get_new/`)
    let sortedList = toSort("upper", response["result"])
    updateTable(sortedList)
};

const toSortAscending = async () => {
    let response = await doRequest(`${url}/get_new/`)
    let sortedList = toSort("lower", response["result"])
    updateTable(sortedList)
};



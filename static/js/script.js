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

const updateTable = (list) => {
     for (let i = 0; i < list.length; i++) {
        let created = document.getElementById(`${i+1}-created`);
        let cpu = document.getElementById(`${i+1}-cpu`);
        created.textContent = (list[i]["created"]);
        cpu.textContent = list[i]["cpu"].toFixed(2);
    }
}

const toSortDescending = async () => {
    let response = await doRequest("http://127.0.0.1:8000/get_new/")
    let sortedList = toSort("upper", response["result"])
    updateTable(sortedList)
};

const toSortAscending = async () => {
    let response = await doRequest("http://127.0.0.1:8000/get_new/")
    let sortedList = toSort("lower", response["result"])
    updateTable(sortedList)
};



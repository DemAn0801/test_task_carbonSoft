const URL = "http://127.0.0.1:8000";
let sortMethod = "chronic";

const doRequest = async(url) => {
    let response = await fetch(url);
    return await response.json();
};

const toSort = (how, list) => {
    switch(how) {
        case "chronic":
            return list.sort((a, b) => a.created < b.created ? 1 : -1);
        case "lower":
            return list.sort((a, b) => a.cpu > b.cpu ? 1 : -1);
        case "upper":
            return list.sort((a, b) => a.cpu < b.cpu ? 1 : -1);
    };
};

const toSortDescending = async(target) => {
    let buttons = document.querySelectorAll(".btn.my_btn");
    buttons.forEach(el => el.classList.remove("active_button"));
    target.classList.add("active_button")
    sortMethod = "upper";
    let response = await doRequest(`${URL}/get_new/`);
    let sortedList = toSort(sortMethod, response["result"]["rows"]);
    updateMainTable(sortedList);
};

const toSortAscending = async(target) => {
    let buttons = document.querySelectorAll(".btn.my_btn");
    buttons.forEach(el => el.classList.remove("active_button"));
    target.classList.add("active_button")
    sortMethod = "lower";
    let response = await doRequest(`${URL}/get_new/`);
    let sortedList = toSort(sortMethod, response["result"]["rows"]);
    updateMainTable(sortedList);
};

const toSortChronic = async(target) => {
    let buttons = document.querySelectorAll(".btn.my_btn");
    buttons.forEach(el => el.classList.remove("active_button"));
    target.classList.add("active_button")
    sortMethod = "chronic";
    let response = await doRequest(`${URL}/get_new/`);
    let sortedList = toSort(sortMethod, response["result"]["rows"]);
    updateMainTable(sortedList);
};



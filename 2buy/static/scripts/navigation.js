/*Item Entry*/
const table = document.getElementById("list-table");
const addBox = document.getElementById("add-box");
const addButton = document.getElementById("add-item")
const submitButton = document.getElementById("submit-item");
const closeButton = document.getElementsByClassName("close-button")[0];

addButton.onclick = function(){
    addBox.style.display = "block";
}

closeButton.onclick = function(){
    addBox.style.display = "none";
}

window.onclick = function(event){
    if(event.target == addBox){
        addBox.style.display = "none";
    }
}

/*Logout*/
const userPage = document.getElementsByClassName("user-page");
const loginState = document.getElementById("login-state");
const logoutButton = document.getElementById("logout-button");

logoutButton.onclick = function(){
    loginState.value = "0";
    userPage.action = "/2buy-<user>";
}
const table = document.getElementById("list-table");
const addBox = document.getElementById("add-box");
const addButton = document.getElementById("add-item")
const submitButton = document.getElementById("submit-item");
const closeButton = document.getElementsByClassName("close-button")[0];

function validate(){
    let loginForm = document.getElementById("login-form");
    let username = document.getElementById("username-entry");
    let password = document.getElementById("password-entry");

    if(username.value == "backend" && password.value  == "developer"){
        loginForm.action = "/home";
    }
    else{
        loginForm.action = "#";
    }
}

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
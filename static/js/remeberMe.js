window.onload = (e) => {
    // check local storage for a remember me key
    let rememberKey = localStorage.getItem("rememberKey");
    // if the key exists, log in the user using the key
    if (rememberKey) {
        //log in the user
        console.log("logging in the user!");
    }
};

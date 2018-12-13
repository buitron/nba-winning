var scoreboard = (_id, toggle) => {
    document.getElementById(_id).classList.toggle(toggle);
};

var predict = (_class, _class2, toggle,) => {
    document.querySelector(_class).classList.toggle(toggle);

    var selector = document.querySelector(_class2);
    selector.style.display = selector.style.display === 'block' ? 'none' : 'block';
};

window.onload = () => {
    var reloading = sessionStorage.getItem("reloading");
    if (reloading) {
        sessionStorage.removeItem("reloading");
        predict('.dataframe', '.centered', 'ml-active');
    }
}

reloadP = () => {
    sessionStorage.setItem("reloading", "true");
    document.location.reload();
}

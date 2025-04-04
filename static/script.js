function setCookie() {
    let value = document.getElementById("cookieValue").value;
    document.cookie = `challenge=${value}; path=/`;
    alert("Cookie Set! Now check your progress.");
}

function updateResponseHeader() {
    var inputElement = document.getElementById("headerInput");
    var headerValue = inputElement.value;
    alert(headerValue);
    var headerDisplayElement = document.getElementById("headerDisplay");
    headerDisplayElement.textContent = headerValue;
}
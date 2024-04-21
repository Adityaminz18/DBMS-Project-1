document.getElementById("signup-form").addEventListener("submit", function(event) {
    var username = document.getElementById("username");
    var email = document.getElementById("email");
    var password = document.getElementById("password");
    var usernameError = document.getElementById("username-error");
    var emailError = document.getElementById("email-error");
    var passwordError = document.getElementById("password-error");
    var isValid = true;

    usernameError.innerHTML = "";
    emailError.innerHTML = "";
    passwordError.innerHTML = "";

    if (username.value.trim() === "") {
        usernameError.innerHTML = "Username is required";
        isValid = false;
    }

    if (email.value.trim() === "") {
        emailError.innerHTML = "Email is required";
        isValid = false;
    } else if (!isValidEmail(email.value.trim())) {
        emailError.innerHTML = "Invalid email format";
        isValid = false;
    }

    if (password.value.trim() === "") {
        passwordError.innerHTML = "Password is required";
        isValid = false;
    }

    if (!isValid) {
        event.preventDefault();
    }
});

function isValidEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

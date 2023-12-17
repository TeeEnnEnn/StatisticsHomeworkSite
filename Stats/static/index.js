document.addEventListener('DOMContentLoaded', function () {

    const navigationShade = document.getElementById("navigation-shade")
    const shadeExit = document.getElementById("shade-exit");
    const shadeButton = document.getElementById("shade-button");

    // This button clik make the shade appear
    shadeButton.addEventListener("click", function () {
        navigationShade.classList.remove("hide");
    });

    // This button click makes the shade disappear
    shadeExit.addEventListener("click", function () {
        navigationShade.classList.add("hide");
    });

    const formValueField = document.getElementById("form-value");
    let darkMode = false;
    let nightButtonHTML = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" fill=\"currentColor\"\n" +
        "class=\"bi bi-moon-stars-fill\" viewBox=\"0 0 16 16\">\n" +
        "<path d=\"M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z\"></path>\n" +
        "<path d=\"M10.794 3.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387a1.734 1.734 0 0 0-1.097 1.097l-.387 1.162a.217.217 0 0 1-.412 0l-.387-1.162A1.734 1.734 0 0 0 9.31 6.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387a1.734 1.734 0 0 0 1.097-1.097l.387-1.162zM13.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732l-.774-.258a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L13.863.1z\"></path>\n" +
        "</svg>";
    let dayButtonInnerHTML = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" fill=\"currentColor\" class=\"bi bi-sun-fill\" viewBox=\"0 0 16 16\">\n" +
        "<path d=\"M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z\"/>\n" +
        "</svg>";

    function setThemePreference(theme) {
        localStorage.setItem("themePreference", theme);
    }

    function getThemePreference() {
        return localStorage.getItem("themePreference");
    }

    const nightButton = document.getElementById("night-mode");
    const nightModePrompt = document.getElementById("night-mode-prompt");


    if (getThemePreference() === "light") {
        // If the day mode stylesheet is preferred
        nightButton.innerHTML = nightButtonHTML;
        nightModePrompt.innerHTML = "Change To Night Mode";
        changeTheme("light");
    } else {
        // If the night mode stylesheet is preferred
        nightButton.innerHTML = dayButtonInnerHTML;
        nightModePrompt.innerHTML = "Change To Day Mode";
        changeTheme("dark");
    }

    // This button changes the theme of the page.
    nightButton.addEventListener("click", function () {
        if (darkMode === false) {
            nightButton.innerHTML = dayButtonInnerHTML;
            nightModePrompt.innerHTML = "Change To Day Mode";
            changeTheme("dark")
            darkMode = true;
            setThemePreference("dark")
        } else {
            changeTheme("light")
            nightButton.innerHTML = nightButtonHTML;
            nightModePrompt.innerHTML = "Change To Night Mode";
            darkMode = false;
            setThemePreference("light")
        }
    });

});


function changeTheme(theme) {
    if (theme === "dark") {  // Dark theme colors
        document.documentElement.style.setProperty("--background-color", "rgb(25, 31, 38)");
        document.documentElement.style.setProperty("--bubble-color", "rgb(68, 70, 86)");
        document.documentElement.style.setProperty("--shadow", "0px 0px 7px rgba(139, 140, 147, 0.75)");
        document.documentElement.style.setProperty("--text-color", "white");
        document.documentElement.style.setProperty("--background-color-transparent", "rgba(12, 31, 38, 0.85)")
    } else {  // Light theme colors
        document.documentElement.style.setProperty("--background-color", "rgb(251, 251, 251)");
        document.documentElement.style.setProperty("--bubble-color", "#a9d5ff");
        document.documentElement.style.setProperty("--shadow", "0 0 10px 2px rgb(25 0 255 / 75%)");
        document.documentElement.style.setProperty("--text-color", "black");
        document.documentElement.style.setProperty("--background-color-transparent", "rgb(251, 251, 251, 0.85)");
    }
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('reset-button').addEventListener('click', async function () {
        fetch('/reset-data', {
            method: 'POST',
        })
            .then(response => response.json())
            .then(data => {
                console.log(data.message);
                resetForm();
                // Replace the current history entry with a new one that has the same URL but no form data
                window.history.replaceState({}, document.title, window.location.href);
                location.reload();
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    function resetForm() {
        let formValueField = document.getElementById("form-value");
        // Store the value in the sessionStorage object with the key "formValue"
        sessionStorage.setItem("formValue", formValueField.value);
        formValueField.value = "";
    }


    // When the page is reloaded, check if there is a value stored in the sessionStorage object
    let storedValue = sessionStorage.getItem("formValue");
    if (storedValue) {
        // If there is, clear it and set the form value field to an empty string
        sessionStorage.clear();
        document.getElementById("form-value").value = "";
    }

    // To select and focus on the value that is already in the form.
    window.addEventListener("load", function () {
        let myFormInput = document.getElementById("form-value");
        myFormInput.focus();
        myFormInput.select();
    });

    let options = document.querySelectorAll(".option");
    options.forEach(option =>{
        if (dataSetSize < 3){
            option.classList.add("hide");
        }
    })

    /*    // To make the alert grid disappear when it is no longer in use
        const flashMessage = document.querySelector(".flash-message");
        if (flashMessage){
            setTimeout(function (){
                flashMessage.classList.add("alert-complete");
            }, 3000)
        }*/

});

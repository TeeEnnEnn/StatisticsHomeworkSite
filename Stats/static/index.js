document.addEventListener('DOMContentLoaded', function () {
    const formValueField = document.getElementById("form-value");

    // Reset the value in the field
    function resetForm() {
        sessionStorage.setItem("formValue", formValueField.value);
        formValueField.value = "";
    }

    // To select and focus on the value that is already in the form.
    window.addEventListener("load", function () {
        formValueField.focus();
        formValueField.select();
    });

    // To hide the Ascending and Descending options on the current data set
    let options = document.querySelectorAll(".option");
    options.forEach(option => {
        if (dataSetSize < 3) {
            option.classList.add("hide");
        }
    });

// Add event listener for double-click on data-value elements
    const dataGrid = document.querySelector(".data-set-grid");
    dataGrid.addEventListener("dblclick", async function (event) {
        const element = event.target;
        if (element.classList.contains("data-value")) {
            const index = element.id.split("-")[1];
            const data = {"index": index};

            // Send a POST request to your Flask app to delete the item from the data_set
            const response = await fetch('/delete-item', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                // If the deletion was successful, remove the element from the DOM
                element.remove();
                console.log(formValueField.value);
                resetForm();
                window.history.replaceState({}, document.title, window.location.href);
                location.reload();
            } else {
                // Handle error if needed
                console.error('Error:', response.statusText);
            }
        }
    });


});

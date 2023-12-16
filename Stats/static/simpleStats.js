document.addEventListener("DOMContentLoaded", function () {
    let dataset = [];
    let dataGrid = document.getElementById("data-grid");

    function updateUI() {
        if (dataset.length !== 0) {
            dataGrid.innerHTML = "";
            dataGrid.style.display = "grid";
            dataset.forEach((value, index) => {
                const pElement = document.createElement("p");
                pElement.className = "data-value center";
                pElement.id = `value-${index}`;
                pElement.textContent = value;
                dataGrid.appendChild(pElement);
            });
        } else {
            dataGrid.innerHTML = "";
            dataGrid.style.display = "block";
            let emptyP = document.createElement("p");
            emptyP.textContent = "The data set is empty";
            dataGrid.appendChild(emptyP);
        }
    }

    let simpleForm = document.getElementById("simple-submission");
    simpleForm.addEventListener("submit", function (event) {
        event.preventDefault();
        let formData = new FormData(simpleForm)
        let rounding = formData.get("rounding");
        let value = formData.get("value");

        dataset.push(value);
        updateUI();
    });

    let ascending = document.getElementById("ascending-button");
    let descending = document.getElementById("descending-button");

    ascending.addEventListener("click", function () {
        dataset.sort((a, b) => a - b);
        updateUI();
    });

    descending.addEventListener("click", function () {
        dataset.sort((a, b) => b - a);
        updateUI();
    })


});
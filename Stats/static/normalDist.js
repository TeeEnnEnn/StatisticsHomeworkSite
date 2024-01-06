if (window.location.href.includes("normal")) {
    document.addEventListener("DOMContentLoaded", function () {
        const normalForm = document.getElementById("normal-distribution");
        normalForm.addEventListener("submit", async function (event) {
            event.preventDefault();
            let formData = new FormData(normalForm);

            let x = Number(formData.get("x"));
            let sd = Number(formData.get("sd"));
            let mean = Number(formData.get("mean"));

            await sendForCalculation(x, mean, sd);
        });
    });

    async function sendForCalculation(x, mean, sd) {
        fetch("/complex/normal", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({x: x, mean: mean, sd: sd})
        }).then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error. Status: ${response.status}`);
            }
            return response.json();
        }).then((data) => {
            if (data.message === "error") throw new Error(`Internal Server Error. Error: ${data.error}`)
            updateResults(data.probability);
        }).catch((error) => {
            console.error(error);
        })
    }

    function updateResults(probability) {
        document.getElementById("probability").textContent = `Probability = ${probability}`;
    }
}
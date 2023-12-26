if (window.location.href.includes("normal")){
    document.addEventListener("DOMContentLoaded", function (){
        const normalForm = document.getElementById("normal-distribution");
        normalForm.addEventListener("submit", function (event){
            event.preventDefault();
            let formData = new FormData(normalForm);
        })
    })
}
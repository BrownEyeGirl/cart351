
window.onload = function () {
  console.log("loaded script_post.js");
 document
    .querySelector("#insertPlantFormFetchPost")
    .addEventListener("submit", async function (event) {
      event.preventDefault();
      console.log("post form clicked")
      // format the data from the form and package it using formData
let form = document.querySelector("#insertPlantFormFetchPost");
let data = new FormData(form);

// fetch the data from the flask application using the built url, and log the response to the console
try {
        let res = await fetch("/postPlantFormFetch", {
          method: "POST", // use post method to send data to the server
          body: data, // send the form data as the body of the request
        });
        let resJSON = await res.json();
        console.log(resJSON);
      } catch (err) {
        console.log(err);
    }


})

};
// NOTE: we are NOT reloading the page, we are just updating the innerHTML of the result-container div with the new image path returned from the server. This is a common technique used in single-page applications (SPAs) to update the UI without a full page reload.
document.querySelector("#result-container").innerHTML = `<img src = ${resJSON.imagePath} />` 



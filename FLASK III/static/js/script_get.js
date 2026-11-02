 
window.onload = function () {
  console.log("loaded script_get.js");
  document
    .querySelector("#insertPlantFormFetch")
    .addEventListener("submit", async function (event) {
      event.preventDefault();
      console.log("button clicked");
    });
};

const htmlForm = document.querySelector("#insertPlantFormFetch"); // get form element by its ID 
const formData = new FormData(htmlForm); // FormData can take an HTML form as a parameter upon making a new instance, and will automatically populate the object with the form's current keys & values using the name property of each element for the keys and their submitted value for the values.
const queryParams = new URLSearchParams(formData).toString(); // format key/value pairs as query parameters for a URL. This is a built-in JS object that can take a FormData object as a parameter upon making a new instance, and will automatically populate the object with the form's current keys & values using the name property of each element for the keys and their submitted value for the values.
const url = `/getDataFromForm?${queryParams}`; // build the url, done using a GET request

// fetch the data from the flask application using the built url, and log the response to the console
try{
    let res = await fetch(url)
    let resJSON = await res.json()
      console.log(resJSON)

}
catch(err) { 
  console.log(err)
}

document.querySelector("#result-container").innerHTML += 
       ` THE NEW RESULT: ${resJSON.data_received}
        OWNER NAME : ${resJSON.owner}
        PLANT NAME : ${resJSON.plantname}`
  
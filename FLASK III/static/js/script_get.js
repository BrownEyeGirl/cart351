 
window.onload = function () {
  console.log("loaded script_get.js");
  document
    .querySelector("#insertPlantFormFetch")
    .addEventListener("submit", async function (event) {
      event.preventDefault();
      console.log("button clicked");
    });
};
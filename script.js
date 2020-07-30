console.log("coucou");

function envoiDonnees() {
  let formData = new FormData(document.getElementById("form"));
  let object = {};
  formData.forEach(function(value, key){
    object[key] = value;
  });
  let json = JSON.stringify(object);
  console.log(json);
  return
}


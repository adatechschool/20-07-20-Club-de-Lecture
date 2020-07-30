console.log("coucou");

function envoiDonnees() {
  let formData = new FormData(document.getElementById("form"));
  let object = {};
  formData.forEach(function(value, key){
    object[key] = value;
  });
  let json = JSON.stringify(object);

  var req = new XMLHttpRequest();
  req.open("POST", "https://clublecture.herokuapp.com/api/users");

  req.send(json);
  console.log(json);
  return
}

console.log("coucou");

function envoiDonnees() {
  let formData = new FormData(document.getElementById("form"));
  let object = {};
  formData.forEach(function(value, key){
    object[key] = value;
  });
  let json = JSON.stringify(object);

  var req = new XMLHttpRequest();
  req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 201){
      document.getElementById("test").innerHTML = "votre compte a bien été créé";}
    else {
      document.getElementById("test").innerHTML = "votre compte n'a pas peu être créé";
    }
  };
  req.open("POST", "https://clublecture.herokuapp.com/api/users");
  req.send(json);

  return
}


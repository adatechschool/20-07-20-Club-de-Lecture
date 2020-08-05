function envoiPublication()
{
  let publication = new FormData(document.getElementById("formulaire"))
  let object = {};
  publication.forEach(function(value, key){
    object[key] = value;
  });
  object['user_name'] = "Toto";
  console.log(object)

  let json = JSON.stringify(object);

  var req = new XMLHttpRequest();
  req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 201){
      document.getElementById("message").innerHTML = "votre publication a bien été postée";}
    else if (this.readyState == 4) {
      document.getElementById("message").innerHTML = "votre publication n'a pas pu être postée";
    }
  };
  req.open("POST", "https://clublecture.herokuapp.com/api/posts");
  req.send(json);

  return


}

function compteur()
{
 const limit = 10;

 let valeur = document.querySelector('textarea').value;
 console.log(valeur);
 document.querySelector('p').innerHTML= limit - valeur.length;
if (valeur.length > limit){
  document.querySelector('button').disabled = true;
}else{
  document.querySelector('button').disabled = false;
}
}

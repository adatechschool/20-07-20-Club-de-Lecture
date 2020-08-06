window.onload = function() {
  fetch_publications();
}

function fetch_publications() {
  var req = new XMLHttpRequest();
  req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var publications = JSON.parse(this.responseText)
      for (i in publications) {
        document.body.append(create_div(publications[i]));
      }

    }
  };
  req.open("GET", "http://localhost:8000/api/posts")
  req.send();
}

function create_div(publication) {
//  console.log(publication)
  var new_div = document.createElement('div');

  new_div.innerHTML =`
  <div class ="userName">
    ${publication.user_name}
  </div>
  <div class ="publicationContent">
    ${publication.description}
  </div>
  <div id="zoneEdition_${publication.id}" style="display:none;">
  <textarea >${publication.description}</textarea>
  <div class = "publicationDate">
    ${publication.creation_date}
  </div>
  <button type="button" onclick="enregistrerModifications(${publication.id},'${publication.user_name}')" >
    Enregistrer
  </button>
  </div>
  <button type="button" onclick="modifierPublication(${publication.id})">
    Modifier
  </button>`;
  return new_div;
}

function enregistrerModifications(numeroClique,userNameCorrespondant){

  let newText = document.querySelector(`#zoneEdition_${numeroClique} textarea`).value ;
  console.log(newText);

  let object = {};
  object['description'] = newText;

  console.log(object)

  let json = JSON.stringify(object);
  var req = new XMLHttpRequest();
  req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200){
      console.log("ça marche")
    }
    else if (this.readyState == 4) {
      console.log("ça marche pas")
    }
  };
  let url = `http://localhost:8000/api/posts/${userNameCorrespondant}/${numeroClique}`
  req.open("PUT", url);
  req.send(json);

}

function modifierPublication(numeroClique) {
  console.log("fonction de modification de la publication numero " + numeroClique)
  let boite = document.getElementById("zoneEdition_"+numeroClique)
  boite.style.display = "block";
}

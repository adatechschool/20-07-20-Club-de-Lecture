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
  req.open("GET", "https://clublecture.herokuapp.com/api/posts")
  req.send();
}

function create_div(publication) {
  var new_div = document.createElement('div');

  new_div.innerHTML =`
  <div class ="userName">
    ${publication.user_name}
  </div>
  <div class ="publicationContent">
    ${publication.description}
  </div>
  <textarea name="" id="boiteDeSaisie_${publication.id}" style="display:none;">
    ${publication.description}
  </textarea>
  <div class = "publicationDate">
    ${publication.creation_date}
  </div>
  <button type="button" onclick="modifierPublication(${publication.id})">
    Modifier
  </button>`;
  return new_div;
}

function modifierPublication(numeroClique) {
  console.log("fonction de modification de la publication numero " + numeroClique)
  let boite = document.getElementById("boiteDeSaisie_"+numeroClique)
  boite.style.display = "block";
}

window.onload = function() {
  fetch_publications();
}

function fetch_publications() {
  var req = new XMLHttpRequest();
  req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var publications = JSON.parse(this.responseText)
      for(i in publications) {
        document.body.append(create_div(publications[i]));
      }

    }
  };
  req.open("GET", "https://clublecture.herokuapp.com/api/posts")
  req.send();
}

function create_div(publication) {
  var new_div = document.createElement('div')
  new_div.innerHTML = publication.user +
                      ' ' +
                      publication.description +
                      ' ' +
                      publication.creation_date;
  return new_div;
}

      // <div id="cunediv">
      //   <p class="user"></p>
      //   <p class="description"></p>
      //   <p class="creation_date"></p>
      // </div>

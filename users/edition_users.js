window.onload = function() {
  fetch_users();
}

function fetch_users() {
  var req = new XMLHttpRequest();
  req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var user_list = JSON.parse(this.responseText)
      for (i in user_list) {
        document.body.append(create_div(user_list[i]));
      }

    }
  };
  req.open("GET", "http://localhost:8000/api/users")
  req.send();
}

function create_div(user_list) {
//  console.log(publication)
  var new_div = document.createElement('div');

  new_div.innerHTML =`
  <div class ="userName">
    ${user_list.user_name}
  </div>
  <div class ="email">
    ${user_list.email}
  </div>
  <div class ="creation_date">
   ${user_list.creation_date};
  </div>

`;

  return new_div;
}

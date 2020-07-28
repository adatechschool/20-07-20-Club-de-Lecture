function displayResult (str)
{
    document.body.innerHTML += str
}

function sendFormJSON ()
{
    const formulaire = document.getElementById("inscription")
    const formData = new FormData(formulaire)
    var d = {}
    formData.forEach (function(v, k) {
        d[k] = v
    });
    dataStr = JSON.stringify(d)

    fetch ('https://clublecture.herokuapp.com/api/users',
           {
           method: "POST",
           body: dataStr,
           headers: {
               'Content-Type': 'application/json'
               }
           })
    .then(res => displayResult(res))
    .catch(err => displayResult(err))
}

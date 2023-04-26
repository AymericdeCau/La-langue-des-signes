const b_connection = document.getElementById("sign_in");  // on récupère notre bouton connexion
const indentification = document.querySelector("div.identification");
const bonjour = document.querySelector("h3.h3_bonjour");
const déconnection = document.querySelector("#sign_out");
console.log(déconnection)
// fonction permettant de récupérer les paramètres de l'url
function findGetParameter(parameterName) {
    var result = "aucun",
        tmp = [];
    var items = window.location.search.substring(1).split("&");
    for (var index = 0; index < items.length; index++) {
        tmp = items[index].split("=");
        if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    }
    return result;
}

// on modifie notre page en fonction de ces paramètres
var nom = findGetParameter("name");
if (nom != "aucun") {
    indentification.style.display = "none";
    bonjour.textContent = "Vous êtes connecté à la plateforme LLM."
    bonjour.classList.add("le_bonjour");
    déconnection.classList.add("la_déconnection");
}



var cookies = findGetParameter("cookies");
console.log(nom, cookies)

if (nom != "aucun") {
    var a = document.querySelectorAll("a:not(.b_sommaire)");
    for (let i = 0; i < a.length; i++){
        a[i].href += "?name=" + nom;
    }
    document.getElementById("b_connexion").textContent = nom;
    document.getElementById("b_connexion").title = nom;
}

if (cookies != "aucun") {
    var a = document.querySelectorAll("a:not(.non_lien)");
    for (let i = 0; i < a.length; i++){
        if (nom != "aucun") {
            a[i].href += "&cookies=" + cookies;
       } else {
           a[i].href += "?cookies=" + cookies;
       }
    }
}


b_connection.addEventListener("click", () => {
    var le_nom = document.getElementById("username").value;
    var a = document.querySelectorAll("a:not(.b_sommaire)");
    for (let i = 0; i < a.length; i++){
        if (nom != "aucun" || cookies != "aucun") {
            var items = window.location.search.substring(1);
            console.log(a[i].href,"   ",  le_nom,"   ",  cookies, "   ", items);
            var liste = a[i].href.split("?");
            console.log("la liste : ", liste);
            a[i].href = liste[0];
            console.log(a[i].href,"   ",  le_nom,"   ",  cookies);
        }
        console.log(a[i].href,"   ", le_nom,"   ",  cookies, "2");
        a[i].href += "?name=" + le_nom + "&cookies=" + cookies;
        console.log(a[i].href,"   ",  le_nom,"   ",  cookies, "2");
    }
    document.getElementById("b_connexion").textContent = le_nom;
    document.getElementById("b_connexion").title = le_nom;


    indentification.style.display = "none";
    bonjour.textContent = "Bonjour " + le_nom + ", vous êtes maintenant connecté à la plateforme LLM !"
    bonjour.classList.add("le_bonjour");
    déconnection.classList.add("la_déconnection");
})


déconnection.addEventListener("click", () => {
    var a = document.querySelectorAll("a:not(.b_sommaire)");
    for (let i = 0; i < a.length; i++){
        var liste = a[i].href.split("?");
        if (cookies != "aucun") {
            a[i].href = liste[0] + "?cookies=" + cookies;
        } else {
            a[i].href = liste[0];
        }
    document.querySelector("#b_connexion").textContent = "Connexion";
    document.querySelector("#b_connexion").title = "Connexion";

    indentification.style.display = "grid";
    bonjour.classList.remove("le_bonjour");
    déconnection.classList.remove("la_déconnection");
}})


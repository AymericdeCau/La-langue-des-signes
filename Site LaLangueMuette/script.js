const b_connection = document.getElementById("sign_in");  // on récupère notre bouton connexion
const flèche_sommaire = document.getElementById("flèche_sommaire"); // on récupère notre bouton_sommaire pour la partie du sommaire

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
var cookies = findGetParameter("cookies");

console.log(nom,cookies)

if (nom != "aucun") {
    var a = document.querySelectorAll("a:not(.non_lien)");
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

function delay() {
    console.log("ha");
    setTimeout(popupVisible, 2000);
}

function changementUrl(choix) {
    var a = document.querySelectorAll("a:not(.non_lien)");
    for (let i = 0; i < a.length; i++){
        if (nom != "aucun") {
            a[i].href += "&cookies=" + choix;
       } else {
           a[i].href += "?cookies=" + choix;
       }
}}

function popupVisible () {
    document.querySelector("#popup").classList.add("popup");
    document.querySelector(".cross").addEventListener("click", () => {
        document.querySelector("#popup").classList.remove("popup");
        changementUrl("refuser")
    })
    document.querySelector("#choice_1").addEventListener("click", () => {
        document.querySelector("#popup").classList.remove("popup");
        changementUrl("accepter")
    })
    document.querySelector("#choice_2").addEventListener("click", () => {
        document.querySelector("#popup").classList.remove("popup");
        changementUrl("refuser")
    })
}

if (cookies == "aucun") {
    delay();
}


function sommaireOuverture() {
    const sommaire = document.querySelector(".sommaire");
    const choix = document.querySelector(".sommaire ul");

    if (choix.style.display != "block") {
    flèche_sommaire.src = "./asserts/flèche-développer.png";
    flèche_sommaire.title = "réduire le sommaire"
    choix.style.display = "block";
    sommaire.style.maxWidth = "150px";
    sommaire.style.opacity = "1";
    } else {
    flèche_sommaire.src = "./asserts/flèche-avant.png";
    flèche_sommaire.title = "développer le sommaire"
    choix.style.display = "none";
    sommaire.style.maxWidth = "125px";
    sommaire.style.opacity = "0.6";
    }
}

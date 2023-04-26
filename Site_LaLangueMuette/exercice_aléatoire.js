const b1 = document.getElementById("b1");
const b2 = document.getElementById("b2");
const b3 = document.getElementById("b3");

const im1 = document.getElementById("img_qst_1");
const im2 = document.getElementById("img_qst_2");
const im3 = document.getElementById("img_qst_3");

const b_suivant = document.getElementById("b_suivant");

const correct = document.getElementById("correct");
const faux = document.getElementById("faux");

const étoile1 = document.getElementById("star1");
const étoile2 = document.getElementById("star2");
const étoile3 = document.getElementById("star3");
const étoile4 = document.getElementById("star4");
const étoile5 = document.getElementById("star5");

const bravo = document.getElementById("bravo_niv");

var begin = 1;
var answer;
var essaie = 0;
var score = 0;


function interrogation (array) {

  var correction = 0;
  answer = 0;

  var rand = Math.floor(Math.random()*array.length);
  var bonneReponse = array[rand];
  array.splice(rand, 1);

  document.getElementById("la_question").textContent = "Quel est le signe pour " + bonneReponse[0] + " ?  ";
  document.getElementById("le_score").textContent = "Résultat : " + score + "/" + essaie;

  var rand = Math.floor(Math.random()*array.length);
  var mauvaiseReponse1 = array[rand];
  array.splice(rand, 1);

  var rand = Math.floor(Math.random()*array.length);
  var mauvaiseReponse2 = array[rand];
  
  array.push(bonneReponse);
  array.push(mauvaiseReponse1);

  var rand = Math.floor(Math.random()*3);
  if (rand == 0) {var fList = [bonneReponse, mauvaiseReponse1, mauvaiseReponse2]};
  if (rand == 1) {var fList = [mauvaiseReponse1, bonneReponse, mauvaiseReponse2]};
  if (rand == 2) {var fList = [mauvaiseReponse1, mauvaiseReponse2, bonneReponse]};

  faux.textContent = "La solution était le signe n°" + (rand + 1) + " .";
  var a = fList[0][1].length-4;
  var b = fList[0][1].length-4;
  var c = fList[0][1].length-1;
  im1.src = fList[0][1].substr(0,a) + "_ex" + fList[0][1].substr(b,c);
  a = fList[1][1].length-4;
  b = fList[1][1].length-4;
  c = fList[1][1].length-1;
  im2.src = fList[1][1].substr(0,a) + "_ex" + fList[1][1].substr(b,c);
  a = fList[2][1].length-4;
  b = fList[2][1].length-4;
  c = fList[2][1].length-1;
  im3.src = fList[2][1].substr(0,a) + "_ex" + fList[2][1].substr(b,c);

  b1.addEventListener("click", () => {
    if (correction == 0) {
      if (rand == 0) {
        correct.classList.add("show");
        b1.style.border = "2px solid green";
        score+=1;
      } else {
        faux.classList.add("show");
        b1.style.border = "2px solid red";
      }
    correction ++;
    answer = 1;
    essaie += 1;
    }
  })
  b2.addEventListener("click", () => {
    if (correction == 0) {
      if (rand == 1) {
        correct.classList.add("show");
        b2.style.border = "2px solid green";
        score+=1;
      } else {
        faux.classList.add("show");
        b2.style.border = "2px solid red";
      }
    correction ++;
    answer = 1;
    essaie += 1;
    }
  })
  b3.addEventListener("click", () => {
    if (correction == 0) {
      if (rand == 2) {
        correct.classList.add("show");
        b3.style.border = "2px solid green";
        score+=1;
      } else {
        faux.classList.add("show");
        b3.style.border = "2px solid red";
      }
    correction ++;
    answer = 1;
    essaie += 1;
    }
  })

}

function questionnaire (array) {
  if (begin == 1) {
    interrogation(array);
    begin = 0;
  }
  b_suivant.addEventListener("click", () => {
  if (answer == 1) {
    console.log(essaie, score/essaie, essaie > 1 && score/essaie > 0.5 )
    if (essaie > 5 && score/essaie > 0.5) { étoile1.src = "./asserts/étoile-pleine.png";}
    if (essaie > 10 && score/essaie > 0.6) { étoile2.src = "./asserts/étoile-pleine.png";}
    if (essaie > 15 && score/essaie > 0.7) { étoile3.src = "./asserts/étoile-pleine.png";}
    if (essaie > 20 && score/essaie > 0.8) { étoile4.src = "./asserts/étoile-pleine.png";}
    if (essaie > 30 && score/essaie > 0.9) { 
      étoile5.src = "./asserts/étoile-pleine.png";
      bravo.style.visibility = "visible";
    }
    correct.classList.add("delete");
    faux.classList.add("delete");
    correct.classList.remove("show");
    faux.classList.remove("show");
    correct.classList.remove("delete");
    faux.classList.remove("delete");
    b1.style.border = "1px solid rgb(0,0,0)";
    b1.style.border.radius = "5px";
    b2.style.border = "1px solid rgb(0,0,0)";
    b2.style.border.radius = "5px";
    b3.style.border = "1px solid rgb(0,0,0)";
    interrogation(array);

  }
  })
}

questionnaire(array, 3);
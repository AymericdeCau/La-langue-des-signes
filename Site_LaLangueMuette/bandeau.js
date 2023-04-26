document.write(`
<header>
<nav>
    <ul class="bandeau">
        <li id="logo"><a href="./index.html" title="Page d'accueil de LLM"><img src="./asserts/logo.jpg" class="logo" alt="logo"></a></li>
        <li id="accueil"><a href="./index.html" title="Page d'accueil de LLM" class="bouton">Accueil</a></li>
        <li id="apprendre">
            <a class="bouton">Apprendre</a>
            <div class="ruban_déroule">
                <ul class="liste_déroule">
                    <li><a href="./cours.html" class="menu_déroule" title="Aller à la page Cours">Cours</a></li>
                    <li><a href="./exercice.html" class="menu_déroule" title="Aller à la page Exercices">Exercices</a></li>
                </ul></div>
        </li>
        <li id="cours">
            <a href="./cours.html" class="bouton" title="Aller à la page Cours">Cours</a>
            <div class="ruban_déroule">
                <ul class="liste_déroule">
                    <li><a href="./A-H.html" class="menu_déroule" >Les lettres de A à H</a></li>
                    <li><a href="./I-P.html" class="menu_déroule">Les lettres de I à P</a></li>
                    <li><a href="./Q-Z.html" class="menu_déroule" >Les lettres de Q à Z</a></li>
                    <li><a href="./0-9.html" class="menu_déroule" >Les chiffres de 0 à 9</a></li>
                    <li><a href="./Exp_courantes_1.html" class="menu_déroule" >Expressions courantes n°1</a></li>
                    <li><a href="./Exp_courantes_2.html" class="menu_déroule" >Expressions courantes n°2</a></li>
                    <li><a href="./Les émotions.html" class="menu_déroule" >Les émotions</a></li>
                    <li><a href="./Les verbes usuels.html" class="menu_déroule" >Les verbes usuels</a></li>
                </ul>
        </li>
        <li id="exercice">
            <a href="./exercice.html" class="bouton"title="Aller à la page Exercices">Exercices</a>
            <div class="ruban_déroule">
                <ul class="liste_déroule">
                    <li><a href="./Exercice_1.html" class="menu_déroule" >Les caractères de base</a></li>
                    <li><a href="./Exercice_2.html" class="menu_déroule">Les quelques mots pour discuter</a></li>
                    <li><a href="./Exercice_Total.html" class="menu_déroule" >Tout à la fois</a></li>
                </ul>
        </li>
        <li id="journal"><a href="./journal.html" class="bouton" title="Aller à la page Journal">Crédit</a></li>
        <li id="connexion"><a href="./connexion.html" id="b_connexion" title="Connexion">Connexion</a></li>
    </ul>
</nav>
</header>

`);
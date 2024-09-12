/*********************************************************************************
 * 
 * Ce fichier contient toutes les fonctions n�cessaires � l'affichage et � la 
 * fermeture de la popup de partage. 
 * 
 *********************************************************************************/


/**
 * Cette fonction affiche la popup pour partager son score. 
 */
function afficherPopup() {
    let popupBackground = document.querySelector(".popupBackground")
    // La popup est masqu�e par d�faut (display:none), ajouter la classe "active"
    // va changer son display et la rendre visible. 
    popupBackground.classList.add("active")
}

/**
 * Cette fonction cache la popup pour partager son score. 
 */
function cacherPopup() {
    let popupBackground = document.querySelector(".popupBackground")
    // La popup est masqu�e par d�faut (display:none), supprimer la classe "active"
    // va r�tablir cet affichage par d�faut. 
    popupBackground.classList.remove("active")
}


/**
 * Cette fonction initialise les �couteurs d'�v�nements qui concernent 
 * l'affichage de la popup. 
 */
function initAddEventListenerPopup() {
    // On �coute le click sur le bouton "partager"
    btnPartage = document.querySelector(".zonePartage button")
    let popupBackground = document.querySelector(".popupBackground")
    btnPartage.addEventListener("click", () => {
        // Quand on a cliqu� sur le bouton partag�, on affiche la popup
        afficherPopup()
    })

    // On �coute le click sur la div "popupBackground"
    popupBackground.addEventListener("click", (event) => {
        // Si on a cliqu� pr�cis�ment sur la popupBackground 
        // (et pas un autre �l�ment qui se trouve dedant)
        if (event.target === popupBackground) {
            // Alors on cache la popup
            cacherPopup()
        }
    })
}
const button = document.getElementById("calc");
const dimBut = document.getElementById("dimCalc");
const resultText = document.getElementById("result");

button.addEventListener("click", () => {
    // Récupération des valeurs
    const montant = parseFloat(document.getElementById("value1").value);
    const taux = parseFloat(document.getElementById("value2").value);

    // Validation des entrées
    if (isNaN(montant) || isNaN(taux)) {
        resultText.textContent = "Veuillez entrer des valeurs valides pour le montant et le taux.";
        return;
    }

    // Affiche un message indiquant que le calcul est en cours
    resultText.textContent = "Calcul en cours...";

    // Utilise un délai pour simuler le calcul
    setTimeout(() => {
        // Calcul du montant final
        const montantFinal = (montant * taux) / 100;
        const montantTax = montant + montantFinal

        // Affiche le résultat final après le délai
        resultText.textContent = `Le montant après ${taux}% est de ${montantTax} €`;
    }, 500);  // Délai de 500ms (ajuste si nécessaire)
});

dimBut.addEventListener("click", () => {
    // Récupération des valeurs
    const montant = parseFloat(document.getElementById("value1").value);
    const taux = parseFloat(document.getElementById("value2").value);

    // Validation des entrées
    if (isNaN(montant) || isNaN(taux)) {
        resultText.textContent = "Veuillez entrer des valeurs valides pour le montant et le taux.";
        return;
    }

    // Affiche un message indiquant que le calcul est en cours
    resultText.textContent = "Calcul en cours...";

    // Utilise un délai pour simuler le calcul
    setTimeout(() => {
        // Calcul du montant final
        const montantFinal = (montant * taux) / 100;
        const montantTax = montant - montantFinal

        // Affiche le résultat final après le délai
        resultText.textContent = `Le montant après ${taux}% est de ${montantTax} €`;
    }, 500);  // Délai de 500ms (ajuste si nécessaire)
});

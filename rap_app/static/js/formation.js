document.addEventListener("DOMContentLoaded", function () {
    console.log("📌 Script chargé !");

    // ✅ Fonction pour récupérer le CSRF Token dans les cookies
    function getCSRFToken() {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith("csrftoken=")) {
                    cookieValue = cookie.substring("csrftoken=".length, cookie.length);
                    break;
                }
            }
        }
        return cookieValue;
    }

    // ✅ 1️⃣ Mise à jour des inscrits avec confirmation
    document.querySelectorAll(".update-inscrits").forEach(input => {
        input.addEventListener("change", function () {
            let formationId = this.dataset.formationId;
            let field = this.dataset.field;
            let oldValue = this.defaultValue;
            let newValue = parseInt(this.value, 10);

            if (isNaN(newValue)) {
                alert("Veuillez entrer une valeur valide.");
                this.value = oldValue;
                return;
            }

            // ✅ Demander confirmation avant d'envoyer
            let confirmMessage = `Voulez-vous vraiment modifier "${field}" de ${oldValue} à ${newValue} ?`;
            if (!confirm(confirmMessage)) {
                this.value = oldValue; // Rétablir la valeur précédente en cas d'annulation
                return;
            }

            console.log("➡️ Données envoyées :", {
                formation_id: formationId,
                field: field,
                value: newValue
            });

            fetch(`/formations/modifier-inscrits/${formationId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    field: field,
                    value: newValue
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log("✅ Réponse serveur :", data);
                if (data.success) {
                    alert("Mise à jour réussie !");
                    location.reload(); // 🔄 Recharge la page après mise à jour
                } else {
                    alert("Erreur : " + data.error);
                    this.value = oldValue; // Rétablir la valeur précédente en cas d'erreur
                }
            })
            .catch(error => {
                console.error("❌ Erreur AJAX :", error);
                alert("Une erreur est survenue.");
                this.value = oldValue; // Rétablir la valeur précédente en cas d'échec
            });
        });
    });

    // ✅ 2️⃣ Gestion de l'affichage des colonnes avec mémorisation
    const toggleButton = document.getElementById("toggleColumns");
    if (toggleButton) {
        toggleButton.addEventListener("click", function () {
            const table = document.querySelector(".formation-table");
            if (!table) return;

            // ✅ Mise à jour des colonnes à masquer (en commençant à 0)
            const columnsToToggle = [6, 7, 8, 9]; // Prévus, Inscrits, Places, Transformation, Saturation

            // ✅ Récupération de l'état précédent des colonnes
            let hiddenColumns = JSON.parse(localStorage.getItem("hiddenColumns")) || [];

            columnsToToggle.forEach(colIndex => {
                const cells = table.querySelectorAll(`thead th:nth-child(${colIndex + 1}), tbody td:nth-child(${colIndex + 1})`);

                cells.forEach(cell => {
                    cell.classList.toggle("d-none"); // Masquer/Afficher la colonne
                });

                // ✅ Mise à jour de l'état stocké
                if (hiddenColumns.includes(colIndex)) {
                    hiddenColumns = hiddenColumns.filter(c => c !== colIndex);
                } else {
                    hiddenColumns.push(colIndex);
                }
            });

            localStorage.setItem("hiddenColumns", JSON.stringify(hiddenColumns));
            console.log("🔄 Colonnes masquées :", hiddenColumns);
        });

        // ✅ 3️⃣ Appliquer l'état des colonnes au chargement de la page
        const hiddenColumns = JSON.parse(localStorage.getItem("hiddenColumns")) || [];
        hiddenColumns.forEach(colIndex => {
            document.querySelectorAll(`thead th:nth-child(${colIndex + 1}), tbody td:nth-child(${colIndex + 1})`).forEach(cell => {
                cell.classList.add("d-none");
            });
        });

        console.log("📌 Colonnes masquées appliquées :", hiddenColumns);
    }
});



// Fonction pour récupérer le CSRF Token dans les cookies
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith("csrftoken=")) {
                cookieValue = cookie.substring("csrftoken=".length, cookie.length);
                break;
            }
        }
    }
    return cookieValue;
}

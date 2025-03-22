document.addEventListener("DOMContentLoaded", function () {
    console.log("📌 Script chargé !");

    // ✅ Fonction pour récupérer le CSRF Token
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

    // ✅ Fonction pour afficher une toast personnalisée
    function showToast(message, type = "success") {
        const toast = document.createElement("div");
        toast.className = `toast align-items-center text-bg-${type} border-0`;
        toast.role = "alert";
        toast.style.zIndex = 9999;
        toast.setAttribute("data-bs-delay", "3000");
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
            </div>
        `;

        const container = document.getElementById("toastContainer") || document.body;
        container.appendChild(toast);

        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();

        toast.addEventListener('hidden.bs.toast', () => toast.remove());
    }

    // ✅ 1️⃣ Mise à jour des inscrits
    document.querySelectorAll(".update-inscrits").forEach(input => {
        input.addEventListener("change", function () {
            const formationId = input.dataset.formationId;
            const field = input.dataset.field;
            const oldValue = input.defaultValue;
            const newValue = parseInt(input.value, 10);

            if (isNaN(newValue)) {
                showToast("❌ Valeur invalide", "danger");
                input.value = oldValue;
                return;
            }

            const confirmMessage = `Modifier "${field}" de ${oldValue} à ${newValue} ?`;
            if (!confirm(confirmMessage)) {
                input.value = oldValue;
                return;
            }

            input.disabled = true;

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
                if (data.success) {
                    showToast("✅ Mise à jour réussie !");
                    input.defaultValue = newValue;

                    // ✅ Animation de surbrillance verte
                    input.classList.add("bg-success", "text-white");
                    setTimeout(() => {
                        input.classList.remove("bg-success", "text-white");
                    }, 1500);

                    // ✅ Met à jour dynamiquement les stats liées dans la ligne
                    const row = input.closest("tr");

                    const prevus_crif = parseInt(row.querySelector('[data-field="prevus_crif"]').value) || 0;
                    const prevus_mp = parseInt(row.querySelector('[data-field="prevus_mp"]').value) || 0;
                    const inscrits_crif = parseInt(row.querySelector('[data-field="inscrits_crif"]').value) || 0;
                    const inscrits_mp = parseInt(row.querySelector('[data-field="inscrits_mp"]').value) || 0;
                    const candidats = parseInt(row.querySelector('[data-field="nombre_candidats"]').value) || 0;

                    const places_restantes_crif = Math.max(prevus_crif - inscrits_crif, 0);
                    const places_restantes_mp = Math.max(prevus_mp - inscrits_mp, 0);

                    const total_prevus = prevus_crif + prevus_mp;
                    const total_inscrits = inscrits_crif + inscrits_mp;

                    const taux_saturation = total_prevus > 0 ? (100 * total_inscrits / total_prevus) : 0;
                    const taux_transformation = candidats > 0 ? (100 * total_inscrits / candidats) : 0;

                    row.querySelector("td:nth-child(11)").innerHTML = `
                        <span class="badge bg-secondary px-2">CRIF: ${places_restantes_crif}</span>
                        <span class="badge bg-success px-2">MP: ${places_restantes_mp}</span>
                    `;

                    row.querySelector("td:nth-child(12)").innerHTML = `
                        <span class="fw-bold text-purple">${taux_transformation.toFixed(0)}%</span>
                    `;

                    const progressTd = row.querySelector("td:nth-child(13)");
                    const progressColor = 
                        taux_saturation >= 100 ? "bg-success" :
                        taux_saturation >= 80 ? "bg-primary" :
                        taux_saturation >= 50 ? "bg-warning" :
                        "bg-danger";

                    progressTd.innerHTML = `
                        <div class="progress" style="height: 8px;">
                            <div class="progress-bar ${progressColor}" role="progressbar" style="width: ${taux_saturation}%"></div>
                        </div>
                        <span class="fw-bold d-block mt-1">${taux_saturation.toFixed(0)}%</span>
                    `;
                } else {
                    showToast("❌ " + data.error, "danger");
                    input.value = oldValue;
                }
            })
            .catch(error => {
                console.error("❌ Erreur AJAX :", error);
                showToast("Erreur lors de la requête", "danger");
                input.value = oldValue;
            })
            .finally(() => {
                input.disabled = false;
            });
        });
    });

    // ✅ 2️⃣ Affichage/Masquage des colonnes avec mémorisation
    const toggleButton = document.getElementById("toggleColumns");
    if (toggleButton) {
        toggleButton.addEventListener("click", function () {
            const table = document.querySelector(".formation-table");
            if (!table) return;

            const columnsToToggle = [6, 7, 8, 9];

            let hiddenColumns = JSON.parse(localStorage.getItem("hiddenColumns")) || [];

            columnsToToggle.forEach(colIndex => {
                const cells = table.querySelectorAll(`thead th:nth-child(${colIndex + 1}), tbody td:nth-child(${colIndex + 1})`);
                cells.forEach(cell => cell.classList.toggle("d-none"));

                if (hiddenColumns.includes(colIndex)) {
                    hiddenColumns = hiddenColumns.filter(c => c !== colIndex);
                } else {
                    hiddenColumns.push(colIndex);
                }
            });

            localStorage.setItem("hiddenColumns", JSON.stringify(hiddenColumns));
        });

        // ✅ 3️⃣ Appliquer l'état des colonnes masquées au chargement
        const hiddenColumns = JSON.parse(localStorage.getItem("hiddenColumns")) || [];
        hiddenColumns.forEach(colIndex => {
            document.querySelectorAll(`thead th:nth-child(${colIndex + 1}), tbody td:nth-child(${colIndex + 1})`)
                .forEach(cell => cell.classList.add("d-none"));
        });
    }
});

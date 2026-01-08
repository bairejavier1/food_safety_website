const form = document.getElementById("serviceForm");
const status = document.getElementById("status");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        phone: document.getElementById("phone").value
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/request-service", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        status.textContent = result.message;
        status.style.color = "green";
    } catch (error) {
        status.textContent = "Error sending request.";
        status.style.color = "red";
    }
});

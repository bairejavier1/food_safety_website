const form = document.getElementById("service-request-form");
const modal = document.getElementById("success-modal");
const closeModalBtn = document.getElementById("close-modal-btn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const message = document.getElementById("message").value.trim();

  try {
    const response = await fetch("http://127.0.0.1:8000/request-service", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        phone,
        message: message || null
      })
    });

    if (!response.ok) {
      throw new Error("Failed to submit request");
    }

    // Clear form
    form.reset();

    // Show modal
    modal.classList.add("active");

  } catch (err) {
    console.error("Error submitting request:", err);
    alert("There was an issue submitting your request. Please try again.");
  }
});

// Close modal button
closeModalBtn.addEventListener("click", () => {
  modal.classList.remove("active");
});

// Close modal when clicking outside
modal.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.classList.remove("active");
  }
});

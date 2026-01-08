const form = document.getElementById("serviceForm");
const modal = document.getElementById("successModal");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const phone = document.getElementById("phone").value;

  await fetch("http://127.0.0.1:5000/request-service", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, phone })
  });

  form.reset();
  modal.style.display = "flex";

  setTimeout(() => {
    modal.style.display = "none";
  }, 4000);
});

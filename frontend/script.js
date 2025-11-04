function showSection(id) {
  document.querySelectorAll(".section").forEach(sec => sec.classList.remove("active"));
  document.getElementById(id).classList.add("active");
  window.scrollTo(0, 0);
}

function searchItems() {
  const query = document.getElementById("searchBar").value.toLowerCase();
  const items = document.querySelectorAll(".item-card");
  items.forEach(item => {
    const text = item.innerText.toLowerCase();
    item.style.display = text.includes(query) ? "block" : "none";
  });
}

document.getElementById("foundForm")?.addEventListener("submit", e => {
  e.preventDefault();
  alert("Item submitted! (Backend integration coming soon)");
  showSection("home");
});

document.getElementById("claimForm")?.addEventListener("submit", e => {
  e.preventDefault();
  alert("Claim submitted! (Backend integration coming soon)");
  showSection("home");
});

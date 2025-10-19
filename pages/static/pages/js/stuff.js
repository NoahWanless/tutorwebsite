  function toggleDropdown() {
    document.getElementById("dropdownMenu").classList.toggle("show");
  }

  // Optional: Close dropdown if clicked outside
  window.addEventListener("click", function(event) {
    const dropdown = document.querySelector(".dropdown");
    if (!dropdown.contains(event.target)) {
      document.getElementById("dropdownMenu").classList.remove("show");
    }
  });



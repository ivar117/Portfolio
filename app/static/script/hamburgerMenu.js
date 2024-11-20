function handleSideNavEscPress(event) {
    if (event.key == "Escape") {
        sideNav.style.width = "0";
        document.removeEventListener("keydown", handleSideNavEscPress);
        document.removeEventListener("click", handleClickOutsideSidenav);
    }
}

function handleClickOutsideSidenav(event) {
    if (!sideNav.contains(event.target)) {
        sideNav.style.width = "0";
        document.removeEventListener("keydown", handleSideNavEscPress);
        document.removeEventListener("click", handleClickOutsideSidenav);
    }
};

function openSideNav() {
    sideNav = document.getElementById("sidenav");
    sideNav.style.width = "250px";

    requestAnimationFrame(() => {
        document.addEventListener("click", handleClickOutsideSidenav);
        document.addEventListener("keydown", handleSideNavEscPress);
    });
}
      
function closeSideNav() {
    document.getElementById("sidenav").style.width = "0";
    document.removeEventListener("keydown", handleSideNavEscPress);
    document.removeEventListener("click", handleClickOutsideSidenav);
}

document.querySelectorAll("#side-navbar a").forEach(anchor =>
    anchor.addEventListener("click", closeSideNav)
);

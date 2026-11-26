const temaTersimpan = localStorage.getItem('tema');
const htmlElement = document.documentElement;
const btnToggleTheme = document.getElementById("themeIcon");

btnToggleTheme.addEventListener('click', klikTema);

if (temaTersimpan == 'dark') {
    htmlElement.setAttribute('data-bs-theme', 'dark');
    btnToggleTheme.classList.remove('fa-sun');
    btnToggleTheme.classList.add('fa-moon');
    localStorage.setItem('tema', 'dark');
} else {
    htmlElement.setAttribute('data-bs-theme', 'light');
    btnToggleTheme.classList.remove('fa-moon');
    btnToggleTheme.classList.add('fa-sun');
    localStorage.setItem('tema', 'light');
}

function klikTema() {
    const temaAktif = htmlElement.getAttribute('data-bs-theme');
    if (temaAktif == 'dark') {
        htmlElement.setAttribute('data-bs-theme', 'light');
        btnToggleTheme.classList.remove('fa-moon');
        btnToggleTheme.classList.add('fa-sun');
        localStorage.setItem('tema', 'light');
    } else {
        htmlElement.setAttribute('data-bs-theme', 'dark');
        btnToggleTheme.classList.remove('fa-sun');
        btnToggleTheme.classList.add('fa-moon');
        localStorage.setItem('tema', 'dark');
    }
}
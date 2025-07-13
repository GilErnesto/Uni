    //logos
const logo = document.getElementById('logo');
const logoP = document.getElementById('logoP');

// Função para ocultar os logos
function desaparece() {
    console.log('Função desaparece');
    if (logo) logo.hidden = true;
    if (logoP) logoP.hidden = true;
    }

// Função para mostrar os logos com base no tema
function aparece() {
    console.log('Função aparece');
    const theme = document.documentElement.getAttribute('data-bs-theme') || 'light';

    if (logo) logo.hidden = theme === 'dark';
    if (logoP) logoP.hidden = theme !== 'dark';
    }

const button = document.getElementById('tooglebutton');
function ativar() {
        if (logo.hidden === true && logoP.hidden === true) {
    aparece();
        } else {desaparece(); }
    }
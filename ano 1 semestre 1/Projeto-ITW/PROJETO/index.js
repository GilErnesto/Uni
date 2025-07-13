document.addEventListener("DOMContentLoaded", function () {
    const carouselElement = document.getElementById('olimpics');
    const carousel = new bootstrap.Carousel(carouselElement, {
        ride: false, // Desativa a rolagem automática
    });

    carouselElement.addEventListener('slid.bs.carousel', function (e) {
        e.preventDefault(); // Impede a rolagem da página
    });
});
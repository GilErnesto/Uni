// Defina a data final do countdown
const targetDate = new Date("July 14, 2028 00:00:00").getTime();

function updateCountdown() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    // Calcule os anos, meses, dias, horas, minutos e segundos
    const years = Math.floor(distance / (1000 * 60 * 60 * 24 * 365));
    const months = Math.floor((distance % (1000 * 60 * 60 * 24 * 365)) / (1000 * 60 * 60 * 24 * 30));
    const days = Math.floor((distance % (1000 * 60 * 60 * 24 * 30)) / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Exiba o resultado
    document.getElementById("years").innerText = years;
    document.getElementById("months").innerText = months;
    document.getElementById("days").innerText = days;
    document.getElementById("hours").innerText = hours;
    document.getElementById("minutes").innerText = minutes;
    document.getElementById("seconds").innerText = seconds;

    // Se o countdown terminar, exiba uma mensagem
    if (distance < 0) {
        clearInterval(countdownInterval);
        document.getElementById("timer").innerHTML = "<div class='text'>EXPIRED</div>";
    }
}

// Atualize o countdown a cada segundo
const countdownInterval = setInterval(updateCountdown, 1000);

// Lógica do carrinho de compras
let cartCount = 0;
let cartItems = [];

function addToCart(itemName, itemPrice) {
    cartCount++;
    cartItems.push({ name: itemName, price: itemPrice });
    document.getElementById("cart-count").innerText = cartCount;
    updateCartItems();
}

function updateCartItems() {
    const cartItemsElement = document.getElementById("cart-items");
    cartItemsElement.innerHTML = "";
    cartItems.forEach(item => {
        const itemElement = document.createElement("div");
        itemElement.className = "cart-item";
        itemElement.innerText = `${item.name} - €${item.price.toFixed(2)}`;
        cartItemsElement.appendChild(itemElement);
    });
}

function redirectToCart() {
    window.location.href = "shop-pos.html";
}
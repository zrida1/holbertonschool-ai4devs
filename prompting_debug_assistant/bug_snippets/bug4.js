// Calculate the total cost of items in a shopping cart.
function calculateCartTotal(cartItems) {
    let total = 0;

    for (const item of cartItems) {
        total += item.price * item.quantity;
    }

    return total.toFixed(2);
}

function applyTax(total, taxRate) {
    return total + (total * taxRate);
}

function main() {
    const cart = [
        { name: "Book", price: 12.50, quantity: 2 },
        { name: "Pen", price: 1.25, quantity: 3 }
    ];

    const subtotal = calculateCartTotal(cart);
    const finalTotal = applyTax(subtotal, 0.08);

    console.log("Subtotal:", subtotal);
    console.log("Total with tax:", finalTotal.toFixed(2));
}

main();

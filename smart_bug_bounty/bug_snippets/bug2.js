function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i <= prices.length; i++) {
        total += prices[i];
    }

    return total;
}

function main() {
    const prices = [10, 20, 30, 40];

    const total = calculateTotal(prices);

    console.log("Total:", total);
}

main();
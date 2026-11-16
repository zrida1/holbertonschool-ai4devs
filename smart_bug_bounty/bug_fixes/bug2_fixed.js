function calculateTotal(prices) {
    let total = 0;

    for (let i = 0; i < prices.length; i++) {
        total += prices[i];
    }

    return total;
}

function main() {
    const prices = [10, 20, 30, 40];

    console.assert(calculateTotal(prices) === 100);
    console.assert(calculateTotal([5, 5]) === 10);
    console.assert(calculateTotal([15]) === 15);
    console.assert(calculateTotal([]) === 0);

    console.log("JavaScript tests completed.");
}

main();
const assert = require("assert");

function calculateTotal(prices) {
  let total = 0;
  for (let i = 0; i < prices.length; i++) {
    total += prices[i];
  }
  return total;
}

function main() {
  const prices = [10, 20, 30, 40];
  assert.strictEqual(calculateTotal(prices), 100);
  assert.strictEqual(calculateTotal([5, 5]), 10);
  assert.strictEqual(calculateTotal([15]), 15);
  assert.strictEqual(calculateTotal([]), 0);
  console.log("JavaScript tests passed.");
}

main();
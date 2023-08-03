var maxProfit = function(prices) {
  let diff = 0;
  let cl = prices[0]; // current lowest
  let maxP = 0;


  for(const price of prices) {
      diff = price - cl;
      if (diff > maxP) {
      maxP = diff;
      continue;
    }

    if(price < cl) {
      cl = price;
    }

  }
  return maxP;
};
console.log(maxProfit([7,6,4,3,1]));
console.log(maxProfit([7,1,5,3,6,4]));
console.log(maxProfit([1,2, 3]));

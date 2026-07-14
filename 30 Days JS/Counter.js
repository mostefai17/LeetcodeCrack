/**
 * @param {number} n
 * @return {Function} counter
 */

 /*
 JavaScript provides convenient syntax that returns a value and then increments it. This allows us to avoid having to initially set a variable to n - 1.

 Implementation
  */
  
var createCounter = function(n) {
  return function() {
    return n++;      
  };
};

 
  const counter = createCounter(10)
  counter() // 10
  counter() // 11
  counter() // 12
 

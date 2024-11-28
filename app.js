//1 problem///////////

const arr = [1, 9, 0, 5];
Array.prototype.last = function () {
  if (this.length === 0) {
    return -1;
  } else {
    return this[this.length - 1];
  }
};  


////////////    2620       /////////////////
var createCounter = function (n) {
  return function () {
    return n++;
  };
};

const counter = createCounter(10);
//  console.log(counter());
//  console.log(counter());
//  console.log(counter());  



////////////         9    ////////////

var isPalindrome = function(x) {
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
       return false
       
   }
   let reversedHalf = 0;
   while (x > reversedHalf) {
       reversedHalf = reversedHalf * 10 + x % 10; 
       x = Math.floor(x / 10);

   }
   if(x === reversedHalf || x === Math.floor(reversedHalf / 10)){
       return true;
   }
}; 


// console.log(isPalindrome(121)); 
// console.log(isPalindrome(-121)); 
// console.log(isPalindrome(11)); 

////////////////////////////////////////  


console.log("hello, node");

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

var isPalindrome = function (x) {
  if (x < 0 || (x % 10 === 0 && x !== 0)) {
    return false;
  }
  let reversedHalf = 0;
  while (x > reversedHalf) {
    reversedHalf = reversedHalf * 10 + (x % 10);
    x = Math.floor(x / 10);
  }
  if (x === reversedHalf || x === Math.floor(reversedHalf / 10)) {
    return true;
  }
};

// console.log(isPalindrome(121));
// console.log(isPalindrome(-121));
// console.log(isPalindrome(11));

////////////////////////////////////////

// console.log("hello, node");

///////2621//////////

/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
  return new Promise((resolve) =>
    setTimeout(() => {
      console.log(millis);
    }, millis)
  );
}

// sleep(1000)
/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */

/////////////////////////////////////

let nums = [3, 2, 4];
let target = 6;
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        console.log(nums[i], nums[j]);
        return [i, j];
      }
    }
  }


  
};
// console.log(twoSum(nums, target)); 


/**import React from "react";
import ReactDom from "react-dom";
import "./styles.css";
function Cv() {
  return (
    <section>
      <hr />
      <h1>HASSAN HAYAT</h1>
      <hr />
      <h2 className="h2">Personal profile</h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero totam
        accusamus doloremque quidem quod atque delectus dolore alias amet ad
        officiis obcaecati et ducimus, voluptates nihil nulla placeat eligendi.
        Distinctio.
      </p>
      <hr />
      <h2 className="h2">Education</h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero totam
        accusamus doloremque quidem quod atque delectus dolore alias amet ad
        officiis obcaecati et ducimus, voluptates nihil nulla placeat eligendi.
        Distinctio.
      </p>
      <hr />
      <h2 className="h2">Work Experience</h2>
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Vero totam
        accusamus doloremque quidem quod atque delectus dolore alias amet ad
        officiis obcaecati et ducimus, voluptates nihil nulla placeat eligendi.
        Distinctio.
      </p>
      <hr />
      <h2 className="h2">CONTACT US</h2>
      <a href="tel:+923395001230">+923395001230</a>
      <br />
      <a href="mailto:hassanhayat0012@gmail.com">hassanhayat0012@gmail.com</a>
    </section>
  );
}
ReactDom.render(<Cv />, document.querySelector("#root"));
**/
//react project



var compose = function(functions) {
    
  return function(x) {
       for(let i = functions.length-1;i>=0;i--){
           x = functions[i]
       }
       return x;
   }
};
 const fn = compose([x => x + 1, x => 2 * x])
//  fn(4) // 9


console.log(fn(4));

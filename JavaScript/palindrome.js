// input from terminal
const readline = require('readline');

let rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Word: ', function (word) {
  if (isPalindrome(word)) {
    console.log(`${word} is a palindrome`);
  } else {
    console.log(`${word} is not a palindrome`);
  }

  rl.close();
  process.stdin.destroy();
});

/**
 * Checks whether a word is a palindrome
 * 
 * @param  {string} word The word to test
 * @return {boolean} Whether or not the word is a palindrome
 */
function isPalindrome(word) {
  word = word.toUpperCase();
  return word== word.split('').reverse().join('');
}

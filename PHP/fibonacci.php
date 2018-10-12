<?php
/**
 * Calculates the Fibonacci-number after a number of iterations
 * 
 * @param int $iterations the number of iterations
 * @return int the Fibonacci-number
 */
function fibonacci($iterations) {
  // 0 and 1 will return their own value
  if ($iterations <= 1) {
    return $iterations;
  }

  // add the previous 2 numbers
  return fibonacci($iterations - 1) + fibonacci($iterations  - 2);
}

/**
 * Prints the Fibonacci-number after a number of iterations
 * 
 * @param int $iterations the number of iterations
 */
function print_fibonacci($iterations) {
  for ($i = 0; $i < $iterations; $i++) {
    echo fibonacci($i).' ';
  }
}

$iterations = readline('Number of iterations: ');
$input_accepted = false;

if ($iterations > 33) {
  $continue = readline('This may take a while to compute, continue? [Y/N]: ');

  if (strtoupper($continue) == 'Y') {
    print_fibonacci($iterations);
  }
} else {
  print_fibonacci($iterations);
}
?>
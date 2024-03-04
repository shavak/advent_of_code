// Supporting crate for the solution to Advent of Code 2023 Day 1.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::str::Chars;
use std::collections::HashMap;

pub fn first_digit(char_iter: Chars, radix: u32) -> u32 {
    let mut ans = 0;
    for c in char_iter {
        if let Some(x) = c.to_digit(radix) {
            ans = x;
            break;
        }
    }
    ans
}

fn digit_check(w: &Vec<char>, j: usize) -> Option<u32> {
    let digits = HashMap::from([
        ("one", 1_u32),
        ("two", 2_u32),
        ("three", 3_u32),
        ("four", 4_u32),
        ("five", 5_u32),
        ("six", 6_u32),
        ("seven", 7_u32),
        ("eight", 8_u32),
        ("nine", 9_u32),
    ]);
    let c = w[j];
    match w[j] {
        '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' => c.to_digit(10),
        _ => {
            let mut ans: Option<u32> = None;
            for (word, d) in digits {
                let s: &str = &w.iter().skip(j).take(word.len()).collect::<String>()[..];
                if s == word {
                    ans = Some(d);
                    break;
                }
            }
            ans
        }
    }
}

pub fn calibration_value(w: &Vec<char>) -> u32 {
    let mut ans = 0;
    let n = w.len();
    for i in 0..n {
        if let Some(x) = digit_check(&w, i) {
            ans = 10 * x;
            break;
        }
    }
    for i in 0..n {
        if let Some(x) = digit_check(&w, n - i - 1) {
            ans += x;
            break;
        }
    }
    ans
}

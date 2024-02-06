// Advent of Code 2023 Problem 1 Part 1
// Author: Shavak Sinanan <shavak@gmail.com>

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::str::Chars;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn first_digit(char_iter: Chars, radix: u32) -> u32 {
    let mut ans = 0;
    for c in char_iter {
        if let Some(x) = c.to_digit(radix) {
            ans = x;
            break;
        }
    }
    ans
}

fn main() {
    let radix = 10_u32;
    let input_path_str = "./input.txt";
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path_str) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines.flatten() {
            acc += first_digit(line.chars(), radix) * radix
                + first_digit(line.chars().rev().collect::<String>().chars(), radix);
        }
    }
    println!("Sum of calibration values = {acc}");
}

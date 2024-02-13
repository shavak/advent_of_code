// Advent of Code 2023 Problem 1 Part 2
// Author: Shavak Sinanan <shavak@gmail.com>

use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
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

fn calibration_value(w: &Vec<char>) -> u32 {
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

fn main() {
    let input_path_str = "./input.txt";
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path_str) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines.flatten() {
            let w: Vec<char> = line.chars().collect();
            acc += calibration_value(&w);
        }
    }
    println!("Sum of calibration values = {acc}");
}

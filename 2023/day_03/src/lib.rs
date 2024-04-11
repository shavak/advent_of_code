// Supporting crate for the solution to Advent of Code 2023 Day 3.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::collections::HashMap;

fn is_symbol(c: char) -> bool {
    match c {
        '.' | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' => false,
        _ => true,
    }
}

pub fn part_number_sum(top: &Vec<char>, middle: &Vec<char>, bottom: &Vec<char>) -> u32 {
    let b: u32 = 10;
    let mut acc: u32 = 0;
    let mut y: u32 = 0;
    let mut reading_number: bool = false;
    let mut symbol_in_play: bool = false;
    let l: usize = top.len();
    let m: usize = middle.len();
    let n: usize = bottom.len();
    for j in 0..m {
        let c = middle[j];
        let mut symbol_above = false;
        if j < l {
            // Check for symbol above.
            symbol_above = is_symbol(top[j]);
        }
        let mut symbol_below = false;
        if j < n {
            // Check for symbol below.
            symbol_below = is_symbol(bottom[j]);
        }
        match c {
            '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' => {
                // This is a digit.
                // I am reading a number.
                reading_number = true;
                // Continue to build the prospective part number.
                y *= b;
                if let Some(x) = c.to_digit(b) {
                    y += x;
                }
                // Update the check that the part number is admissible.
                symbol_in_play = symbol_in_play || symbol_above || symbol_below
            }
            '.' => {
                // This is a nothing. But I don't do nothing.
                if reading_number {
                    // I was previously reading a number.
                    symbol_in_play = symbol_in_play || symbol_above || symbol_below;
                    if symbol_in_play {
                        acc += y;
                    }
                }
                symbol_in_play = symbol_above || symbol_below;
                // Reset everything.
                y = 0;
                reading_number = false;
            }
            _ => {
                // This a symbol.
                symbol_in_play = true;
                if reading_number {
                    // I was previously reading a number.
                    acc += y;
                }
                // Reset everything.
                reading_number = false;
                y = 0;
            }
        }
    }
    acc + if symbol_in_play { y } else { 0 }
}

pub fn star_coordinates(
    top: &Vec<char>,
    middle: &Vec<char>,
    bottom: &Vec<char>,
    i: i32,
    coords: &mut HashMap<(i32, i32), Vec<u32>>,
) {
    let b: u32 = 10;
    let mut reading_number: bool = false;
    let mut y: u32 = 0;
    let mut u: Vec<(i32, i32)> = Vec::new();
    let mut v: Vec<(i32, i32)> = Vec::new();
    let l: usize = top.len();
    let m: usize = middle.len();
    let n: usize = bottom.len();
    for j in 0..m {
        let c = middle[j];
        if j < l && top[j] == '*' {
            u.push((i - 1, j as i32));
        }
        if j < n && bottom[j] == '*' {
            u.push((i + 1, j as i32));
        }
        match c {
            '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' => {
                // This is a digit.
                // I am reading a number.
                reading_number = true;
                // Continue to build the prospective part number.
                y *= b;
                if let Some(x) = c.to_digit(b) {
                    y += x;
                }
            }
            _ => {
                if c == '*' {
                    u.push((i, j as i32));
                }
                if reading_number {
                    // I was previously reading a number.
                    // Add the coordinates and the number to the hash map.
                    for p in v.iter() {
                        coords.entry(*p).or_insert(Vec::new()).push(y);
                    }
                    for p in u.iter() {
                        coords.entry(*p).or_insert(Vec::new()).push(y);
                    }
                }
                // Reset everything.
                reading_number = false;
                y = 0;
                v.clear();
            }
        }
        v.append(&mut u);
    }
    if reading_number {
        // I was previously reading a number.
        // Add the coordinates and the number to the hash map.
        for p in v {
            coords.entry(p).or_insert(Vec::new()).push(y);
        }
        for p in u {
            coords.entry(p).or_insert(Vec::new()).push(y);
        }
    }
}

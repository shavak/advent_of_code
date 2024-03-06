// Solution to Advent of Code 2023 Day 1.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::path::*;
use aoc_utils::*;
use day_01::*;

fn part_a(input_path: &Path) {
    let radix = 10_u32;
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            acc += first_digit(line.chars(), radix) * radix
                + first_digit(line.chars().rev().collect::<String>().chars(), radix);
        }
    }
    println!("Part (a):\nSum of calibration values = {acc}\n");
}

fn part_b(input_path: &Path) {
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            let w: Vec<char> = line.chars().collect();
            acc += calibration_value(&w);
        }
    }
    println!("Part (b):\nSum of calibration values = {acc}\n");
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "input.txt";
    let input_filename_b = "input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

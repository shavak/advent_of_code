// Solution to Advent of Code 2023 Day 2.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::path::Path;
use std::collections::HashMap;
use aoc_utils::*;
use day_02::*;

fn part_a(input_path: &Path) {
    let content = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            let v: Vec<&str> = line.split(':').collect();
            if is_admissible_game(v[1].trim(), &content) {
                acc += game_number(v[0]);
            }
        }
    }
    println!("Part (a):\nSum of admissible Game IDs = {acc}\n");
}

fn part_b(input_path: &Path) {
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            let v: Vec<&str> = line.split(':').collect();
            acc += game_power(minimum_content(v[1].trim()));
        }
    }
    println!("Part (b):\nSum of game powers = {acc}\n");
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "input.txt";
    let input_filename_b = "input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

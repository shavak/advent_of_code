// Solution to Advent of Code 2023 Day 4.
// Author: Shavak Sinanan <shavak@gmail.com>

use::std::path::*;
use::std::collections::HashMap;
use aoc_utils::*;
use day_04::*;

fn part_a(input_path: &Path) {
    let mut acc: u32 = 0;
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            acc += card_points(&line);
        }
    }
    println!("Part (a):\nTotal number of points = {acc}\n");
}

fn part_b(input_path: &Path) {
    let mut k: u32 = 0;
    let mut card_copies: HashMap<u32, u32> = HashMap::new();
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            k += 1;
            update_card_count(&line, k, &mut card_copies);
        }
    }
    println!("Part (b):\nTotal number of cards = {}\n", card_copies.values().sum::<u32>());
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "input.txt";
    let input_filename_b = "input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

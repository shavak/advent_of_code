// Solution to Advent of Code 2023 Day 6.
// Author: Shavak Sinanan <shavak@gmail.com>

use::std::path::*;
use::std::collections::HashMap;
use day_06::*;

fn part_a(input_path: &Path) {
}

fn part_b(input_path: &Path) {
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "test_input.txt";
    let input_filename_b = "test_input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

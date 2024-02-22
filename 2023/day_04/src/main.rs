// Solution to Advent of Code 2023 Day 4.
// Author: Shavak Sinanan <shavak@gmail.com>

use::std::path::*;
use day_04::*;

fn part_a(input_path: &Path) {
    let mut acc: u32 = 0;
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            acc += card_points(line);
        }
    }
    println!("Part (a):\nTotal number of points = {acc}\n");
}

fn part_b(input_path: &Path) {
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
        }
    }
    let mut acc = 0;
    println!("Part (b):\n<text here> = {acc}\n");
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "input.txt";
    let input_filename_b = "test_input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

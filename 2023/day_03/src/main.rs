// Solution to Advent of Code 2023 Day 3.
// Author: Shavak Sinanan <shavak@gmail.com>

use::std::path::*;
use::std::collections::HashMap;
use aoc_utils::*;
use day_03::*;

fn part_a(input_path: &Path) {
    let mut top: Vec<char>;
    let mut middle: Vec<char> = Vec::new();
    let mut bottom: Vec<char> = Vec::new();
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            top = middle;
            middle = bottom;
            bottom = line.chars().collect();
            acc += part_number_sum(&top, &middle, &bottom);
        }
    }
    top = middle;
    middle = bottom;
    bottom = Vec::new();
    acc += part_number_sum(&top, &middle, &bottom);
    println!("Part (a):\nSum of part numbers = {acc}\n");
}

fn part_b(input_path: &Path) {
    let mut top: Vec<char>;
    let mut middle: Vec<char> = Vec::new();
    let mut bottom: Vec<char> = Vec::new();
    let mut k = -2;
    let mut coords: HashMap<(i32, i32), Vec<u32>> = HashMap::new();
    if let Ok(lines) = read_lines(input_path) {
        for line in lines.flatten() {
            k += 1;
            top = middle;
            middle = bottom;
            bottom = line.chars().collect();
            star_coordinates(&top, &middle, &bottom, k, &mut coords);
        }
    }
    k += 1;
    top = middle;
    middle = bottom;
    bottom = Vec::new();
    star_coordinates(&top, &middle, &bottom, k, &mut coords);
    let mut acc = 0;
    for (_, y) in coords {
        if y.len() == 2 {
            acc += y[0] * y[1];
        }
    }
    println!("Part (b):\nSum of gear ratios = {acc}\n");
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "input.txt";
    let input_filename_b = "input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

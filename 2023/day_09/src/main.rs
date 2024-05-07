// Solution to Advent of Code 2023 Day 9.
// Author: Shavak Sinanan <shavak@gmail.com>

use aoc_utils::*;
use day_09::*;
use std::path::Path;

fn extrapolated_value_sum(input_path: &Path, rev: bool) -> i64 {
    let mut ans = 0;
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        while let Some(line) = lines_f.next() {
            let mut v = split_whitespace_parse::<i64>(&line);
            if rev {
                v.reverse();
            }
            ans += extrapolate_from_history(&mut v);
        }
    }
    ans
}

fn part_a(input_path: &Path) {
    println!(
        "Part (a):\nSum of extrapolated values = {}\n",
        extrapolated_value_sum(input_path, false)
    );
}

fn part_b(input_path: &Path) {
    println!(
        "Part (b):\nSum of extrapolated values = {}\n",
        extrapolated_value_sum(input_path, true)
    );
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "input.txt";
    let input_filename_b = "input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

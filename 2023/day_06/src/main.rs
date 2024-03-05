// Solution to Advent of Code 2023 Day 6.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::path::Path;
use aoc_utils::*;
use day_06::*;

fn part_a(input_path: &Path) {
    let mut acc: u64 = 1u64;
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        let t: Vec<f64> = split_whitespace_parse::<f64>(&lines_f.next().unwrap());
        let d: Vec<f64> = split_whitespace_parse::<f64>(&lines_f.next().unwrap());
        let n = t.len();
        for i in 0..n {
            acc *= num_record_breaks(t[i], d[i]);
        }
    }
    println!("Part (a):\nProduct = {acc}\n");
}

fn part_b(input_path: &Path) {
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        let lnt = &lines_f.next().unwrap();
        let i: usize = lnt.find(":").unwrap();
        let t = lnt[i + 1..].split_whitespace().collect::<Vec<&str>>().join("").parse::<f64>().unwrap();
        let lnd = &lines_f.next().unwrap();
        let i: usize = lnd.find(":").unwrap();
        let d = lnd[i + 1..].split_whitespace().collect::<Vec<&str>>().join("").parse::<f64>().unwrap();
        println!("Part (b):\nNumber of ways to break record = {}", num_record_breaks(t, d))
    }
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "input.txt";
    let input_filename_b = "input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

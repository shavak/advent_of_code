// Supporting crate for the solution to Advent of Code 2023 Day 4.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn card_points(card: String) -> u32 {
    let v: Vec<&str> = card.split(" | ").collect();
    let u: Vec<&str> = v[0].split(": ").collect();
    let w: HashSet<u32> = HashSet::from_iter(
        u[1]
        .trim()
        .split_whitespace()
        .map(|s| s.trim().parse::<u32>().unwrap())
    );
    let y = v[1]
        .trim()
        .split_whitespace()
        .map(|s| s.trim().parse::<u32>().unwrap());
    let mut m = 0;
    for k in y {
        m += if w.contains(&k) { 1 } else { 0 };
    }
    if m == 0 { 0 } else { 2u32.pow(m - 1) }
}

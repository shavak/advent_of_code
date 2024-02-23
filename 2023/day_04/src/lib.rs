// Supporting crate for the solution to Advent of Code 2023 Day 4.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;
use std::collections::HashMap;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn num_matches(card: String) -> u32 {
    // Computes the number of matches on a single card.
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
    for j in y {
        m += if w.contains(&j) { 1 } else { 0 };
    }
    m
}

pub fn card_points(card: String) -> u32 {
    let m = num_matches(card);
    if m == 0 { 0 } else { 2u32.pow(m - 1) }
}

pub fn update_card_count(card: String, k: u32, card_copies: &mut HashMap<u32, u32>) {
    // Updates the count of each card.
    let h: &mut u32 = card_copies.entry(k).or_insert(0u32);
    *h += 1;
    let c: u32 = (*h).clone();
    let m = num_matches(card);
    let mut q: &mut u32;
    for i in 1..=m {
        q = card_copies.entry(k + i).or_insert(0u32);
        *q += c;
    }
}

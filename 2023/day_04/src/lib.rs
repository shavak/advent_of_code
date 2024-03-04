// Supporting crate for the solution to Advent of Code 2023 Day 4.
// Author: Shavak Sinanan <shavak@gmail.com>

use aoc_utils::*;
use std::collections::HashMap;
use std::collections::HashSet;

fn num_matches(card: &str) -> u32 {
    // Computes the number of matches on a single card.
    let i: usize = card.find(":").unwrap();
    let j: usize = card.find("|").unwrap();
    let w: HashSet<u32> = HashSet::from_iter(split_whitespace_parse(&card[i + 1..j - 1]));
    let mut m = 0;
    for k in split_whitespace_parse(&card[j + 1..]) {
        m += if w.contains(&k) { 1 } else { 0 };
    }
    m
}

pub fn card_points(card: &str) -> u32 {
    let m = num_matches(card);
    if m == 0 {
        0
    } else {
        1 << (m - 1)
    }
}

pub fn update_card_count(card: &str, k: u32, card_copies: &mut HashMap<u32, u32>) {
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

// Solution to Advent of Code 2023 Day 7.
// Author: Shavak Sinanan <shavak@gmail.com>

use aoc_utils::*;
use day_07::*;
use std::collections::HashMap;
use std::path::Path;
static WILD: char = 'J';

fn part_a(input_path: &Path) {
    let u = [
        '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A',
    ];
    let mut r: HashMap<char, u64> = HashMap::new();
    for i in 0..u.len() {
        r.insert(u[i], i as u64);
    }
    let mut acc: u32 = 0;
    let mut v: Vec<CamelCardHand> = Vec::new();
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        while let Some(line) = lines_f.next() {
            v.push(CamelCardHand::new(&line, &r, WILD));
        }
    }
    v.sort_by_key(|x| x.f);
    for i in 0..v.len() {
        acc += v[i].bid * ((i + 1) as u32);
    }
    println!("Part (a):\nTotal winnings = {acc}\n");
}

fn part_b(input_path: &Path) {
    let u = [
        'J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A',
    ];
    let mut r: HashMap<char, u64> = HashMap::new();
    for i in 0..u.len() {
        r.insert(u[i], i as u64);
    }
    let mut acc: u32 = 0;
    let mut v: Vec<CamelCardHand> = Vec::new();
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        while let Some(line) = lines_f.next() {
            v.push(CamelCardHand::new(&line, &r, WILD));
        }
    }
    v.sort_by_key(|x| x.g);
    for i in 0..v.len() {
        acc += v[i].bid * ((i + 1) as u32);
    }
    println!("Part (b):\nTotal winnings = {acc}\n");
}

fn main() {
    let input_root_dir = Path::new("input/");
    let input_filename_a = "input.txt";
    let input_filename_b = "input.txt";
    println!();
    part_a(input_root_dir.join(input_filename_a).as_path());
    part_b(input_root_dir.join(input_filename_b).as_path());
}

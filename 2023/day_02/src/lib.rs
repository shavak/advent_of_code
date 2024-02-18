// Supporting crate for the solution to Advent of Code 2023 Day 2.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn create_round(round_str: &str) -> HashMap<&str, u32>{
    let mut round: HashMap<&str, u32> = HashMap::new();
    let v: Vec<&str> = round_str.split(", ").collect();
    for colour_str in v.iter() {
        let w: Vec<&str> = colour_str.split(" ").collect();
        round.insert(w[1], w[0].parse::<u32>().unwrap());
    }
    round
}

fn is_admissible_round(round: HashMap<&str, u32>, content: &HashMap<&str, u32>) -> bool {
    let mut ans: bool = true;
    for (colour, x) in round {
        if let Some(c) = content.get(colour).cloned() {
            if x > c {
                ans = false;
            }
        }
    }
    ans
}

pub fn is_admissible_game(game_str: &str, content: &HashMap<&str, u32>) -> bool {
    let v: Vec<&str> = game_str.split("; ").collect();
    let mut ans: bool = true;
    for round_str in v.iter() {
        if !is_admissible_round(create_round(round_str.trim()), content) {
            ans = false;
            break;
        }
    }
    ans
}

pub fn game_number(heading: &str) -> u32 {
    let v: Vec<&str> = heading.split(" ").collect();
    v[1].parse::<u32>().unwrap_or(0)
}

pub fn minimum_content(game_str: &str) -> HashMap<&str, u32> {
    let v: Vec<&str> = game_str.split("; ").collect();
    let mut min_cubes: HashMap<&str, u32> = HashMap::new();
    for round_str in v.iter() {
        let round = create_round(round_str.trim());
        for (colour, x) in round {
            let y = min_cubes.entry(colour).or_insert(0);
            if *y < x {
                *y = x;
            }
        }
    }
    min_cubes
}

pub fn game_power(cube_map: HashMap<&str, u32>) -> u32 {
    let mut acc = 1;
    for (_, x) in cube_map {
        acc *= x;
    }
    acc
}

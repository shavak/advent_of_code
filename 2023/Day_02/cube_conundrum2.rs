// Advent of Code 2023 Problem 2 Part 2
// Author: Shavak Sinanan <shavak@gmail.com>

use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn create_round(round_str: &str) -> HashMap<&str, u32>{
    let mut round: HashMap<&str, u32> = HashMap::new();
    let v: Vec<&str> = round_str.split(", ").collect();
    for colour_str in v.iter() {
        let w: Vec<&str> = colour_str.split(" ").collect();
        round.insert(w[1], w[0].parse::<u32>().unwrap());
    }
    round
}

fn minimum_content(game_str: &str) -> HashMap<&str, u32> {
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

fn game_power(cube_map: HashMap<&str, u32>) -> u32 {
    let mut acc = 1;
    for (_, x) in cube_map {
        acc *= x;
    }
    acc
}

fn main() {
    let input_path_str = "./input.txt";
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path_str) {
        for line in lines.flatten() {
            let v: Vec<&str> = line.split(':').collect();
            acc += game_power(minimum_content(v[1].trim()));
        }
    }
    println!("Sum of game powers = {acc}");
}

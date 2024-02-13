// Advent of Code 2023 Problem 2 Part 1
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

fn is_admissible_round(round: HashMap<&str, u32>, content: &HashMap<&str, u32>) -> bool {
    let mut ans: bool = true;
    for (colour, x) in round {
        let c = content.get(colour).cloned().unwrap_or(0);
        if x > c {
            ans = false;
        }
    }
    ans
}

fn is_admissible_game(game_str: &str, content: &HashMap<&str, u32>) -> bool {
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

fn game_number(heading: &str) -> u32 {
    let v: Vec<&str> = heading.split(" ").collect();
    v[1].parse::<u32>().unwrap_or(0)
}

fn main() {
    let input_path_str = "./input.txt";
    let content = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);
    let mut acc = 0;
    if let Ok(lines) = read_lines(input_path_str) {
        for line in lines.flatten() {
            let v: Vec<&str> = line.split(':').collect();
            if is_admissible_game(v[1].trim(), &content) {
                acc += game_number(v[0]);
            }
        }
    }
    println!("Sum of admissible Game IDs = {acc}");
}

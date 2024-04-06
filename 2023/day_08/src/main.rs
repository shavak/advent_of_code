// Solution to Advent of Code 2023 Day 8.
// Author: Shavak Sinanan <shavak@gmail.com>

use aoc_utils::*;
use day_08::*;
use std::collections::HashMap;
use std::collections::HashSet;
use std::path::Path;

fn part_a(input_path: &Path) {
    let mut inst: Vec<char> = Vec::<char>::new();
    let mut graph: HashMap<String, (String, String)> = HashMap::new();
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        inst = lines_f.next().unwrap().chars().collect();
        lines_f.next();
        while let Some(line) = lines_f.next() {
            let s: Vec<&str> = line.split(" = ").map(|x| x.trim()).collect();
            let q: Vec<&str> = s[1][1..s[1].len() - 1]
                .split(", ")
                .map(|x| x.trim())
                .collect();
            graph.insert(s[0].to_string(), (q[0].to_string(), q[1].to_string()));
        }
    }
    let source_id = "AAA";
    let dest_id = "ZZZ";
    println!(
        "Part (a):\nNumber of steps = {}\n",
        num_human_steps(&source_id, &dest_id, graph, &inst)
    );
}

fn part_b(input_path: &Path) {
    let mut inst: Vec<char> = Vec::<char>::new();
    let mut graph: HashMap<String, (String, String)> = HashMap::new();
    let source_suffix = "A";
    let dest_suffix = "Z";
    let mut source_nodes: Vec<String> = Vec::new();
    let mut dest_nodes: HashSet<String> = HashSet::new();
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        inst = lines_f.next().unwrap().chars().collect();
        lines_f.next();
        while let Some(line) = lines_f.next() {
            let s: Vec<&str> = line.split(" = ").map(|x| x.trim()).collect();
            let q: Vec<&str> = s[1][1..s[1].len() - 1]
                .split(", ")
                .map(|x| x.trim())
                .collect();
            graph.insert(s[0].to_string(), (q[0].to_string(), q[1].to_string()));
            if s[0].ends_with(&source_suffix) {
                source_nodes.push(s[0].to_string());
            }
            if s[0].ends_with(&dest_suffix) {
                dest_nodes.insert(s[0].to_string());
            }
            if q[0].ends_with(&dest_suffix) {
                dest_nodes.insert(q[0].to_string());
            }
            if q[1].ends_with(&dest_suffix) {
                dest_nodes.insert(q[1].to_string());
            }
        }
    }
    // for (k, (u, v)) in &graph {
    //     println!("{} = {}, {}", k, u, v);
    // }
    println!(
        "Part (b):\nNumber of steps = {}\n",
        num_ghost_steps(source_nodes, dest_nodes, graph, &inst)
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

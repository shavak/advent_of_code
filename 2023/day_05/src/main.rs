// Solution to Advent of Code 2023 Day 4.
// Author: Shavak Sinanan <shavak@gmail.com>

use ::std::path::*;
use day_05::*;

fn part_a(input_path: &Path) {
    let mut v: Vec<u64> = Vec::<u64>::new();
    let mut rm: RangeMap = RangeMap::new();
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        v = lines_f
            .next()
            .unwrap_or(String::from("seeds: "))
            .split(": ")
            .collect::<Vec<&str>>()[1]
            .trim()
            .split_whitespace()
            .map(|x| x.trim().parse::<u64>().unwrap())
            .collect();
        while let Some(line) = lines_f.next() {
            if line == "" {
                v = v.iter().map(|x| rm.image(*x)).collect();
                rm.clear();
                // If needed, I can parse the string in the next line to extract the source
                // and destination identifiers.
                lines_f.next();
            } else {
                let u: Vec<u64> = line
                    .trim()
                    .split_whitespace()
                    .map(|x| x.trim().parse::<u64>().unwrap())
                    .collect();
                rm.add_range(u[0], u[1], u[2] as usize)
            }
        }
    }
    v = v.iter().map(|x| rm.image(*x)).collect();
    println!(
        "Part (a):\nLowest location number = {}\n",
        v.iter().min().unwrap()
    );
}

fn part_b(input_path: &Path) {
    let mut v: Vec<(u64, u64)> = Vec::<(u64, u64)>::new();
    let mut rm: RangeMap = RangeMap::new();
    if let Ok(lines) = read_lines(input_path) {
        let mut lines_f = lines.flatten();
        let h: Vec<u64> = lines_f
            .next()
            .unwrap_or(String::from("seeds: "))
            .split(": ")
            .collect::<Vec<&str>>()[1]
            .trim()
            .split_whitespace()
            .map(|x| x.trim().parse::<u64>().unwrap())
            .collect();
        let m = h.len();
        let mut i = 0_usize;
        while i < m {
            v.push((h[i], h[i + 1]));
            i += 2;
        }
        while let Some(line) = lines_f.next() {
            if line == "" {
                v = v.iter().flat_map(|&(q, k)| rm.range_image(q, k)).collect();
                rm.clear();
                // If needed, I can parse the string in the next line to extract the source
                // and destination identifiers.
                lines_f.next();
            } else {
                let w: Vec<u64> = line
                    .trim()
                    .split_whitespace()
                    .map(|x| x.trim().parse::<u64>().unwrap())
                    .collect();
                rm.add_range(w[0], w[1], w[2] as usize)
            }
        }
    }
    v = v.iter().flat_map(|&(q, k)| rm.range_image(q, k)).collect();
    println!(
        "Part (b):\nLowest location number = {}\n",
        v.iter().map(|&(r, _)| r).min().unwrap()
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

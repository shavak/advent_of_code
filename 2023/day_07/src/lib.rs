// Supporting crate for the solution to Advent of Code 2023 Day 7.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::cmp::*;
use std::collections::HashMap;

#[derive(Debug)]
pub struct CamelCardHand {
    pub hand: String,
    pub bid: u32,
    pub f: u64,
    pub g: u64,
}

impl CamelCardHand {
    pub fn new(line: &str, r: &HashMap<char, u64>, wild: char) -> Self {
        let k = line.find(" ").unwrap();
        let m = r.len();
        let b = (max(m, k) + 1) as u64;
        let mut h = HashMap::new();
        let mut f = 0;
        let mut q = 1;
        for c in line.chars() {
            if c.is_whitespace() {
                break;
            }
            f *= b;
            f += r.get(&c).unwrap();
            h.entry(c).and_modify(|x| *x *= b).or_insert(1);
            q *= b;
        }
        let mut g = f;
        let mut e = wild;
        let mut y = 0;
        for (&a, &w) in &h {
            f += q * w;
            if w > y && a != wild {
                y = w;
                e = a;
            }
        }
        if e != wild { 
            let d = h.remove(&wild).unwrap_or(0) * b;
            h.entry(e)
                .and_modify(|x| *x *= if d > 0 { d } else { 1 });
        }
        for (_, w) in h {
            g += q * w;
        }
        Self {
            hand: String::from(&line[..k]),
            bid: line[k..].trim().parse::<u32>().unwrap(),
            f: f,
            g: g,
        }
    }
}

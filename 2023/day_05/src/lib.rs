// Supporting crate for the solution to Advent of Code 2023 Day 5.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::cmp::*;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

#[derive(Debug)]
pub struct RangeMap {
    a: Vec<u64>,
    g: HashMap<u64, (u64, usize)>, 
}

impl RangeMap {

    pub fn new() -> Self {
        Self {
            a: Vec::<u64>::new(),
            g: HashMap::<u64, (u64, usize)>::new(),
        }
    }

    pub fn clear(&mut self) {
        self.a.clear();
        self.g.clear();
    }

    pub fn add_range(&mut self, y: u64, x: u64, l: usize) {
        if let Err(i) = self.a.binary_search(&x) {
            self.a.insert(i, x)
        }
        self.g.insert(x, (y, l));
    }

    pub fn image(&self, q: u64) -> u64 {
        match self.a.binary_search(&q) {
            Ok(_) => {
                let &(r, _) = self.g.get(&q).unwrap();
                r
            }
            Err(i) => {
                if i == 0 {
                    // Straight-through map.
                    q
                }
                else {
                    // Check the left side of the range.
                    let t = self.a[i - 1];
                    let d = q - t;
                    let &(w, l) = self.g.get(&t).unwrap();
                    if d < (l as u64) {
                        // Hit!
                        w + d
                    }
                    else {
                        // Miss! It's a straight-through map again.
                        q
                    }
                }
            }
        }
    }

    pub fn range_image(&self, q: u64, k: u64) -> Vec<(u64, u64)> {
        let mut v: Vec<(u64, u64)> = Vec::new();
        let n = self.a.len();
        if n == 0 {
            v.push((q, k));
            return v;
        }
        let mut r = q;
        let mut j = k;
        let mut i = self.a.partition_point(|&x| x < q);
        let mut s;
        let mut d;
        if i == 0 {
            s = self.a[0];
            d = min(s - r, j);
            if d > 0 {
                v.push((r, d));
                r += d;
                j -= d;
            }
        }
        else {
            s = self.a[i - 1];
            let &(w, l) = self.g.get(&s).unwrap();
            let x = s + (l as u64);
            if x > r {
                d = min(x - r, j);
                if d > 0 {
                    v.push((w + r - s, d));
                    r += d;
                    j -= d;
                }
            }
        }
        while i < n {
            if j == 0 {
                // No more mapping to be done.
                break;
            }
            s = self.a[i];
            d = min(s - r, j);
            if d > 0 {
                v.push((r, d));
                r += d;
                j -= d;
            }
            if j > 0 {
                let &(w, l) = self.g.get(&s).unwrap();
                d = min(l as u64, j);
                v.push((w, d));
                r += d;
                j -= d;
            }
            i += 1;
        }
        if j > 0 {
            v.push((r, j));
        }
        v
    }

}

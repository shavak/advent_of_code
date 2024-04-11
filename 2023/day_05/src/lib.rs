// Supporting crate for the solution to Advent of Code 2023 Day 5.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::cmp::*;
use std::collections::BTreeMap;

#[derive(Debug)]
pub struct RangeMap {
    g: BTreeMap<u64, (u64, usize)>,
}

impl RangeMap {
    pub fn new() -> Self {
        Self {
            g: BTreeMap::<u64, (u64, usize)>::new(),
        }
    }

    pub fn clear(&mut self) {
        self.g.clear();
    }

    pub fn add_range(&mut self, y: u64, x: u64, l: usize) {
        self.g.insert(x, (y, l));
    }

    pub fn image(&self, q: u64) -> u64 {
        match self.g.range(..=q).next_back() {
            Some((x, (y, l))) => {
                let d = q - x;
                if d < (*l as u64) {
                    // Lies within a map range.
                    y + d
                } else {
                    // Straight-through map.
                    q
                }
            }
            None => {
                // Straight-through map.
                q
            }
        }
    }

    pub fn range_image(&self, q: u64, k: u64) -> Vec<(u64, u64)> {
        let mut v: Vec<(u64, u64)> = Vec::new();
        let mut r = q;
        let mut j = k;
        let mut d;
        let mut ran = self.g.range(..q);
        if let Some((x, (y, l))) = ran.next_back() {
            let w = x + (*l as u64);
            if w > r {
                d = min(w - r, j);
                if d > 0 {
                    v.push((y + r - x, d));
                    r += d;
                    j -= d;
                }
            }
        }
        ran = self.g.range(r..q + k);
        while let Some((x, (y, l))) = ran.next() {
            if j == 0 {
                // No more mapping to be done.
                break;
            }
            d = min(x - r, j);
            if d > 0 {
                v.push((r, d));
                r += d;
                j -= d;
            }
            if j > 0 {
                d = min(*l as u64, j);
                v.push((*y, d));
                r += d;
                j -= d;
            }
        }
        if j > 0 {
            // Smush the leftovers in.
            v.push((r, j));
        }
        v
    }
}

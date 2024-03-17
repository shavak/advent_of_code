// Supporting crate for the solution to Advent of Code 2023 Day 6.
// Author: Shavak Sinanan <shavak@gmail.com>

pub fn num_record_breaks(t: f64, d: f64) -> u64 {
    let p = 0.5 * t;
    let q = (p * p - d).sqrt() - 1.0;
    ((p + q).ceil() - (p - q).floor()) as u64 + 1
}

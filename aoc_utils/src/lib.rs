// Supporting library crate for Advent of Code.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::str::FromStr;

pub fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn split_parse<T: FromStr>(mixed_str: &str, sep: &str) -> Vec<T> {
    mixed_str
        .trim()
        .split(sep)
        .map(|s| s.trim().parse::<T>())
        .flatten()
        .collect()
}

pub fn split_whitespace_parse<T: FromStr>(mixed_str: &str) -> Vec<T> {
    mixed_str
        .trim()
        .split_whitespace()
        .map(|s| s.trim().parse::<T>())
        .flatten()
        .collect()
}

#[cfg(test)]
mod tests {

    #[test]
    fn read_lines_test() {
        assert_eq!(0, 0);
    }
}

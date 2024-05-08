// Supporting crate for the solution to Advent of Code 2023 Day 9.
// Author: Shavak Sinanan <shavak@gmail.com>

pub fn extrapolate_from_history(a: &mut Vec<i64>) -> i64 {
    let mut n = a.len();
    if n == 0 {
        return 0_i64;
    }
    n -= 1;
    let mut acc = a[n];
    let mut all_zeros;
    loop {
        all_zeros = true;
        for j in 0..n {
            let d = a[j + 1] - a[j];
            all_zeros &= d == 0;
            a[j] = d;
        }
        if all_zeros || n == 0 {
            break acc;
        }
        n -= 1;
        acc += a[n];
    }
}

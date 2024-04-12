// Supporting crate for the solution to Advent of Code 2023 Day 8.
// Author: Shavak Sinanan <shavak@gmail.com>

use num::integer;
use std::cmp;
use std::collections::HashMap;
use std::collections::HashSet;

pub fn num_human_steps(
    source: &str,
    dest: &str,
    graph: HashMap<String, (String, String)>,
    inst: &Vec<char>,
) -> u64 {
    let n = inst.len();
    let mut j = 0_usize;
    let mut x = source;
    loop {
        let (l, r) = graph.get(x).unwrap();
        x = if inst[j % n] == 'L' { l } else { r };
        j += 1;
        if x == dest {
            break j as u64;
        }
    }
}

fn period(
    x: &str,
    graph: &HashMap<String, (String, String)>,
    dest_nodes: &HashSet<String>,
    inst: &Vec<char>,
) -> Vec<(u64, bool, u64)> {
    let n = inst.len();
    let mut j = 0_usize;
    let mut cyc: HashMap<(&str, usize), usize> = HashMap::new();
    let (mut y, mut i) = (x, 0_usize);
    let mut u: Vec<u64> = Vec::new();
    let q;
    loop {
        if let Some(&k) = cyc.get(&(y, i)) {
            q = k as u64;
            break;
        }
        if dest_nodes.contains(y) {
            u.push(j as u64);
        }
        cyc.insert((y, i), j);
        let (l, r) = graph.get(y).unwrap();
        y = if inst[i] == 'L' { l } else { r };
        i = (i + 1) % n;
        j += 1;
    }
    let mut a: Vec<(u64, bool, u64)> = Vec::new();
    let p = j as u64 - q;
    for k in u {
        a.push((k, k >= q, p));
    }
    a
}

fn simple_modular(r: u64, p: u64, t: u64) -> Option<u64> {
    if r > t || (r % p != t % p) {
        None
    } else {
        Some(t)
    }
}

fn chinese_remainder(r: u64, u: u64, s: u64, v: u64) -> Option<(u64, u64)> {
    let d = integer::gcd(u, v);
    if r % d != s % d {
        return None;
    }
    let l = integer::lcm(u, v);
    let w = r % u;
    let mut k = s;
    loop {
        if k % u == w {
            break;
        }
        k += v;
    }
    if k > r {
        Some((k, l))
    } else {
        Some((r, l))
    }
}

fn sync(a: &Vec<(u64, bool, u64)>, b: &Vec<(u64, bool, u64)>) -> (Vec<(u64, bool, u64)>, u64) {
    let mut c: Vec<(u64, bool, u64)> = Vec::new();
    let mut m = u64::MAX;
    for &(j, adv_a, p) in a {
        for &(k, adv_b, q) in b {
            if !(adv_a || adv_b) && j == k {
                m = cmp::min(m, j);
                c.push((j, false, 0));
            } else if !adv_a && adv_b {
                if let Some(e) = simple_modular(k, q, j) {
                    m = cmp::min(m, e);
                    c.push((e, false, 0));
                }
            } else if adv_a && !adv_b {
                if let Some(e) = simple_modular(j, p, k) {
                    m = cmp::min(m, e);
                    c.push((e, false, 0));
                }
            } else if adv_a && adv_b {
                if let Some((f, l)) = chinese_remainder(j, p, k, q) {
                    m = cmp::min(m, f);
                    c.push((f, true, l));
                }
            }
        }
    }
    (c, m)
}

pub fn num_ghost_steps(
    source_nodes: Vec<String>,
    dest_nodes: HashSet<String>,
    graph: HashMap<String, (String, String)>,
    inst: &Vec<char>,
) -> u64 {
    let mut a = vec![(0_u64, true, 1_u64)];
    let mut ans = u64::MAX;
    for x in &source_nodes {
        let b = period(&x, &graph, &dest_nodes, inst);
        (a, ans) = sync(&a, &b);
    }
    ans
}

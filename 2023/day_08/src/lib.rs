// Supporting crate for the solution to Advent of Code 2023 Day 8.
// Author: Shavak Sinanan <shavak@gmail.com>

use std::collections::HashSet;
use std::collections::HashMap;
use std::cmp;
use num::integer;

pub fn num_human_steps(source: &str, dest: &str, graph: HashMap<String, (String, String)>, inst: &Vec<char>) -> u64 {
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

fn period(x: &str, graph: &HashMap<String, (String, String)>, dest_nodes: &HashSet<String>, inst: &Vec<char>) -> (Vec<(u64, bool, u64)>, u64) {
    let  n = inst.len();
    let mut j = 0_usize;
    let mut cyc: HashMap<(&str, usize), usize> = HashMap::new();
    let (mut y, mut i) = (x, 0_usize);
    let mut v: Vec<(&str, usize)> = Vec::new();
    let mut u: Vec<u64> = Vec::new();
    let q;
    loop {
        if let Some(&k) = cyc.get(&(y, i)) {
            q = k as u64;
            break;
        }
        v.push((y, i));
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
    let mut m: u64 = u64::MAX;
    let p = j as u64 - q;
    for k in u {
        m = cmp::min(m, k);
        a.push((k, k >= q, p));
    }
    (a, m)
}

fn simple_modular(r: u64, p: u64, t: u64) -> Option<u64> {
    if r > t || (r % p != t % p) {
        None
    }
    else {
        Some(t)
    }
}

fn chinese_remainder(r: u64, p: u64, s: u64, q: u64) -> Option<(u64, u64)> {
    let d = integer::gcd(p, q);
    if r % d != s % d {
        return None;
    }
    let l = integer::lcm(p, q);
    let w = r % p;
    let mut k = s;
    loop {
        if k % p == w {
            break;
        }
        k += q;
    }
    if k > r { Some((k, l)) } else {Some((r, l))}
}

fn sync(a: &Vec<(u64, bool, u64)>, b: &Vec<(u64, bool, u64)>) -> (Vec<(u64, bool, u64)>, u64) {
    let mut c: Vec<(u64, bool, u64)> = Vec::new();
    let mut m = u64::MAX;
    for &(j, adv_a, p) in a {
        for &(k, adv_b, q) in b {
            if !(adv_a || adv_b) && j == k {
                m = cmp::min(m, j);
                c.push((j, false, 0));
            }
            else if !adv_a && adv_b {
                if let Some(e) = simple_modular(k, q, j) {
                    m = cmp::min(m, e);
                    c.push((e, false, 0));
                }
            }
            else if adv_a && !adv_b {
                if let Some(e) = simple_modular(j, p, k) {
                    m = cmp::min(m, e);
                    c.push((e, false, 0));
                }
            }
            else if adv_a && adv_b {
                if let Some((f, l)) = chinese_remainder(j, p, k, q) {
                    m = cmp::min(m, f);
                    c.push((f, true, l));
                }
            }
        }
    }
    (c, m)
}

pub fn num_ghost_steps(source_nodes: Vec<String>, dest_nodes: HashSet<String>, graph: HashMap<String, (String, String)>, inst: &Vec<char>) -> u64 {
    let mut a = vec![(0_u64, true, 1_u64)];
    let mut ans = u64::MAX;
    for x in &source_nodes {
        for (j, adv, m) in &a {
            println!("{j}, {adv}, {m}");
        }
        let (b, _) = period(&x, &graph, &dest_nodes, inst);
        let (c, m) = sync(&a, &b);
        a = c;
        ans = m;
    }
    ans
}

/*
    'g: loop {
        if node_heap.is_empty() {
            break u64::MAX;
        }
        let mut term_check: HashMap<u64, u32> = HashMap::new();
        for rev_tup in node_heap.iter() {
            let (j, _, _) = rev_tup.0;
            let f = *term_check.entry(j).and_modify(|y| *y += 1).or_insert(1);
            if f == e {
                break 'g j;
            }
        }
        let (j, adv, x) = node_heap.pop().unwrap().0;
        if adv {
            node_heap.push(Reverse((j + h.get(&x as &str).unwrap(), adv, x)));
        }
    }
fn condense_graph(graph: &HashMap<String, (String, String)>, inst: &Vec<char>, n: usize, k: usize) -> HashMap<String, String> {
    let mut h: HashMap<String, String> = HashMap::new();
    for (x, _) in graph {
        let mut y = x;
        for j in k..n + k {
            let (l, r) = graph.get(y).unwrap();
            y = if inst[j % n] == 'L' { l } else { r };
        }
        h.insert(x.to_string(), y.to_string());
    }
    h
}

fn num_condensed_steps(h: &HashMap<String, String>, s: &str, dest_nodes: &HashSet<String>) -> Option<(u64, String)> {
    let mut j = 0_u64;
    let mut y = s;
    let mut cyc: HashSet<String> = HashSet::new();
    loop {
        y = h.get(y).unwrap();
        j += 1;
        if dest_nodes.contains(y) {
            break Some((j, y.to_string()));
        }
        if cyc.contains(y) {
            break None;
        }
        cyc.insert(y.to_string());
    }
}

fn destination_touchpoints(h: &HashMap<String, String>, x: &str, dest_nodes: &HashSet<String>) -> (Vec<(u64, bool)>, u64) {
    let mut j = 0_usize;
    let mut cyc: HashMap<&str, usize> = HashMap::new();
    let mut y = x;
    let mut v: Vec<&str> = Vec::new();
    let mut u: Vec<usize> = Vec::new();
    let k;
    loop {
        if let Some(i) = cyc.get(y) {
            k = *i;
            break;
        }
        v.push(y);
        if dest_nodes.contains(y) {
            u.push(j);
        }
        cyc.insert(y, j);
        y = h.get(y).unwrap();
        j += 1;
    }
    let mut b: Vec<(u64, bool)> = Vec::new();
    for i in u {
        b.push((i as u64, i >= k));
    }
    (b, (j - k) as u64)
}

fn ghost_helper(source_nodes: &Vec<String>, dest_nodes: &HashSet<String>, graph: &HashMap<String, (String, String)>, inst: &Vec<char>, n: usize, k: usize) -> Option<u64> {
    let h = condense_graph(&graph, inst, n, k);
    let e = source_nodes.len() as u32;
    let mut node_heap = BinaryHeap::new();
    let mut l = 1;
    let mut a_max = 0;
    let mut period: HashMap<&str, u64> = HashMap::new();
    for x in source_nodes {
        let (v, m) = destination_touchpoints(&h, x, dest_nodes);
        period.insert(x, m);
        l = integer::lcm(l, m);
        println!();
        println!("{x}, {m}");
        for (j, adv) in v {
            node_heap.push(Reverse((j, adv, x)));
            a_max = cmp::max(a_max, j);
            println!("{j}, {adv}, {x}");
        }
    }
    a_max += l;
    println!("\na_max = {a_max}\n");
    'g: loop {
        if node_heap.is_empty() {
            break None;
        }
        let mut term_check: HashMap<u64, u32> = HashMap::new();
        for rev_tup in node_heap.iter() {
            let (j, _, _) = rev_tup.0;
            let f = *term_check.entry(j).and_modify(|y| *y += 1).or_insert(1);
            if f == e {
                break 'g Some(j);
            }
        }
        let (j, adv, x) = node_heap.pop().unwrap().0;
        if j > a_max {
            break None;
        }
        if adv {
            node_heap.push(Reverse((j + period.get(&x as &str).unwrap(), adv, x)));
        }
    }
    /*
    let mut node_heap = BinaryHeap::new();
    for s in source_nodes {
        //println!("{s}");
        if let Some((j, z)) = num_condensed_steps(&h, &s, &dest_nodes) {
            node_heap.push(Reverse((j, z)));
        }
        else {
            return None;
        }
    }
    //println!("\n");
    let mut memo: HashMap<String, (u64, String)> = HashMap::new();
    let mut count = 0;
    loop {
        let (m, _) = node_heap.peek().unwrap().0;
        let mut donezo = true;
        //println!();
        for t in node_heap.iter() {
            let (i, s) = &t.0;
            //println!("{i}, {s}");
            donezo &= *i == m;
            // donezo = count > 10;
        }
        if donezo {
            break Some(m);
        }
        let (i, s) = node_heap.pop().unwrap().0;
        if let Some((j, q)) = memo.get(&s) {
            node_heap.push(Reverse((i + *j, q.to_string())));
        }
        else {
            if let Some((k, z)) = num_condensed_steps(&h, &s, &dest_nodes) {
                memo.insert(s.to_string(), (k, z.to_string()));
                node_heap.push(Reverse((i + k, z)));
            }
            else {
                break None;
            }
        }
        count += 1;
    }
    */
    //None
}

pub fn num_ghost_steps(source_nodes: Vec<String>, dest_nodes: HashSet<String>, graph: HashMap<String, (String, String)>, inst: &Vec<char>) -> u64 {
    let n_len = inst.len();
    let n = n_len as u64;
    let mut v: Vec<String> = source_nodes;
    let mut u: Vec<String> = Vec::new();
    let mut a = u64::MAX / n;
    for j in 0..1 {
        if let Some(q) = ghost_helper(&v, &dest_nodes, &graph, inst, n_len, j) {
            a = cmp::min(a, (j as u64) + n * q);
        }
        for x in &v {
            let (l, r) = graph.get(x).unwrap();
            u.push((if inst[j] == 'L' { l } else { r }).to_string());
        }
        v.clear();
        v.append(&mut u);
    }
    a
}


fn num_steps_b(source: &str, dest_suffix: &str, graph: &HashMap<String, (String, String)>, inst: &Vec<char>, k: usize) -> (u64, String) {
    let n = inst.len();
    let mut j = k;
    let mut x = source;
    loop {
        let (l, r) = graph.get(x).unwrap();
        x = if inst[j % n] == 'L' { l } else { r };
        j += 1;
        if x.ends_with(dest_suffix) {
            break ((j - k) as u64, x.to_string());
        }
    }
}


pub fn num_ghost_steps(source_nodes: Vec<String>, dest_suffix: &str, graph: HashMap<String, (String, String)>, inst: &Vec<char>) -> u64 {
    let n = inst.len();
    let mut node_heap = BinaryHeap::new();
    println!("Source nodes:");
    for s in source_nodes {
        println!("{s}");
        node_heap.push(Reverse(num_steps_b(&s, dest_suffix, &graph, inst, 0_usize)));
    }
    let mut memo: HashMap<(String, usize), (u64, String)> = HashMap::new();
    let mut donezo = true;
    loop {
        let (m, _) = node_heap.peek().unwrap().0;
        for t in node_heap.iter() {
            let (i, _) = &t.0;
            println!("-, 0: ({i}, {s})");
            donezo &= *i == m;
        }
        println!("donezo: {donezo}, m: {m}");
        if donezo {
            break m;
        }
        let (i, s) = node_heap.pop().unwrap().0;
        let k = ((i + 1) as usize) % n;
        let (x, q) = memo.entry((s.clone(), k)).or_insert(num_steps_b(&s, dest_suffix, &graph, inst, k));
        node_heap.push(Reverse((i + *x, q.to_string())));
        println!("i + *x = {}, s = {s}", i + *x);
        break;
    }
    let (test_i, test_s) = num_steps_b(&"XCZ", dest_suffix, &graph, inst, 11568 % n);
    println!("{test_i}, {test_s}");
    0_u64
}


pub fn num_ghost_steps(source: Vec<String>, dest_suffix: String, graph: HashMap<String, (String, String)>, inst: &Vec<char>) -> u64 {
    let n = inst.len();
    let mut j = 0_usize;
    let mut v = source;
    let mut u = Vec::new();
    let mut donezo = false;
    loop {
        if donezo {
            break j as u64;
        }
        donezo = true;
        for y in &v {
            let (l, r) = graph.get(y).unwrap();
            let x = if inst[j % n] == 'L' { l } else { r };
            u.push(x.to_string());
            donezo &= x.ends_with(&dest_suffix);
        }
        v.clear();
        v.append(&mut u);
        j += 1;
    }
}
*/

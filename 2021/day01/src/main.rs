use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let data: Vec<i32> = io::BufReader::new(File::open("../data.txt").unwrap())
        .lines()
        .map(|line| line.unwrap())
        .map(|line| line.parse::<i32>().unwrap())
        .collect();

    println!(
        "{}",
        data.iter()
            .zip(&data[1..data.len()])
            .map(|pair| if pair.0 < pair.1 { 1 } else { 0 })
            .sum::<i32>()
    );

    println!(
        "{}",
        data.iter()
            .zip(&data[3..data.len()])
            .map(|pair| if pair.0 < pair.1 { 1 } else { 0 })
            .sum::<i32>()
    );
}

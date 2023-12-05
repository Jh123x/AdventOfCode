use std::{collections::HashMap, borrow::BorrowMut};

const INPUT_FILE: &str = "testcase.txt";

fn main() {
    // Read the file
    let input = std::fs::read_to_string(INPUT_FILE).unwrap();

    // Split the input into lines
    let lines: Vec<&str> = input.lines().map(|val| {
        val.trim()
    }).collect();
    let mut points = 0;
    let mut card_map: HashMap<&usize,u64> = std::collections::HashMap::new();
    let mut curr_card_no = std::borrow::Cow::Borrowed(&0);
    for idx in 0..lines.len() {
        let line = lines.get(idx).unwrap();
        let nos = line.split("|").collect::<Vec<&str>>();
        let winning_no = parse_line(nos[0].split(":").collect::<Vec<&str>>()[1]);
        let my_no = parse_line(nos[1]);
        let intersections = winning_no.intersection(&my_no);
        let no_intersections: u64 = intersections.count().try_into().unwrap();
        if no_intersections == 0 {
            continue;
        }
        // Part 1.
        points += i32::pow(2, (no_intersections - 1).try_into().unwrap());

        // Part 2.
        curr_card_no = std::borrow::Cow::Owned(idx + 1);
        if card_map.get(&curr_card_no.clone().to_be()).unwrap() == &0{
            card_map.insert(&curr_card_no, no_intersections);
        } else {
            card_map.insert(&curr_card_no, card_map.get(&curr_card_no.clone().to_be()).unwrap() * no_intersections);
        }
    }
    println!("Part 1 points: {}", points);
}

fn parse_line(line: &str) -> std::collections::HashSet<i32> {
    return line
        .trim()
        .split(" ")
        .filter(|str_val| str_val.len() > 0)
        .map(|val_str| val_str.trim().parse::<i32>().unwrap())
        .collect::<std::collections::HashSet<i32>>();
}

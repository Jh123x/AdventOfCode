const FILENAME: &str = "../input.txt";

fn main() {
    let contents = std::fs::read_to_string(FILENAME).unwrap();
    let mut elves = Vec::new();

    let mut elv_calories = 0;
    for line in contents.lines() {
        if line.len() == 0 {
            elves.push(elv_calories);
            elv_calories = 0;
            continue;
        }
        elv_calories += line.parse::<i32>().unwrap();
    }

    // Get top 3.
    let mut top3 = std::collections::BinaryHeap::new();
    for elv in elves {
        top3.push(std::cmp::Reverse(elv));
        if top3.len() > 3 {
            top3.pop();
        }
    }

    elv_calories = 0;

    while top3.len() > 0 {
        let current = top3.pop().unwrap().0;
        elv_calories += current;
        println!("Calories: {}", current)
    }
    println!("Total calories of top 3: {}", elv_calories);
}

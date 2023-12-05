const INPUT_FILE: &str = "testcase.txt";

fn main() {
    // Read the file
    let input = std::fs::read_to_string(INPUT_FILE).unwrap();

    // Split the input into lines
    let lines: Vec<&str> = input.lines().map(|val| {
        val.trim()
    }).collect();
    let mut points = 0;
    for idx in 0..lines.len() {
        let line = lines.get(idx).unwrap();
        let nos = line.split("|").collect::<Vec<&str>>();
        let winning_no = parse_line(nos[0].split(":").collect::<Vec<&str>>()[1]);
        let my_no = parse_line(nos[1]);
        let intersections = winning_no.intersection(&my_no);
        let no_intersections: u32 = intersections.count().try_into().unwrap();
        if no_intersections == 0 {
            continue;
        }
        // Part 1.
        points += i32::pow(2, no_intersections - 1);


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

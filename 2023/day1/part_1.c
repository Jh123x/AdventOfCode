#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILE_NAME "input.txt"
#define MAX_LINE 256

int parse_line(char *line);
int parse_line_pt_2(char *line);

int main(void)
{
    // Read file
    FILE *fp = fopen(FILE_NAME, "r");

    // Read the file line by line
    char line[MAX_LINE];
    int sum = 0, sum2 = 0;
    while (fgets(line, sizeof(line), fp))
    {
        // Do something with the line
        sum += parse_line(line);
        sum2 += parse_line_pt_2(line);
    }

    printf("Sum: %d\n", sum);

    // Close the file
    fclose(fp);
}

int parse_line(char *line)
{
    int first_digit = -1;
    int second_digit = -1;

    for (int i = 0; i <= MAX_LINE; ++i)
    {
        char chr = line[i];
        if (chr == '\n' || chr == '\0' || chr == EOF)
        {
            break;
        }
        // If a digit is found, store it
        if (chr < '0' || chr > '9')
        {
            continue;
        }
        if (first_digit == -1)
        {
            first_digit = chr - '0';
        }
        second_digit = chr - '0';
    }

    // Convert char to int
    return (int)first_digit * 10 + (int)second_digit;
}

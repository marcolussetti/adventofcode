package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
)

var functions = [][]func(string, []string) string {
	{day1part1, day1part2},
}

func invokeFunction(day int, part int, input string, trailingArgs []string) bool {
	result := functions[day-1][part-1](input, trailingArgs)

	fmt.Printf("\n%v", result)
	return len(result) > 0
}

func printParameters(day int, part int, inputPath string, input string, trailingArgs []string) {
	fmt.Printf("Running AOC 2020 for day %v, part %v. Using input file %v (%v chars, %v lines) and trailing flags [%v]\n\n", day, part, inputPath, len(input), len(strings.Split(input, "\n")), strings.Join(trailingArgs, ", "))
}

func main() {
	// CLI flags
	day := flag.Int("day", 1, "Day of Advent of code")
	part := flag.Int("part", 2, "Part of the day")
	inputPath := flag.String("path", "", "Path to input file. Optional, will try for inputs/day1.txt or inputs/day1part1.txt otherwise.")
	flag.Parse()

	trailingFlags := flag.Args()

	if *day < 0 || *day > len(functions) {
		print("Invalid day.")
	}
	if *part <= 0 || *part < len(functions[*day]) {
		print("Invalid part.")
	}

	data := loadFileWithFallback(*inputPath, *day, *part)

	printParameters(*day, *part, *inputPath, data, trailingFlags)

	result := invokeFunction(*day, *part, data, trailingFlags)

	if result {
		os.Exit(0)
	} else {
		os.Exit(1)
	}
}

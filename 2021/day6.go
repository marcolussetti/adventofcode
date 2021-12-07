package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func countFishes(days int, fishes []int) int {
	dayFishes := make([]int, days)

	// Pre-seed the first round because it starts lower than 0
	for fish := range fishes {
		for newDay := fishes[fish]; newDay < days; newDay += 7 {
			dayFishes[newDay] += 1
		}
	}
	for day := range dayFishes {
		for newDay := day + 9; newDay < days; newDay += 7 {
			dayFishes[newDay] += dayFishes[day]
		}
	}

	total := len(fishes)
	for day := range dayFishes {
		total += dayFishes[day]
	}

	return total
}

func main() {
	dataString, _ := os.ReadFile("day6.txt")
	dataSlice := strings.Split(string(dataString), ",")
	dataIntSlice := []int{}
	for i := range dataSlice {
		iInt, _ := strconv.Atoi(dataSlice[i])
		dataIntSlice = append(dataIntSlice, iInt)
	}

	fmt.Printf("Part A: %d\n", countFishes(80, dataIntSlice))
	fmt.Printf("Part B: %d\n", countFishes(256, dataIntSlice))

}

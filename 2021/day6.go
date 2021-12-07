package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	dataString, _ := os.ReadFile("day6.txt")
	dataSlice := strings.Split(string(dataString), ",")
	dataIntSlice := []int{}
	for i := range dataSlice {
		iInt, _ := strconv.Atoi(dataSlice[i])
		dataIntSlice = append(dataIntSlice, iInt)
	}

	// Test dataset
	// dataIntSlice = []int{3, 4, 3, 1, 2}

	// Only gets to day 228 before it dies out of memory
	// for day := 0; day < 256; day++ {
	// 	fmt.Println(day)
	// 	for f := range dataIntSlice {
	// 		if dataIntSlice[f] == 0 {
	// 			dataIntSlice[f] = 6
	// 			dataIntSlice = append(dataIntSlice, 8)
	// 		} else {
	// 			dataIntSlice[f] -= 1
	// 		}
	// 	}
	// }
	DAY_MAX := 256
	dayFishes := make([]int, DAY_MAX)

	// Pre-seed the first round because it starts lower than 0
	for fish := range dataIntSlice {
		for newDay := dataIntSlice[fish]; newDay < DAY_MAX; newDay += 7 {
			dayFishes[newDay] += 1
		}
	}
	for day := range dayFishes {
		for newDay := day + 9; newDay < DAY_MAX; newDay += 7 {
			dayFishes[newDay] += dayFishes[day]
		}
	}

	total := len(dataIntSlice)
	for day := range dayFishes {
		total += dayFishes[day]
	}

	fmt.Print(total)
}

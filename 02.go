package main

import (
	"strconv"
	"strings"
)

func day2part1(input string, _ []string) string {
	values := strings.Split(string(input), "\n")


	var matchingRows []int
	for rowNum, value := range values {
		if len(value) == 0 {
			continue
		}
		value = strings.ReplaceAll(value, "-", " ")
		value = strings.ReplaceAll(value, ": ", " ")
		//print(value)
		valueArr := strings.Split(value, " ")
		first, _ := strconv.Atoi(valueArr[0])
		second, _ := strconv.Atoi(valueArr[1])
		letter := valueArr[2]
		target := valueArr[3]

		var matches []string
		for _, targetLetter := range target {
			if letter == string(targetLetter) {
				matches = append(matches, string(targetLetter))
			}
		}

		if len(matches) >= first && len(matches) <= second {
			matchingRows = append(matchingRows, rowNum)
		}
	}

	return strconv.Itoa(len(matchingRows))
}

func day2part2(input string, _ []string) string {
	values := strings.Split(string(input), "\n")

	var matchingRows []int
	for rowNum, value := range values {
		if len(value) == 0 {
			continue
		}
		value = strings.ReplaceAll(value, "-", " ")
		value = strings.ReplaceAll(value, ": ", " ")
		valueArr := strings.Split(value, " ")
		first, _ := strconv.Atoi(valueArr[0])
		second, _ := strconv.Atoi(valueArr[1])
		letter := valueArr[2]
		target := valueArr[3]

		var matches []bool
		for _, targetLetter := range target {
			matches = append(matches, string(targetLetter) == letter)
		}

		if btoi(matches[first-1]) ^ btoi(matches[second-1]) == 1 {
			matchingRows = append(matchingRows, rowNum)
		}
	}

	return strconv.Itoa(len(matchingRows))
}

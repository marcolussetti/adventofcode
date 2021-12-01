package main

import (
	"io/ioutil"
	"math"
	"os"
	"strconv"
	"strings"
)

func readLines(path string) []string {
	content, err := ioutil.ReadFile(path)
	print(content)
	if err == nil {
		//print(err)
		os.Exit(-1)
	}

	lines := strings.Split(string(content), "\n")

	return lines;
}

func calcFuel(value int) int {
	fuel := int(math.Floor(float64(value) / 3.0)) - 2
	if fuel <0 {
		fuel = 0
	}

	return fuel
}

func sumSlice(input []int) int {
	var acc = 0

	for _, val := range input {
		acc += val
	}

	return acc
}

func main() {
	println("whut")
	// Read input
	lines := readLines("../inputs/01")

	var fuels []int

	for _, line := range lines {
		iLine, _ := strconv.Atoi(line)
		fuels = append(fuels, calcFuel(iLine))
	}

	sumFuels := sumSlice(fuels)

	println("Result 1: ", sumFuels)

	println("yo", lines[0])
}

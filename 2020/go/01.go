package main

import (
	"fmt"
	"strconv"
	"strings"
)

func day1part1(input string, _ []string) string {
	target := 2020

	values := strings.Split(string(input), "\n")

	var integers []int
	for _, value := range values {
		integer, _ := strconv.Atoi(value)
		integers = append(integers, integer)
	}

	for _, integer := range integers {
		for _, innerInt := range integers {
			if integer == innerInt {
				continue
			}

			if integer+innerInt == target {
				fmt.Printf("%v+%v=%v, %v*%v=%v\n", integer, innerInt,
					integer+innerInt, integer, innerInt, integer*innerInt)
				return strconv.Itoa(integer * innerInt)
			}
		}
	}
	return ""
}

func day1part2(input string, _ []string) string {
	target := 2020

	values := strings.Split(string(input), "\n")

	var integers []int
	for _, value := range values {
		integer, _ := strconv.Atoi(value)
		integers = append(integers, integer)
	}

	for _, integer := range integers {
		for _, innerInt := range integers {
			for _, evenInnerInt := range integers {
				if integer == innerInt || integer == evenInnerInt || evenInnerInt == innerInt {
					continue
				}

				if integer+innerInt+evenInnerInt == target {
					fmt.Printf("%v+%v+%v=%v, %v*%v*%v=%v\n", integer, innerInt, evenInnerInt,
						integer+innerInt+evenInnerInt, integer, innerInt, evenInnerInt, integer*innerInt*evenInnerInt)
					return strconv.Itoa(integer * innerInt * evenInnerInt)
				}
			}
		}
	}
	return ""
}

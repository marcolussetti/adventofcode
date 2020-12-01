package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	target := 2020
	data, _ := ioutil.ReadFile("input")
	values := strings.Split(string(data), "\n")

	var integers []int
	for _, value := range values {
		integer, _ := strconv.Atoi(value)
		integers = append(integers, integer)
	}

	//print(integers)

	for _, integer := range integers {
		for _, innerInt := range integers {
			for _, evenInnerInt := range integers {
				if integer == innerInt || integer == evenInnerInt || evenInnerInt == innerInt {
					continue
				}

				if integer+innerInt+evenInnerInt == target {
					fmt.Printf("%v+%v+%v=%v, %v*%v*%v=%v\n", integer, innerInt, evenInnerInt,
						integer+innerInt+evenInnerInt, integer, innerInt, evenInnerInt, integer*innerInt*evenInnerInt)
					break
				}
			}
		}
	}
}

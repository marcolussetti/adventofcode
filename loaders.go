package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func pathExists(path string, dir bool) bool {
	status, err := os.Stat(path)
	if os.IsNotExist(err) {
		return false
	}
	if dir {
		return status.IsDir()
	} else {
		return !status.IsDir()
	}
}

func loadFile(path string) string {
	if len(path) > 0 {
		inputBytes, err := ioutil.ReadFile(path)
		if err != nil {
			log.Fatal(err)
		}
		return string(inputBytes)
	}

	return ""
}

func loadFileWithFallback(path string, day int, part int) string {
	const basePath = "inputs"

	if len(path) > 0 {
		return loadFile(path)
	}

	if !pathExists(basePath, true) {
		return ""
	}

	if pathExists(fmt.Sprintf("%v/day%vpart%v.txt", basePath, day, part), false) {
		return loadFile(fmt.Sprintf("%v/day%vpart%v.txt", basePath, day, part))
	}

	if pathExists(fmt.Sprintf("%v/day%v.txt", basePath, day), false) {
		return loadFile(fmt.Sprintf("%v/day%v.txt", basePath, day))
	}

	return ""
}

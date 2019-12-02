let fs = require('fs')

const lines = fs.readFileSync('../inputs/01').toString().split('\n')

function calc_fuel(item) {
    const fuel = Math.floor(parseFloat(item) / 3.0) - 2
    return fuel > 0 ? fuel : 0
}

const fuels_sum = lines.reduce((acc, i) => acc + calc_fuel(i), 0)

console.log(`Result 1: ${fuels_sum}`)

// Part 2

function calc_fuel_with_fuel(item) {
    total_fuel = residual_fuel = calc_fuel(item)

    while (residual_fuel > 0) {
        residual_fuel = calc_fuel(residual_fuel)
        total_fuel += residual_fuel
    }

    return total_fuel
}

const fuels_sum_2 = lines.reduce((acc, i) => acc + calc_fuel_with_fuel(i), 0)
console.log(`Result 2: ${fuels_sum_2}`)

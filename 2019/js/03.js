let fs = require('fs')

const lines = fs.readFileSync('../inputs/03').toString().split('\n').map(line => line.split(','))

const test_inputs_1 = [
    "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","),
    "U62,R66,U55,R34,D71,R55,D58,R83".split(",")
]
const test_inputs_2 = [
    "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
    "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")
]

function generate_points(instructions) {
    let current_point = [0, 0]
    const points = []
    instructions.forEach(instruction => {
        const direction = instruction.substring(0, 1)
        const value = parseInt(instruction.substring(1))
        Array(value).fill().map((_, i) => {
            if (direction === 'R')
                current_point[1]++
            else if (direction === 'L')
                current_point[1]--
            else if (direction === 'U')
                current_point[0]++
            else if (direction === 'D')
                current_point[0]--
            points.push([...current_point])
        })
    })

    return points
}

function manhattan_distance(a, b) {
    console.log(a)
    const vals = a.map((x1, i) => {
        return Math.abs(x1 - b[i])
    })


    return vals.reduce((acc, val) => acc + val, 0)
}

function common_elements(a, b) {
    // See https://exploringjs.com/impatient-js/ch_sets.html#missing-set-operations
    const set_a = [...new Set([...a].map((xy, _) => `${xy[0]},${xy[1]}`))]
    const set_b = [...new Set([...b].map((xy, _) => `${xy[0]},${xy[1]}`))]

    const instersection = [...set_a].filter(el => set_b.indexOf(el) >= 0).map(el => el.split(",").map(s => parseInt(s)))

    // const instersection = [...set_a].filter(el => {
    //     return [...set_b].filter(innerEl => el[0] === innerEl[0] && el[1] === innerEl[1]).length > 0
    // })

    return instersection
}

function min_manhattan_distance(a, b) {
    const points_a = generate_points(a)
    const points_b = generate_points(b)
    const common_points = common_elements(points_a, points_b)
    const distances = common_points.map(point => manhattan_distance(point, [0, 0]))

    return Math.min(...distances)
}

// Example 1
console.log(`Test set 1: ${min_manhattan_distance(...test_inputs_1)}`)
// Example 2
console.log(`Test set 2: ${min_manhattan_distance(...test_inputs_2)}`)

// Result 1
console.log(`Test set 1: ${min_manhattan_distance(...lines)}`)

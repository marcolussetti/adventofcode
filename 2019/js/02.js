let fs = require('fs')

const lines = fs.readFileSync('../inputs/02').toString().split(',').map(item => parseInt(item.trim()))
//console.table(lines)

const ops = {
    1: (a, b) => { return a + b },
    2: (a, b) => { return a * b }
}

function run_program(inputs, noun, verb, advance_step = 4) {
    let program = [...inputs]
    program[1] = noun
    program[2] = verb

    let op = 0
    while (program[op] !== 99) {
        program[program[op + 3]] = ops[program[op]](program[program[op + 1]], program[program[op + 2]])
        op += advance_step
    }

    return program[0]
}

//console.log(run_program([2, 4, 4, 5, 99, 0], 4, 4))

// Result 1
const result_1 = run_program(lines, 12, 2)
console.log(`Result 1: ${result_1}`)


// Part 2

const nouns = Array(100).fill().map((_, i) => i + 1)
const verbs = [...nouns]

const nounsVerbs = nouns.flatMap(n => verbs.map(v => [n, v]))

const results_2 = nounsVerbs.map(nv => {
    return { "noun": nv[0], "verb": nv[1], "result": run_program(lines, nv[0], nv[1]) }
})

const match_2 = results_2.filter(nvr => nvr.result === 19690720)[0]

console.log(`Result 2: ${100 * match_2.noun + match_2.verb}. Noun: ${match_2.noun}. Verb: ${match_2.verb}.`)

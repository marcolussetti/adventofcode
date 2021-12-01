<?php

$input_string = file_get_contents('../inputs/02');
$inputs = explode(",", $input_string);
$inputs = array_map(function($input) {return (int) $input;}, $inputs);


$ADVANCE_STEP = 4;

//print join(",", $inputs);

function run_program($values, $noun, $verb, $advance_step)
{
    $lines = (new ArrayObject($values))->getArrayCopy();
    $lines[1] = $noun;
    $lines[2] = $verb;


    $op = 0;
    while ($lines[$op] !== 99) {
        $operator = $lines[$op];
        $params = [$lines[$op + 1], $lines[$op + 2], $lines[$op + 3]];

        if ($operator === 1) {
            // Addition
            $lines[$params[2]] = $lines[$params[0]] + $lines[$params[1]];
        } elseif ($operator === 2) {
            // Multiply
            $lines[$params[2]] = $lines[$params[0]] * $lines[$params[1]];
        }

        // Advance
        $op = $op + $advance_step;
    }

    return $lines[0];
}

// print_r(run_program([2, 4, 4, 5, 99, 0], 4, 4, $ADVANCE_STEP)[0]);

$result_1 =run_program($inputs, 12, 2, $ADVANCE_STEP);

print(sprintf("Part 1: %d\n", $result_1));

// PART 2

$TARGET_RESULT = 19690720;

foreach (range(1, 100) as $noun) {
    foreach (range(1, 100) as $verb) {
        $result = run_program($inputs, $noun, $verb, $ADVANCE_STEP);
        if ($result === $TARGET_RESULT) {
            $result_2 = 100 * $noun + $verb;
            print(sprintf("Result 2: %d. Noun: %d. Verb: %d", $result_2, $noun, $verb));
            break;
        }
    }
}

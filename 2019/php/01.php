<?php

$input_string = file_get_contents('../inputs/01');
$inputs = explode(PHP_EOL, $input_string);

// print(join("\n", $inputs));

function calc_fuel($mass)
{
    $val = ((int)floor($mass / 3.0)) - 2;
    return $val >= 0 ? $val : 0;
}

//print(calc_fuel(14));

$fuels = array_map('calc_fuel', $inputs);

$result = array_reduce($fuels, function ($cumulative, $value) {
    return $cumulative += $value;
});

echo(sprintf("Result 1: %d\n", $result));

// Part 2

function calc_fuel_with_fuel($mass)
{
    $module_fuel = calc_fuel($mass);
    $total_fuel = $module_fuel;
    $residual_fuel = $module_fuel;

    while ($residual_fuel > 0) {
        $residual_fuel = calc_fuel($residual_fuel);
        $total_fuel += $residual_fuel;
    }

    return $total_fuel;
}

$fuels_2 = array_map('calc_fuel_with_fuel', $inputs);

$result_2 = array_reduce($fuels_2, function ($cumulative, $value) {
    return $cumulative += $value;
});
print sprintf("Result 2: %d\n", $result_2);

print("\n");

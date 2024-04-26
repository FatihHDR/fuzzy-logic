# Fuzzy Logic Temperature Control

This project implements a simple fuzzy logic system for temperature control. The system uses fuzzy sets to represent different temperature ranges and corresponding heating levels.

## Fuzzy Sets

The fuzzy sets defined in the system are as follows:

- `dingin`: Represents low temperatures.
- `hangat`: Represents moderate temperatures.
- `panas`: Represents high temperatures.

Each fuzzy set is defined with a name, a low value, a high value, and a midpoint value.

## Membership Function

The membership function calculates the degree of membership of a given input value to a fuzzy set. It returns 0 if the input value is outside the range of the fuzzy set, and a value between 0 and 1 if the input value is within the range.

## Rules

The system defines rules that map input temperature ranges to output heating levels:

- If the temperature is cold, then the heating level is low.
- If the temperature is warm, then the heating level is medium.
- If the temperature is hot, then the heating level is high.

## Usage

To use the system, instantiate the `FuzzySet` class for each temperature range and heating level, define the rules, and then calculate the membership values for a given input temperature. The output heating level is determined by aggregating the membership values according to the rules.

## License

This project is open source and available under the MIT License.

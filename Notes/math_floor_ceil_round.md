
## Math.floor vs Round vs Math.ceil

`math.floor` rounds down. Take any value and returns the nearest lower integer no matter the decimal point
for example
`6.6` becomes `6`

`math.ceil` is the opposite of math.floor. It returns the next highest integer to the given value. For example, `6.2` becomes `7`

`round` follows standard rounding rules. `0.6` and up is rounded to next highest integer, `0.5` and below is rounded to next lowest integer
for example
`6.6` becomes `7`
`6.5` becomes `6`

Comparision example

```
print(round(6.9)) # result is 7
print(math.floor(6.9)) # result is 6
print(math.ceil(6.9)) # result is 7
print(math.ceil(6.1)) # result is 7
```
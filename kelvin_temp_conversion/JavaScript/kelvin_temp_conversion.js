// The consant value for Kelvin temperature
const kelvin = 293;

// The constant value for Celsius
const celsius = kelvin - 273;
console.log(`The temperature is ${celsius} degrees Celsius.`)

// value for Fahrenheit 
let Fahrenheit = celsius * (9/5) + 32
console.log(`The temperature is ${Fahrenheit} degrees Fahrenheit when not rounded.`)

// rounding Fahrenheit
Fahrenheit = Math.floor(Fahrenheit)

console.log(`The temperature is ${Fahrenheit} degrees Fahrenheit.`)

// Convert temperature to newton scale
let newton = Math.floor(celsius * (33/100))
console.log(`The temperature is ${newton} degrees newton.`)
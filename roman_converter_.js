
const romanNumerals = [
    { value: 1000, numeral: 'M' },
    { value: 900, numeral: 'CM' },
    { value: 500, numeral: 'D' },
    { value: 400, numeral: 'CD' },
    { value: 100, numeral: 'C' },
    { value: 90, numeral: 'XC' },
    { value: 50, numeral: 'L' },
    { value: 40, numeral: 'XL' },
    { value: 10, numeral: 'X' },
    { value: 9, numeral: 'IX' },
    { value: 5, numeral: 'V' },
    { value: 4, numeral: 'IV' },
    { value: 1, numeral: 'I' }
  ];
function to_roman(num) {
    // using grd algorithm
    let result = '';

    romanNumerals.forEach(({value, numeral})=> {
    while(num >= value) {
        result += numeral;
        num -=value;
        }
    })
    return result;
    
}
// console.log(to_roman(1994)); // MCMXCIV

function to_number(str) {
    let total = 0;
    let prevValue = 0;
    for (let i = str.length - 1 ; i >= 0; i--) {
        let currentValue = romanNumerals.find(({numeral}) => numeral === str[i]).value;
        if (currentValue < prevValue) {
            total -= currentValue;

        }
        else {
            total += currentValue;
        }
        prevValue = currentValue;
        
    }
    return total;

}
console.log(to_number('IV')); // 1994
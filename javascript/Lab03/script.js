// Lab03 - Number to Phrase

// create object for reference
let onesphrase = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
let teensphrase = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sisteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
let tensphrase = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

// ask user for a number 0 - 999
let usernumber = parseFloat(prompt("Enter upto 3 digit number from 0 - 999: "))


// convert to phrase
let hundredsdigit, tensdigit

if (usernumber > 99) {
    hundredsdigit = Math.floor(usernumber / 100)
    tensdigit = Math.floor(usernumber % 100 / 10)
}
else {
    tensdigit = Math.floor(usernumber / 10)
}
let onesdigit = usernumber % 10

// create phrase
let hundpartphrase, tenspartphrase, onespartphrase
if (hundredsdigit > 0) {
    hundpartphrase = onesphrase[hundredsdigit] + " hundred"
}
if (tensdigit > 0) {
    if (tensdigit == 1){
        tenspartphrase = teensphrase[onesdigit + 10]
    }
    else {
        tenspartphrase = tensphrase[tensdigit]
        onespartphrase = onesphrase[onesdigit]
    }

}
else {
    onespartphrase = onesphrase[onesdigit]
}

let convertedphrase = ""
if (hundredsdigit > 0) {
    convertedphrase += hundpartphrase
    if (tensdigit > 0 || onesdigit > 0) {
        convertedphrase += " and "
    }
}
if (tensdigit > 1) {
    convertedphrase += tenspartphrase
    if (onesdigit > 0) {
        convertedphrase += onespartphrase
    }
}
else if (tensdigit == 1) {
    convertedphrase += tenspartphrase
}
else if (onesdigit > 0) {
    convertedphrase += onespartphrase
}

alert(convertedphrase)

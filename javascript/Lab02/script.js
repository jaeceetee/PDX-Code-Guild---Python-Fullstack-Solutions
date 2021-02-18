// Lab02 - ROT Cipher - ROT 13

let cypher = {}
//build cypher object
let alphabet = Array.apply(undefined, Array(26)).map(function(x,y) { return String.fromCharCode(y + 65); }).join('');
alphabet += Array.apply(undefined, Array(26)).map(function(x,y) { return String.fromCharCode(y + 97); }).join('');

for (letter of alphabet) {
    if (alphabet.indexOf(letter) + 13 > 51) {
        cypher[letter] = alphabet[alphabet.indexOf(letter) - 39]
    }
    else {
        cypher[letter] = alphabet[alphabet.indexOf(letter) + 13]
    }
}

// get user string
let userinput = prompt("What string would you like to encrypt in ROT 13? ")

// build new string
let encryptedtext = ""
for (char of userinput) {
    encryptedtext += cypher[char]
}

// print the excrypted string
alert(encryptedtext)
// Lab01 - Python lab 7 - Rock, Paper, Scissors

let choices = ['rock', 'paper', 'scissors']
do {

    userchoice = prompt("Rock, paper, or scissors?: ").toLowerCase()

    compchoice = choices[Math.floor(Math.random() * choices.length)]
    message = ''
    if (userchoice == compchoice){
        message = `You are tied! Computer chose ${compchoice}`
    }
    else if (userchoice == "rock"){
        if (compchoice == "paper"){
            message = `Computer wins! ${compchoice} beats ${userchoice}`
        }
        else {
            message = `You win! ${userchoice} beats ${compchoice}`
        }
    }
    else if (userchoice == "scissors"){
        if (compchoice == "rock"){
            message = `Computer wins! ${compchoice} beats ${userchoice}`
        }
        else {
            message = `You win! ${userchoice} beats ${compchoice}`
        }
    }
    else if (userchoice == "paper"){
        if (compchoice == "scissors"){
            message = `Computer wins! ${compchoice} beats ${userchoice}`
        }
        else {
            message = `You win! ${userchoice} beats ${compchoice}`
        }
    }

    alert(message)
}
while (prompt("Enter Y to continue: ") == "Y")
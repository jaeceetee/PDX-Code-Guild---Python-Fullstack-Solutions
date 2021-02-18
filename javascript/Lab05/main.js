let app = new Vue({
    el: '#app',
    data: {
        cardNumber: "",
        validCard: "NOT valid",
        visible: true
    },
    methods: {
        checkCard: function(){
            if (this.cardNumber.length == 16) {
                let numbers = this.cardNumber.split("")
                let checkDigit = numbers.pop()
                numbers.reverse()

                console.log(numbers)

                for (i in numbers) {
                    if ((i % 2) == 0){
                        numbers[i] *= 2
                    }
                    else{
                        numbers[i] = Number(numbers[i])
                    }
                }
                

                console.log(numbers)

                for (i in numbers) {

                    if (numbers[i] > 9) {
                        numbers[i] -= 9
                    }
                }

                let sumValue = 0

                for (num of numbers) {
                    sumValue += num
                }

                sumValue = sumValue.toString()
                console.log(sumValue[1], checkDigit)
                if (sumValue[1] === checkDigit) {
                    this.validCard = "valid"
                    console.log("It's valid!")
                }
                else{
                    this.validCard = "NOT valid"
                }

                this.visible = false
                

                //let checkDigit = this.cardNumber.splice(15, 1)
                console.log(this.visible)
                //console.log(this.cardNumber)
                console.log(numbers)
                //console.log(reverseNumbers)
            }

        }

    }
})

//4556737586899855
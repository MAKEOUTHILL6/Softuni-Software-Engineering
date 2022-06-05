function bonus(input){
    let bonusPoints = 0;
    let num = Number(input[0]);

    if(num % 2 == 0){
        bonusPoints += 1
        if(num <= 100){
            bonusPoints += 5
        }
        else if(num > 1000){
            bonusPoints += num * 0.1
        }
        else{
            bonusPoints += num * 0.2
        }
    }
    else if(num % 5 == 0){
        bonusPoints += 2
        if(num <= 100){
            bonusPoints += 5
        }
        else if(num > 1000){
            bonusPoints += num * 0.1
        }
        else{
            bonusPoints += num * 0.2
        }
    }
    else{
        if(num <= 100){
            bonusPoints += 5
        }
        else if(num > 1000){
            bonusPoints += num * 0.1
        }
        else{
            bonusPoints += num * 0.2
        }
    }
    console.log(bonusPoints);
    console.log(num + bonusPoints);
}
bonus(["15875"]);
function vacation(input){
    let index = 0;
    let vacationPrice = Number(input[index]);
    index++;
    let budget = Number(input[index]);
    index++;
    let daysSpending = 0;
    let totalDays = 0;
    let isSuccessful = true;
    while(budget < vacationPrice){
        let action = input[index];
        index++;
        let current_money = Number(input[index]);
        index++;
        if(action === "spend"){
            budget -= current_money;
            if(budget < 0){
                budget = 0;
            }
            daysSpending++;
        }
        else if(action === "save"){
            budget += current_money;
            daysSpending = 0;
        }
        totalDays++
        if(daysSpending == 5){
            console.log(`You can't save the money.`);
            console.log(totalDays);
            isSuccessful = false;
            break;
        }

    }
    if(isSuccessful){
        console.log(`You saved the money for ${totalDays} days.`)
    }
}
vacation(["2000",
"1000",
"spend",
"1200",
"save",
"2000"])
;

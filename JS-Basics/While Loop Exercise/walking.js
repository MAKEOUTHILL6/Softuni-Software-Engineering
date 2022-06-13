function walking(input){
    let index = 0;
    let goal = 10000;
    let diff = 0;
    let command = input[index];
    index++
    let totalSteps = 0;
    let isSuccessful = true;
    while(totalSteps <= goal){
        if(command === "Going home"){
            bonus_steps = Number(input[index]);
            totalSteps += bonus_steps;
            isSuccessful = false;
            break;
        }
        current_steps = Number(command);
        totalSteps += current_steps;

        command = input[index];
        index++
    }
    diff = Math.abs(totalSteps - goal);
    if(isSuccessful === true){
        console.log("Goal reached! Good job!")
        console.log(`${diff} steps over the goal!`)
    }
    else{
        console.log(`${diff} more steps to reach goal.`)
    }

}
walking(["1500",
"3000",
"250",
"1548",
"2000",
"Going home",
"2000"])

;

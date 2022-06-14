function calc(input){
    let index = 1;
    let destination = input[0];
    let minimalBudget = Number(input[1]);
    let savedMoney = 0;
    while(destination !== "End"){
        index++;
        while(savedMoney < minimalBudget){
            savedMoney += Number(input[index]);
            index++;
        }
        console.log(`Going to ${destination}!`);
        destination = input[index];
        index++;
        minimalBudget = Number(input[index]);
        savedMoney = 0;
    }

}
calc(["Greece",
"1000",
"200",
"200",
"300",
"100",
"150",
"240",
"Spain",
"1200",
"300",
"500",
"193",
"423",
"End"]);

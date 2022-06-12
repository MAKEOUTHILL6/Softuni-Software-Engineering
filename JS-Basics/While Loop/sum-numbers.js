function calc(input){
    let mainSum = Number(input[0]);
    let sumNums = 0;
    let index = 1;
    let inputL = input.length;
    while(index <= inputL){
        let current_num = Number(input[index]);
        sumNums += current_num;
        index++
        if(sumNums >= mainSum){
            console.log(sumNums);
            break;
        }
    }
}
calc(["20",
"1",
"2",
"3",
"4",
"5",
"6"])
;

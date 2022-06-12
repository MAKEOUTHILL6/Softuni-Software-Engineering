function calc(input){
    let range = Number(input[0]);
    let index = 0;
    let tempNum = 1;
    while(index < range){
        if(tempNum > range){
            break;
        }
        console.log(tempNum);
        tempNum = tempNum * 2 + 1;
        index++
    }
}
calc(["31"]);
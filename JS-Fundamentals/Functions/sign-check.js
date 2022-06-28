function solve(numOne, numTwo, numThree){
    let numArr = [numOne, numTwo, numThree];
    let negCount = 0;
    let res;
    for(let el of numArr){
        if(el < 0){
            negCount ++;
        }
    }
    if(negCount % 2 !== 0){
        res = "Negative";
    }else{
        res = "Positive";
    }
    console.log(res);
}
solve(-6,
    -12,
     14
    )
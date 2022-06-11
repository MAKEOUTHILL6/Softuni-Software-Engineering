function func(input){
    let age = Number(input[0]);
    let washerPrice = Number(input[1]);
    let toyPrice = Number(input[2]);
    let sumMoney = 0;
    let diff = 0;
    let count = 0;
    for(let a=1; a <= age; a++){
        if(a % 2 === 0){
            count += 1
            sumMoney += count * 10
            sumMoney -=1
        }
        else if(a % 2 !== 0){
            sumMoney += toyPrice
        }
    }
    diff = Math.abs(washerPrice - sumMoney);

    if(washerPrice <= sumMoney){
        console.log(`Yes! ${diff.toFixed(2)}`)
    }
    else{
        console.log(`No! ${diff.toFixed(2)}`)
    }

}
func(["21",
"1570.98",
"3"])
;

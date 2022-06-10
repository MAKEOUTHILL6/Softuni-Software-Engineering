function calc(input){
    let firstNum = Number(input[0]);
    let secondNum = Number(input[1]);
    let sum = 0;
    for(let a=firstNum; a<=secondNum; a++){
        if(a % 9 === 0){
            sum += a
        }
    }
    console.log(`The sum: ${sum}`)

    for(let a=firstNum; a<=secondNum; a++){
        if(a % 9 === 0){
            console.log(a);
        }
    }
}
calc(["100", "200"]);
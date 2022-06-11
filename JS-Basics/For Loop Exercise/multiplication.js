function table(input){
    let power = Number(input[0]);
    for(let a=1; a <= 10; a++){
        console.log(`${a} * ${power} = ${power * a}`)
    }
}
table(["5"]);
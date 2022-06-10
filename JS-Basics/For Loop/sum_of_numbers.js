function calc(input){
    let seq = input[0];
    let sum = 0;
    for(let a=0; a < seq.length; a++){
        sum+= parseInt(seq[a]);
    }
    console.log(`The sum of the digits is:${sum}`)
}
calc(["1234"]);
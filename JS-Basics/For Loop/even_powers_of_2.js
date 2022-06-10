function calc(input){
    let num = Number(input[0]);
    for(let a=0; a<=num; a++){
        if(a % 2 ===0){
            console.log(2**a)
        }
    }
}
calc(["7"]);
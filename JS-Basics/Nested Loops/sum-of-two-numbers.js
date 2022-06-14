function calc(input){
    let startIndex = Number(input[0]);
    let endIndex = Number(input[1]);
    let magicNumber = Number(input[2]);
    let iteration = 0;
    let isSuccessful = false;
    for(let i=startIndex; i<=endIndex; i++){
        if(isSuccessful){
            break;
        }
        for(let h=startIndex; h<=endIndex; h++){
            iteration++
            let sumNums = i + h
            if(sumNums === magicNumber){
                isSuccessful = true;
                console.log(`Combination N:${iteration} (${i} + ${h} = ${magicNumber})`);
                break;
            }
            else{
                isSuccessful = false;
            }
        }
    }
    if(isSuccessful === false){
        console.log(`${iteration} combinations - neither equals ${magicNumber}`)
    }

}
calc(["1",
"10",
"5"])
;

function operations(input){
    let fnum = Number(input[0]);
    let snum = Number(input[1]);
    let operator = input[2];
    let result = 0;
    if(operator === "+"){
        result = fnum + snum;
        if(result % 2 === 0){
            console.log(`${fnum} ${operator} ${snum} = ${result} - even`)
        }
        else{
            console.log(`${fnum} ${operator} ${snum} = ${result} - odd`)
        }
    }
    else if(operator === "-"){
        result = fnum - snum;
        if(result % 2 === 0){
            console.log(`${fnum} ${operator} ${snum} = ${result} - even`)
        }
        else{
            console.log(`${fnum} ${operator} ${snum} = ${result} - odd`)
        }
    }
    else if(operator === "*"){
        result = fnum * snum;
        if(result % 2 === 0){
            console.log(`${fnum} ${operator} ${snum} = ${result} - even`)
        }
        else{
            console.log(`${fnum} ${operator} ${snum} = ${result} - odd`)
        }
    }
    else if(operator === "/"){
        if(snum === 0){
            console.log(`Cannot divide ${fnum} by zero`);
        }
        else{
            result = fnum / snum;
            if(result % 2 === 0){
                console.log(`${fnum} ${operator} ${snum} = ${result.toFixed(2)}`)
            }
            else{
                console.log(`${fnum} ${operator} ${snum} = ${result.toFixed(2)}`)
            }
        }
    }
    else if(operator === "%"){
        if(snum === 0){
            console.log(`Cannot divide ${fnum} by zero`);
        }
        else{
            result = fnum % snum;
            if(result % 2 === 0){
                console.log(`${fnum} ${operator} ${snum} = ${result}`)
            }
            else{
                console.log(`${fnum} ${operator} ${snum} = ${result}`)
            }
        }
    }     
}
operations(["112",
"0",
"/"])
;

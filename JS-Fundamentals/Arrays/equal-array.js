function solve(firstArray, secondArray){
    let res = 0;
    let areEqual = true;
    for(let i=0; i<firstArray.length; i++){
        if(firstArray[i] !== secondArray[i]){
            console.log(`Arrays are not identical. Found difference at ${i} index`)
            areEqual = false;
            break;
        }else{
            res += Number(firstArray[i]);
        }
    }
    if(areEqual){
        console.log(`Arrays are identical. Sum: ${res}`);
    }
}
solve(['10','20','30'], ['10','20','30']);
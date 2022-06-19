function calc(num){
    num = num.toString();
    let subNumsSum = 0;
    for(let i=0; i<num.length; i++){
        subNumsSum += Number(num[i]);
    }
    if(subNumsSum.toString().includes("9")){
        console.log(`${num} Amazing? True`)
    }else{
        console.log(`${num} Amazing? False`)
    }

}
calc(999);
function calc(num){
    num = String(num);
    sum = 0;
    for(let i=0; i < num.length; i++){
        sum += Number(num[i]);
    }
    console.log(sum);
}
calc(245678);
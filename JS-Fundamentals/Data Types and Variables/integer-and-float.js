function calc(num1, num2, num3){
    let res = num1 + num2 + num3;
    if(res % 1 !== 0){
        res += " - Float";
    }else{
        res += " - Integer";;
    }
    console.log(res)
}
calc(100, 200, 303);
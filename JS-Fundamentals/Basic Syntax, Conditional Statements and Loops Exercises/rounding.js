function rounding(n, prec){
    let num = n;
    let precision = prec;

    if(precision > 15){
        precision = 15;
    }
    num = num.toFixed(precision);
    console.log(parseFloat(num));

}
rounding(10.5,3)
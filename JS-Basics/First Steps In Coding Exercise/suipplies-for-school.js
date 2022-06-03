function materials(input){
    let pricePens = Number(input[0]) * 5.80;
    let priceMarkers = Number(input[1]) * 7.20;
    let priceSpray = Number(input[2]) * 1.20;
    let discount = Number(input[3]) / 100;
    let total = priceMarkers + pricePens + priceSpray;
    let final = total - (total * discount);
    console.log(final);
}

materials(["2 ",
"3 ",
"4 ",
"25 "]
)
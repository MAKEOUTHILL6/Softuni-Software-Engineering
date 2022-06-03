function repaint(input){
    let priceNylon = (Number(input[0]) + 2) * 1.50;
    let pricePaint = (Number(input[1]) + (Number(input[1]) * 0.10)) * 14.50;
    let priceSpray = Number(input[2]) * 5;
    let hours = Number(input[3]);
    let priceBags = 0.40;
    let total = priceBags + priceSpray + pricePaint + priceNylon;
    let sumWorkers = (total * 0.3) * hours;
    let final = sumWorkers + total;
    console.log(final);
}
repaint(["10 ",
"11 ",
"4 ",
"8 "]
);
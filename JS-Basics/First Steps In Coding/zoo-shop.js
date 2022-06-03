function shop(input){
    let priceDogs = Number(input[0]) * 2.50;
    let priceCats = Number(input[1]) * 4;
    let total = priceCats + priceDogs;
    console.log(total + ".")
}
shop(["5",
"4"]
);
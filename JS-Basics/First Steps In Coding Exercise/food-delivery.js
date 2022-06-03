function delivery(input){
    let priceChicken = Number(input[0]) * 10.35;
    let priceFish = Number(input[1]) * 12.40;
    let priceVegan = Number(input[2]) * 8.15;
    let priceDelivery = 2.50;
    let totalMenus = priceVegan + priceChicken + priceFish;
    let priceDessert = totalMenus * 0.2;
    let finish = totalMenus + priceDessert + priceDelivery;
    console.log(finish);
}
delivery(["2 ",
"4 ",
"3 "]
);
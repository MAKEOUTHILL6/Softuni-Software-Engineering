function order(product, count){
    price = 0;
    if(product === "coffee"){
        price = 1.50;
    }
    else if(product === "water"){
        price = 1;
    }
    else if(product === "coke"){
        price = 1.40;
    }
    else if(product === "snacks"){
        price = 2;
    }
    let res = price * count;
    console.log(res.toFixed(2));

}
order("water", 5);
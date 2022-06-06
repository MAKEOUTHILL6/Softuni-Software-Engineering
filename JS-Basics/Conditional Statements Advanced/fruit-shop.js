function shop(input){
    let product = input[0];
    let day = input[1];
    let quantity = input[2];
    let productPrice = 0;
    let isEnded = false;
    if(day === "Monday" || day === "Tuesday" || day === "Wednesday" || day === "Thursday" || day === "Friday"){
        if(product === "banana"){
            productPrice = quantity * 2.50;
        }
        else if(product === "apple"){
            productPrice = quantity * 1.20;
        }
        else if(product === "orange"){
            productPrice = quantity * 0.85;
        }
        else if(product === "grapefruit"){
            productPrice = quantity * 1.45;
        }
        else if(product === "kiwi"){
            productPrice = quantity * 2.70;
        }
        else if(product === "pineapple"){
            productPrice = quantity * 5.50;
        }
        else if(product === "grapes"){
            productPrice = quantity * 3.85;
        }
        else{
            console.log("error");
            isEnded = true;
        }
    }
    else if(day === "Saturday" || day === "Sunday"){
        if(product === "banana"){
            productPrice = quantity * 2.70;
        }
        else if(product === "apple"){
            productPrice = quantity * 1.25;
        }
        else if(product === "orange"){
            productPrice = quantity * 0.90;
        }
        else if(product === "grapefruit"){
            productPrice = quantity * 1.60;
        }
        else if(product === "kiwi"){
            productPrice = quantity * 3.00;
        }
        else if(product === "pineapple"){
            productPrice = quantity * 5.60;
        }
        else if(product === "grapes"){
            productPrice = quantity * 4.20;
        }
        else{
            console.log("error");
            isEnded = true;
            
        }
    }
    else{
        console.log("error");
        isEnded = true;
    }
    if(isEnded === false){
        console.log(productPrice.toFixed(2));
    }

}
shop(["tomato",
"Monday",
"0.5"])
;

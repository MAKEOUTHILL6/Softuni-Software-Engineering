function cinema(input){
    let movieType = input[0];
    let row = Number(input[1]);
    let column = Number(input[2]);
    let income = 0;

    if(movieType === "Premiere"){
        income = row * column * 12;
    }
    else if(movieType === "Normal"){
        income = row * column * 7.50;
    }
    else{
        income = row * column * 5;
    }

    console.log(income.toFixed(2) + " leva");
}
cinema(["Premiere",
"10",
"12"]);
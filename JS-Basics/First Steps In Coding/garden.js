function garden(input){
    let km = Number(input[0]);
    let price = (km * 7.61);
    let discount = price * 0.18;
    let final = price - discount;
    console.log(`The final price is: ${final} lv.`)
    console.log(`The discount is: ${discount} lv.`)

}
garden(["150"]);
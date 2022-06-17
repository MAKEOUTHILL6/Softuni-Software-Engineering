function vac(group, groupType, day){
    let totalPrice = 0;
    if(groupType === "Students"){
        if(day === "Friday"){
            if(group >= 30){
                totalPrice += group * 8.45 - (group * 8.45 * 0.15);
            }
            else{
                totalPrice += group * 8.45;
            }
        }
        else if(day === "Saturday"){
            if(group >= 30){
                totalPrice += group * 9.80 - (group * 9.80 * 0.15);
            }
            else{
                totalPrice += group * 9.80;
            }
        }
        else if(day === "Sunday"){
            if(group >= 30){
                totalPrice += group * 10.46 - (group * 10.46 * 0.15);
            }
            else{
                totalPrice += group * 10.46;
            }
        }
    }
    else if(groupType === "Business"){
        if(day === "Friday"){
            if(group >= 100){
                totalPrice += group * 10.90 - (group * 10.90 * 10);
            }
            else{
                totalPrice += group * 10.90;
            }
        }
        else if(day === "Saturday"){
            if(group >= 100){
                totalPrice += group * 15.60 - (group * 15.60 * 10);
            }
            else{
                totalPrice += group * 15.60;
            }
        }
        else if(day === "Sunday"){
            if(group >= 100){
                totalPrice += group * 16 - (group * 16 * 10);
            }
            else{
                totalPrice += group * 16;
            }
        }
    }
    else if(groupType === "Regular"){
        if(day === "Friday"){
            if(group >= 10 && group <= 20){
                totalPrice += group * 15 - (group * 15 * 0.05);
            }
            else{
                totalPrice += group * 15;
            }
        }
        else if(day === "Saturday"){
            if(group >= 10 && group <= 20){
                totalPrice += group * 20 - (group * 20 * 0.05);
            }
            else{
                totalPrice += group * 20;
            }
        }
        else if(day === "Sunday"){
            if(group >= 10 && group <= 20){
                totalPrice += group * 22.50 - (group * 22.50 * 0.05);
            }
            else{
                totalPrice += group * 22.50;
            }
        }
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}
vac(40,
    "Regular",
    "Saturday"
    );
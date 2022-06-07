function hotel(input){
    let month = input[0];
    let nights = Number(input[1]);
    let studioPrice = 0;
    let apartmentPrice = 0;

    switch(month){
        case "May":
        case "October":
            if(nights > 14){
                studioPrice = (50 - (50 * 0.3)) * nights;
                apartmentPrice = (65 - (65 * 0.1)) * nights
            }
            else if(nights > 7){
                studioPrice = (50 - (50 * 0.05)) * nights;
                apartmentPrice = 65 * nights
            };break;
        case "June":
        case "September":
            if(nights > 14){
                studioPrice = (75.20 - (75.20 * 0.2)) * nights;
                apartmentPrice = (68.70 - (68.70 * 0.1)) * nights
            }
            else if(nights > 7){
                studioPrice = 75.20 * nights;
                apartmentPrice = 68.70 * nights
            };break;
        case "July":
        case "August":
            studioPrice = 76 * nights
            if(nights > 14){
                apartmentPrice = (77 - (77 * 0.1)) * nights
            }
            else{
                apartmentPrice = 77 * nights
            };break;
    }
    console.log(`Apartment: ${apartmentPrice.toFixed(2)} lv.`);
    console.log(`Studio: ${studioPrice.toFixed(2)} lv.`);
}
hotel(["June",
"14"])
;

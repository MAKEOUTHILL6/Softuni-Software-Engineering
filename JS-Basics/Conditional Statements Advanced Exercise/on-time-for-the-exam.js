function exam(input){
    let hourExam = Number(input[0]);
    let minutesExam = Number(input[1]);
    let hourArrival = Number(input[2]);
    let minutesArrival = Number(input[3]);
    
    let timeExam = hourExam * 60 + minutesExam;
    let timeArrival = hourArrival * 60 + minutesArrival;
    let diff = Math.abs(timeArrival - timeExam);
    

    if(timeExam < timeArrival){
        console.log("Late");
        let h = Math.floor(diff / 60);
        let m = diff % 60;
        if(diff >= 60){
            if(m < 10){
                console.log(`${h}:0${m} hours after the start`);
            }
            else{
                console.log(`${h}:${m} hours after the start`);
            }
        }
        else{
            console.log(`${m} minutes after the start`);
        }
    }
    else if(timeExam === timeArrival || timeExam - timeArrival <= 30){
        console.log("On time");
        if(diff > 0){
            let m = diff % 60
            console.log(`${m} minutes before the start`)
        }
    }
    else{
        console.log("Early");
        let h = Math.floor(diff / 60);
        let m = diff % 60;
        if(h > 0){
            if(m < 10){
                console.log(`${h}:0${m} hours before the start`);
            }
            else{
                console.log(`${h}:${m} hours before the start`);
            }
        }
        else{
            console.log(`${m} minutes before the start`);
        }
    }
}
exam(["9",
"30",
"9",
"50"]);

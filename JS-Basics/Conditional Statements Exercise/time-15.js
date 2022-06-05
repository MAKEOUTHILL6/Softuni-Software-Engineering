function time(input){
    let hour = Number(input[0]);
    let minutes = Number(input[1]);
    let bonus = 15;
    if(bonus + minutes >59){
        minutes = (bonus + minutes) - 60;
        hour += 1;
        if(minutes < 10 && hour === 24){
            hour = 0
            console.log(`${hour}:0${minutes}`);
        }
        else{
            console.log(`${hour}:${minutes}`);
        }
    }
    else{
        console.log(`${hour}:${minutes + bonus}`);
    }
}
time(["12", "49"]);
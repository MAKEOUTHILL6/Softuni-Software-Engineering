function theatre(day, age){
    if(day === "Weekday"){
        if(age < 0){
            console.log("Error!")
        }
        else if(0<=age<=18){
            console.log(12+"$")
        }
        else if(18<age<=64){
            console.log(18+"$")
        }
        else if(64<age<=122){
            console.log(12+"$")
        }
    }
    else if(day === "Weekend"){
        if(age < 0){
            console.log("Error!")
        }
        else if(0<=age<=18){
            console.log(15+"$")
        }
        else if(18<age<=64){
            console.log(20+"$")
        }
        else if(64<age<=122){
            console.log(15+"$")
        }
    }
    else if(day === "Holiday"){
        if(age < 0){
            console.log("Error!")
        }
        else if(0<=age<=18){
            console.log(5 + "$")
        }
        else if(18<age<=64){
            console.log(12+"$")
        }
        else if(64<age<=122){
            console.log(10+"$")
        }
    }
}
theatre('Weekday', 
42
);
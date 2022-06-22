function solve(input){
    let arrDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    if(input <= arrDays.length){
        console.log(arrDays[input -1]);
    }else{
        console.log("Invalid day!")
    }
}
solve(6);
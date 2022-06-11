function salary(input){
    let count = Number(input[0]);
    let salary = Number(input[1]);
    let inputL = input.length
    for(let i=2; i<inputL; ++i){
        let currentTab = input[i]

        if(currentTab === "Facebook"){
            salary -= 150;
        }
        else if(currentTab === "Instagram"){
            salary -= 100;

        }
        else if(currentTab === "Reddit"){
            salary -= 50;
            
        }
        if(salary <=0){
            console.log("You have lost your salary.")
            break
        }
    }
    if(salary >0){
        console.log(salary)
    }
}
salary(["3",
"500",
"Facebook",
"Stackoverflow.com",
"softuni.bg"])

;

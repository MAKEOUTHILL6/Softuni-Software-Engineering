function grade(n){
    let desc;
    let formattedGrade = n.toFixed(2)
    if(n < 3){
        desc = "Fail";
        formattedGrade = 2
    }
    else if(n >= 3 && n < 3.50){
        desc = "Poor";
    }
    else if(n >= 3.50 && n < 4.50){
        desc = "Good";
    }
    else if(n >= 4.50 && n < 5.50){
        desc = "Very good";
    }
    else if(n >= 5.50){
        desc = "Excellent";
    }
    console.log(`${desc} (${formattedGrade})`);
}
grade(3.33);
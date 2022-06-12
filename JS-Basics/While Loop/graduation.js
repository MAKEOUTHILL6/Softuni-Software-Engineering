function graduation(input){
    let studentName = input[0];
    let classCount = 1;
    let index = 0;
    let sum = 0;
    let excluded = 0;
    let averageSum = 0;

    while(classCount <= 12){
        index++
        let current_grade = Number(input[index]);
        if(current_grade >= 4){
            sum += current_grade;
            classCount += 1;
        }
        else{
            excluded += 1;
            break;
        }
    }
    averageSum = sum / 12;
    if(excluded >= 1){
        console.log(`${studentName} has been excluded at ${classCount} grade`)
    }
    else{
        console.log(`${studentName} graduated. Average grade: ${averageSum.toFixed(2)}`)
    }
}
graduation(["Mimi", 
"5",
"6",
"5",
"6",
"5",
"6",
"6",
"2",
"3"])
;

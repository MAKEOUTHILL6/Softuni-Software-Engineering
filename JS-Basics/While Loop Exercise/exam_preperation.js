function exam(input){
    let index = 0;
    let badGrade = Number(input[index]);
    index++
    let currentProblem = input[index];
    index++;
    let badCount = 0;
    let sumGrade = 0;
    let problemCount = 0;
    let taskName = "";
    let isSuccessful = true;
    while(currentProblem !== "Enough"){
        taskName = currentProblem;
        let currentGrade = Number(input[index]);
        index++;

        if(currentGrade <= 4){
            badCount++
        }
        if(badCount === badGrade){
            isSuccessful = false;
            console.log(`You need a break, ${badCount} poor grades.`)
            break;
        }
        
        sumGrade += currentGrade;
        problemCount++;

        currentProblem = input[index];
        index++
    }
    if(isSuccessful){
        let avgScore = sumGrade / problemCount;
    console.log(`Average score: ${avgScore.toFixed(2)}`);
    console.log(`Number of problems: ${problemCount}`);
    console.log(`Last problem: ${taskName}`);
    }

}
exam(["3",
"Money",
"6",
"Story",
"4",
"Spring Time",
"5",
"Bus",
"6",
"Enough"]);

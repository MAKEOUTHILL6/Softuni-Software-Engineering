function triangle(num){
    for(let i=1; i<=num; i++){
        let printLine = ""
        for(let j=1; j<=i; j++){
            printLine += `${i} `;
        }
        console.log(printLine)
    }
    
}
triangle(3)
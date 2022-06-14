function comb(input){
    let totalCombs = 0;
    let num = Number(input[0]);
    for(let i=0; i<=num; i++){
        for(let j=0; j<=num; j++){
            for(let h=0; h<=num; h++){
                if(i + j + h === num){
                    totalCombs += 1
                }
            }
        }
    }
    console.log(totalCombs)
}
comb(["25"]);
function letters(num){
    num = Number(num);
    let letter = ""
    for(let i=0; i<num; i++){
        for(let j=0; j<num; j++){
            for(let h=0; h<num; h++){
                console.log(`${String.fromCharCode(97 + i)}${String.fromCharCode(97 + j)}${String.fromCharCode(97 + h)}`)
            }
        
        }
    }
}
letters("3");
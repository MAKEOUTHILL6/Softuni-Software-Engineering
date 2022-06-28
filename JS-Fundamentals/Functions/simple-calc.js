function calc(f, s, op){
    let res;
    switch(op){
        case "multiply": res = f * s;break;
        case "divide": res = f / s;break;
        case "add": res = f + s;break;
        case "subtract": res = f - s; break;
    }
    console.log(res)
}
calc(5,
    5,
    'multiply'
    );
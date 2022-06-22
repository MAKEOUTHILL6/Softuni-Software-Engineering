function solve(num, arr){
    let new_arr = []
    num = num -1 
    for(let i=num; num>=0; num--){
        new_arr.push(arr[num]);
    }
    console.log(new_arr.join(" "));
}
solve(3, [10, 20, 30, 40, 50]);
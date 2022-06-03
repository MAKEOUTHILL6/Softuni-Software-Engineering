function calculator(input){
    let deposited_sum = Number(input[0]);
    let months = Number(input[1]);
    let procent = Number(input[2]);
    let stacked_procent = deposited_sum * (procent / 100);
    let procentPerMonth = stacked_procent / 12;
    let sum = deposited_sum + months * procentPerMonth;
    console.log(sum)
}   
calculator(["2350",
"6 ",
"7 "]

)
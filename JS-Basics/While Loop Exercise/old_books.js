function books(input){
    let index = 1;
    let searchedBook = input[0];
    let current_books = input[index];
    let count = 0;
    let isFound = false;
    while(current_books !== "No More Books"){
        current_books = input[index];
        index++;
        if(current_books == searchedBook){
            isFound = true;
            break;
        }
        else if(current_books == "No More Books"){
            break;
        }
        else{
            count++
        }

    }

    if(isFound){
        console.log(`You checked ${count} books and found it.`)
    }
    else{
        console.log("The book you search is not here!")
        console.log(`You checked ${count} books.`)
    }

}   
books(["Bourne",
"True Story",
"Forever",
"More Space",
"The Girl",
"Spaceship",
"Strongest",
"Profit",
"Tripple",
"Stella",
"The Matrix",
"Bourne"])

;

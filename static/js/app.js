var heightInput = document.querySelector(".height-input-field");
var weightInput = document.querySelector(".weight-input-field");
var calculateButton = document.querySelector(".calculate");
var result = document.querySelector(".result");
var statement = document.querySelector(".result-statement");
var BMI, height, weight;

calculateButton.addEventListener("click", ()=>{

    height = heightInput.value;
    weight = weightInput.value;
    BMI = weight*700/(height*height); 
    result.innerText = BMI;

    if(BMI < 18.5){
        statement.innerText = "Underweight: Baja Peso";    
    }else if((BMI > 18.5) && (BMI < 24.9)){
        statement.innerText = "Normal";
    }else if((BMI > 25) && (BMI < 29.9 )){
        statement.innerText = "Overweight: Exceso de Peso";
    }else{
        statement.innerText = "Obese: Obeso";
    }
});
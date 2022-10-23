window.onload = () => {
	let button = document.querySelector("#btn");

	// Function for calculating BMI
	button.addEventListener("click", calculateBMI);
};

function calculateBMI() {
    //Getting Input for Height: In Centimeters
	let height = parseInt(document
			.querySelector("#height").value);
    //Getting Input for Weight: In Kilograms
	let weight = parseInt(document
			.querySelector("#weight").value);
    
	let result = document.querySelector("#result");
    // Insures that height and weight input is valid: No Letters
	if (height === "" || isNaN(height))
		result.innerHTML = 'Provide a valid Height!:  <span style="font-style:italic;"> Proporcione una Altura Válida!"</span>';

	else if (weight === "" || isNaN(weight))
		result.innerHTML = 'Provide a valid Weight!: <span style="font-style:italic;">Proporcione una Peso Válida!"</span>';

	else {
    //Calculates BMI upto 2 Decimals Spaces
		let bmi = (weight / ((height * height)
							/ 10000)).toFixed(2);
        // Based off Results: Classified as Underweight, Overweight, or Normal
		if (bmi < 18.6) result.innerHTML =
			`Under Weight: <span style="font-style:italic;"> Bajo Peso </span> : <span>${bmi}</span>`;

		else if (bmi >= 18.6 && bmi < 24.9)
			result.innerHTML =
				`Normal: <span style="font-style:italic;"> Normal </span> : <span>${bmi}</span>`;

		else result.innerHTML =
			`Over Weight : <span style="font-style:italic;"> Exceso de Peso </span>: <span>${bmi}</span>`;
	}
}


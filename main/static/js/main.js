$(document).ready(function(){
	// toastr pop ups
	
	quotes = ['"One should eat to live, not live to eat." --Moliere','"Food for the body is not enough. There must be food for the soul." --Dorothy Day','“One cannot think well, love well, sleep well, if one has not dined well.” ― Virginia Woolf','“Ask not what you can do for your country. Ask what’s for lunch.” ― Orson Welles','"Once, during Prohibition, I was forced to live for days on nothing but food and water."--W. C. Fields']
	var randomNumber 
	
	
	$('.centerText').hover(function(){
		randomNumber = Math.floor(Math.random() * 5);
		toastr.remove()
		toastr.info(quotes[randomNumber]);
	})
	// $('*nav')

});
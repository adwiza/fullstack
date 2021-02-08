advice_url = "https://api.adviceslip.com/advice"

$("#main-header").click(function() {

    $.getJSON(advice_url, function(data) {
      	console.log(data);
    });

    set_secret_message("Секретное послание");

});

function set_secret_message(msg) {
	p = $("#second-paragraph");

    p.html(msg)
    p.css("color", "red")
}

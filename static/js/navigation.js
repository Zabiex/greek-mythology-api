function redirectFigure(){
    window.location.pathname = "/figures/" +  document.getElementById("searchInput").value
    //No hacer asi
    //Cambiar el contenido de la pagina solo no redireciconar
}


document.onreadystatechange = function () {
    var state = document.readyState;
    if (state == 'interactive') {
        
    } 
    else if (state == 'complete') {
        var input = document.getElementById("searchInput");

        // Execute a function when the user releases a key on the keyboard
        input.addEventListener("keyup", function(event) {
            // Number 13 is the "Enter" key on the keyboard
            if (event.keyCode === 13) {
                // Cancel the default action, if needed
                event.preventDefault();
                // Trigger the button element with a click
                redirectFigure()
            }
        }); 
    }
}


$(function() {
    $(".toggle").on("click", function() {
        if ($(".nav-item").hasClass("active")) {
            $(".nav-item").removeClass("active");
            $(this).find("a").html("<i class='fas fa-bars'></i>");
            $(this).css("margin-left","auto")
        } else {
            $(".nav-item").addClass("active");
            $(this).find("a").html("<i class='fas fa-times'></i>");
        }
    });
});


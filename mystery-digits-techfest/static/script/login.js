function onNextButtonClick() {
    var phone = $('#phone').val();
    var name = $('#name').val();

    $.ajax({
        type: 'POST',
        url: '/getDetails', 
        data: { phone: phone, name: name },
        /**success: function(response) {
            $("#user-info-form").fadeOut(500, function() {
                $("#continue-with-google").removeClass("hidden").hide().fadeIn(500);
            });
        },
        error: function(error) {
            $("#error").text("Error or Number Already exists!");
        }**/
    });
}
function login(){
    var r=document.getElementById("rules");
    var l=document.getElementById("login");

    l.style.visibility="visible"
    r.style.transform="translateX(100%)";
    setTimeout(function (){r.style.display="none"},500);
    
}
function opt(le,wi,bl,bh,h,i){
    var l=document.getElementById("line").style;

    l.left=le;
    l.width=wi;
    document.getElementById("home").style.color=bh;
    document.getElementById("leadbod").style.color=bl;
    document.getElementById(h).style.display="block";
    document.getElementById(i).style.display="none";
    setTimeout(function(){
        document.getElementById(h).style.opacity="1";
    document.getElementById(i).style.opacity="0";
    },100)
}
$(document).ready(function(){
    // Function to get and display leaderboard
    function getLeaderboard() {
        $.ajax({
            type: 'GET',
            url: '/getL',
            success: function(response){
                console.log("Success. Response:", response);

                // Clear existing leaderboard rows
                $("#leaderboardBody").empty();

                // Check if the response is an array
                if (Array.isArray(response)) {
                    // Add new rows to the leaderboard table
                    $.each(response, function(index, entry) {
                        // Accessing the inner array elements
                        $("#leaderboardBody").append(
                            "<tr><td>" + entry[0] + "</td>" +
                            "<td>" + entry[1] + "</td>" +
                            "<td>" + entry[3] + "</td>" +
                            "<td>" + entry[4] + "</td>" +
                            "<td><img src='" + entry[5] + "' alt='Profile' class='profile'></td></tr>"
                        );
                    });
                } else {
                    console.error("Invalid response format. Expected an array.");
                }
            },
            error: function(error){
                console.error("Error fetching leaderboard: ", error);
            }
        });
    }

    // Call the function to get and display the leaderboard on page load
    getLeaderboard();

    // Set up interval to update leaderboard every 2 seconds
    setInterval(function() {
        getLeaderboard();
    }, 2000);

    // Submit form function remains unchanged
    $("#gameForm").submit(function(e){
        e.preventDefault();

        var val = $("#val").val();
        $.ajax({
            type: 'POST',
            url: '/game',
            data: { val: val },
            success: function(response){
                if (response.continue === "false"){
                    window.location = "/ended";
                }
                document.getElementById("congrats").style.display="block";
                document.getElementById("overlay").style.display="block";
                document.getElementById("levels").innerHTML=level;
                $("#val").val("");
                $("#profileImage").fadeOut(300, function() {
                    $(this).attr("src", response.filepath).fadeIn(300);
                });

                $("#level1").fadeOut(300, function() {
                    $(this).text(response.level).fadeIn(300);
                });

                $("#tries").fadeOut(300, function() {
                    $(this).text(response.tries).fadeIn(300);
                });
            },
            error: function(error){
                if (error.responseJSON.continue === "false"){
                    document.body.innerHTML = '';

                    window.location = "/ended";
                }
                $("#error").fadeOut(300, function() {
                    document.getElementById("error").style.display="block";
                    document.getElementById("overlay").style.display="block";
                });
                if (error.responseJSON && error.responseJSON.tries) {
                    $("#tries").fadeOut(300, function() {
                        $(this).text(error.responseJSON.tries).fadeIn(300);
                    });
                }
            }
        });
    });
});
function left(){
    var n=document.getElementById("val").value.length + 1; 
    var l=level.innerHTML;
    l=l[0];
    var left=l-n;
        console.log(left)
        
}
function zoom(){
    var h=document.getElementById("image").offsetHeight;
    setTimeout(function(){
        document.getElementById("profileImage").style.width="600vw";
        document.getElementById("profileImage").style.height="400vw";
    },100);

    document.getElementById("image").style.height=h+"px"
    console.log(h);
    
}
function overlay(){
    document.getElementById("congrats").style.display="none";
    document.getElementById("error").style.display="none";
        document.getElementById("overlay").style.display="none";
        document.getElementById("profileImage").style.width="100%";
        document.getElementById("profileImage").style.height="fit-content";
}
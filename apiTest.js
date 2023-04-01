let baseUrl = "https://trevonino.pythonanywhere.com/api/"
testData = [];
infoData = [];

async function searchPlayerName() {
    newURL = baseUrl + 'player?'
    fname = $('#searchFirstName').val();
    lname = $('#searchLastName').val();

    document.getElementById("loader").style.display = "block";

    if (fname != '' && lname != '') {
        newURL += 'fname=' + fname + "&lname=" + lname;
    }
    else if (fname != '') {
        newURL += 'fname=' + fname + "%";
    }
    else if (lname != '') {
        newURL += 'lname=' + lname + "%";
    }
    $("[id^=result]").remove();
    const response = await fetch(newURL);
    var data = await response.json();
    if (data.length > 0) {
        for (i = 0; i < data.length; i++) {
            textID = "result" + i;
            document.getElementById("searchResults").innerHTML +=
                "<p id='" + textID + "' onclick='getStats(" + data[i].id + ");'>" + data[i].full_name + "</p>";
        }
    }
    testData = data;
    console.log(testData);
    document.getElementById("loader").style.display = "none";
}

async function getStats(playerID){
    document.getElementById("loader").style.display = "block";
    newURL = baseUrl + 'info?id=' + playerID;
    const response = await fetch(newURL);
    var data = await response.json();
    infoData = data;
    alertMessage = "Full Name: " + infoData[0] + "\nBirthday: " + infoData[1].slice(0,10) + "\nTeam: " + infoData[2] + ", " + infoData[3] + "\nHeight: " + infoData[4] + "\nWeight: " + infoData[5] + "\nPosition: " + infoData[6] + "\nPlayed From: " + infoData[7] + " - " + infoData[8] + "\nDrafted Round: " + infoData[9] + "\nDrafted Number: " + infoData[10];
    document.getElementById("loader").style.display = "none";
    window.alert(alertMessage);
}
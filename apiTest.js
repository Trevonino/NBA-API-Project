let baseUrl = "https://trevonino.pythonanywhere.com/api/"
testData = [];

async function searchPlayerName() {
    newURL = baseUrl + 'player?'
    fname = $('#searchFirstName').val();
    lname = $('#searchLastName').val();

    document.getElementById("loader").style.display = "block";

    if (fname != '' && lname != '') {
        newURL += 'fname=' + fname + "&lname=" + lname;
    }
    else if (fname != '') {
        newURL += 'fname=' + fname;
    }
    else if (lname != '') {
        newURL += 'lname=' + lname;
    }
    $("[id^=result]").remove();
    const response = await fetch(newURL);
    var data = await response.json();
    if (data.length > 0) {
        for (i = 0; i < data.length; i++) {
            textID = "result" + i;
            document.getElementById("searchResults").innerHTML +=
                "<p id='" + textID + "'>" + data[i].full_name + "</p>";
        }
    }
    testData = data;
    console.log(testData);
    document.getElementById("loader").style.display = "none";
}
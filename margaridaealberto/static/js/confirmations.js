function showFoodRestrictionsInput(){
    var foodRestrictions = document.getElementById("food_restriction");
    foodRestrictions.style.display = "flex";
}

function hideFoodRestrictionsInput(){
    var foodRestrictions = document.getElementById("food_restriction");
    foodRestrictions.style.display = "none";
}

function generateConfirmationsCSV(){
    $.getJSON('/api/to_csv/confirmation',
        function(data) {
            downloadFile('/static/data/csv/confirmation.csv');
    });
}

function downloadFile(filename) {
    // Create a link and set the URL using `createObjectURL`
    const link = document.createElement("a");
    link.download = 'confirmations.csv';
    link.style.display = "none";
    link.href = filename

    // It needs to be added to the DOM so it can be clicked
    document.body.appendChild(link);
    link.click();

    // To make this work on Firefox we need to wait
    // a little while before removing it.
    setTimeout(() => {
        URL.revokeObjectURL(link.href);
        link.parentNode.removeChild(link);
    }, 0);
}
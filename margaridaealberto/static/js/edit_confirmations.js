function deleteConfirmation(ele){
    let url = api_url.replace(/.$/, '') + ele.getAttribute('data-confirmation_id');
    $.getJSON(url,function(data){
    });
    let row = ele.parentElement.parentElement
    row.parentNode.removeChild(row);
}
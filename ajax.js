function ajax_get(url, succ, err) {
    $.ajax({
        type : "GET",
        dataType : "json",
        contentType : "text/json",
        url: url,
        success: function(data) {
            succ(data);
        },
        error: function(data) {
            err(data);
        },
    });
}

function ajax_post(url, data, succ, err) {
    $.ajax({
        type : "POST",
        dataType : "json",
        contentType : "text/json",
        url: url,
        data : JSON.stringify(data),
        success: function(data) {
            succ(data);
        },
        error: function(data) {
            err(data);
        },
    });
}

function ajax_put(url, data, succ, err) {
    $.ajax({
        type : "PUT",
        dataType : "json",
        contentType : "text/json",
        url: url,
        data : JSON.stringify(data),
        success: function(data) {
            succ(data);
        },
        error: function(data) {
            err(data);
        },
    });
}

function ajax_delete(url, succ, err) {
    $.ajax({
        type : "DELETE",
        dataType : "json",
        contentType : "text/json",
        url: url,
        success: function(data) {
            succ(data);
        },
        error: function(data) {
            err(data);
        },
    });
}


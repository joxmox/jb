var id = 0;

$(document).ready(function() {
    $("#title").text('Hej hopp');

    $("#crd1").addClass("red");
    $("#val1").text('J');
    $("#sut1").html('&hearts;');
    $("#val2").text('J');
    $("#sut2").html('&hearts;');

    $("#val3").text('K');
    $("#sut3").html('&spades;');
    $("#val4").text('K');
    $("#sut4").html('&spades;');

    start_game();

});

function start_game() {
    var url = '/api/game';
    var data = {
        'user' : 'apa'
    }
    ajax_post(url, data, start_succ, start_fail);
}

function start_succ(data) {
    console.log(data);
    id = data.id;
    var url = '/api/game/' + id;
    ajax_get(url, parse_next, start_fail);
}

function parse_next(data) {
    console.log('yes');
    console.log(data);
}

function start_fail(data) {
    console.log("urk");
    console.log(data);
}

function show_deck() {
    deck = $("#deck");
    for (sut=0; sut<4; sut++) {
        apa = $("<div>").addClass("eol");
        for (val=0; val<13; val++) {
            create_card(sut, val, apa);
        }
        deck.append(apa);
    }
}

function create_card(sut, val, div) {
    if (sut == 0) {
        sym = "&#x2663";
        col = "grn";
    } else if (sut == 1) {
        sym = "&#x2666";
        col = "yel";
    } else if (sut == 2) {
        sym = "&#x2665";
        col = "red";
    } else if(sut == 3) {
        sym = "&#x2660";
        col = "blk";
    }
    if (val == 8) {
        xyz = "T";
    } else if (val == 9) {
        xyz = "J";
    } else if (val == 10) {
        xyz = "Q";
    } else if (val == 11) {
        xyz = "K";
    } else if (val == 12) {
        xyz = "A";
    } else {
        xyz = val + 2;
    }
    front_val = $("<div>").addClass("val").html(xyz);
    front_sut = $("<div>").addClass("sut").html(sym);
    back_val = $("<div>").addClass("val").html(xyz);
    back_sut = $("<div>").addClass("sutr").html(sym);
    front = $("<div>").append(front_val).append(front_sut);
    back = $("<div>").addClass("rot").append(back_val).append(back_sut);
    card = $("<div>").addClass("kaka").addClass(col).append(front).append(back);
    div.append(card);
}



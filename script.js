var id = 0;

var dispatch = {
    'deal_info' : read_dealinfo,
    'show_hands' : show_hands,
    'part_hand' : show_partner,
    'do_bid' : do_bid
}


$(document).ready(function() {
    $("#title").text('Hej hopp');
    $("#start").click(function() {
        start_game();
    });
});

function start_game() {
    var num = $("#numin").val();
    var url = '/api/game';
    var data = {
        'user' : 'apa',
        'num' : num
    }
    ajax_post(url, data, start_succ, start_fail);
}

function start_succ(data) {
    console.log(data);
    id = data.id;
    var url = '/api/game/' + id;
    ajax_get(url, parse_next, start_fail);
}

function get_next() {
    var url = '/api/game/' + id;
    ajax_get(url, parse_next, start_fail);
}

function parse_next(data) {
    console.log('parse and dispatch: ' + data.action);
    console.log(data);
    var action = data.action;
    if (action in dispatch) {
        dispatch[action](data);
        setTimeout(get_next, 100);
    } else {
        if (action != 'end_game') {
            console.log('Invalid action: ' + action);
        }
    }
}

function start_fail(data) {
    console.log("urk");
    console.log(data);
}

function read_dealinfo(data) {
    $("#id").text(data.id);
    $("#num").text(data.info.num);
    $("#zone").text(data.info.zone);
    $("#dealer").text(data.info.dealer);
}

function show_hand(hand, player) {
    var arr = hand.cards.split(' ');
    console.log(arr);
    for (i in arr) {
         console.log(arr[i]);
        var card = create_card(arr[i]);
        player.append(card);
    }
    var hcp = $("<div>").addClass("hcp").text('hcp: ' + hand.hcp);
    player.append(hcp);
}

function show_hands(data) {
    var hands = data.hands;
    console.log("hands: ");
    console.log(hands);
//    var dirs = ['south', 'west', 'north', 'east'];
    var dirs = ['south', 'north'];
    var suits = ['s', 'h', 'd', 'c'];
    for (i in dirs) {
        var dir = dirs[i];
        for (j in suits) {
            var suit = suits[j];
            var player = "#" + dir + "_" + suit;
            var div = $(player);
            var data = hands[dir].suited[suit];
            for (k in data) {
                var card = create_card(data[k], suit);
                $(player).append(card);
            }
        }
    }
}

function show_partner(data) {
    show_hand(data.hand, $("#my_partner"));
}

function do_bid(data) {
    var bid = data.bid;
    var name = bid.name;
    var symb = bid.symb;
    var text = bid.text;
    var color = bid.color;
    var bidder = "#" + data.bidder + "bid";
    var box = $(bidder);
    var apa = $("<span>").html(symb).addClass(color);
    box.append($("<br>")).append(apa);
}
        

function create_card(val, sut) {
//    var tmp = txt.split('');
//    var val = tmp[0];
//    var sut = tmp[1];
    var sym;
    var col;
    if (sut == 'c') {
        sym = "&#x2663";
        col = "grn";
    } else if (sut == 'd') {
        sym = "&#x2666";
        col = "yel";
    } else if (sut == 'h') {
        sym = "&#x2665";
        col = "red";
    } else if(sut == 's') {
        sym = "&#x2660";
        col = "blk";
    }
    var front_val = $("<div>").addClass("val").html(val);
    var front_sut = $("<div>").addClass("sut").html(sym);
    var back_val = $("<div>").addClass("val").html(val);
    var back_sut = $("<div>").addClass("sutr").html(sym);
    var front = $("<div>").append(front_val).append(front_sut);
    var back = $("<div>").addClass("rot").append(back_val).append(back_sut);
    var card = $("<div>").addClass("kaka").addClass(col).append(front).append(back);
    return card;
}

var total_price =0;
var total_ticket_num = 0;
var range_select_css = new Array();
range_select_css[0] = 'none';
range_select_css[1] = 'all';
var select_count = 0;
var img = new Array();
img[0] = new Image();
img[0].src = "/static/images/seat.png";
img[1] = new Image();
img[1].src = "/static/images/seat1.png";
var list = new Array();
var seat_list_size = 0;


function seat_get_func(){
	var x = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
	var str = document.getElementById("span_seat_list").getAttribute("value");
	var seat_list = str.split(',');
	console.log(seat_list);
	for(var i = 0;i<7;i++){
		for(var j = 0;j<7;j++){
			var str = x[i]+'-'+j;
			judge = seat_list.indexOf(str);
			if(judge == -1){
				document.writeln('<img id="'+str+'" onclick="change_IMG(\'' + str + '\')" src ="/static/images/seat.png">&nbsp;&nbsp;&nbsp;&nbsp;');
			}else{
				document.writeln('<img id="'+str+'" src ="/static/images/seat3.png">&nbsp;&nbsp;&nbsp;&nbsp;');
			}
		}
		document.writeln('<br><br>');
	}
}

window.onload = function(){
	
	const adult = 1800;
	const high_school = 1500;
	const prime_middle_school = 1000;
	const child = 600;
	
	var total_price_id = document.getElementById('id_total_price');
	var total_price_text = document.getElementById('total_price_text');

	var ticket_id1 = document.getElementById("ticket_id1");
	var ticket_id2 = document.getElementById("ticket_id2");
	var ticket_id3 = document.getElementById("ticket_id3");
	var ticket_id4 = document.getElementById("ticket_id4");
	var ticket_id5 = document.getElementById("ticket_id5");
	
	var count_up_btn1   = document.getElementById("btn_count_up1");
	var count_down_btn1 = document.getElementById("btn_count_down1");
	var reset_btn1      = document.getElementById("btn_reset1");
	
	var count_up_btn2   = document.getElementById("btn_count_up2");
	var count_down_btn2 = document.getElementById("btn_count_down2");
	var reset_btn2      = document.getElementById("btn_reset2");
	
	var count_up_btn3   = document.getElementById("btn_count_up3");
	var count_down_btn3 = document.getElementById("btn_count_down3");
	var reset_btn3      = document.getElementById("btn_reset3");
	
	var count_up_btn4   = document.getElementById("btn_count_up4");
	var count_down_btn4 = document.getElementById("btn_count_down4");
	var reset_btn4      = document.getElementById("btn_reset4");
	
	var count_up_btn5   = document.getElementById("btn_count_up5");
	var count_down_btn5 = document.getElementById("btn_count_down5");
	var reset_btn5      = document.getElementById("btn_reset5");
	
	var count_value = 0;
	var count_value1 = 0;
	var count_value2 = 0;
	var count_value3 = 0;
	var count_value4 = 0;
	var count_value5 = 0;
	
	count_up_btn1.onclick = function(){
		count_value1 += 1;
		total_ticket_num += 1;
		ticket_id1.value=count_value1;
		ticket_id1.setAttribute("value",count_value1);
		total_price += adult;
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット1 枚数　　"+count_value1);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	count_down_btn1.onclick = function(){
		if(count_value1 >= 1){
			count_value1-=1;
			total_ticket_num -= 1;
			total_price -= adult;
		}else{
			count_value1 =0;
		}
		document.form.ticket1.value=count_value1;
		document.form.ticket1.setAttribute("value",count_value1);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット1 枚数　　"+count_value1);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	reset_btn1.onclick = function(){
		total_price -= adult * count_value1;
		total_ticket_num -= count_value1;
		count_value1=0;
		document.form.ticket1.value=count_value1;
		document.form.ticket1.setAttribute("value",count_value1);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット1 枚数　　"+count_value1);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	
	count_up_btn2.onclick = function(){
		count_value2 += 1;
		total_ticket_num += 1;
		document.form.ticket2.value=count_value2;
		document.form.ticket2.setAttribute("value",count_value2);
		total_price += high_school;
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット2 枚数　　"+count_value2);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	count_down_btn2.onclick = function(){
		if(count_value2 >= 1){
			count_value2-=1;
			total_ticket_num -= 1;
			total_price -= high_school;
		}else{
			count_value2 =0;
		}
		document.form.ticket2.value=count_value2;
		document.form.ticket2.setAttribute("value",count_value2);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット2 枚数　　"+count_value2);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	reset_btn2.onclick = function(){
		total_price -= high_school * count_value2;
		total_ticket_num -= count_value2;
		count_value2=0;
		document.form.ticket2.value=count_value2;
		document.form.ticket2.setAttribute("value",count_value2);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット2 枚数　　"+count_value2);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	
	count_up_btn3.onclick = function(){
		count_value3 += 1;
		total_ticket_num += 1;
		document.form.ticket3.value=count_value3;
		document.form.ticket3.setAttribute("value",count_value3);
		total_price += prime_middle_school;
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット3 枚数　　"+count_value3);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	count_down_btn3.onclick = function(){
		if(count_value3 >= 1){
			count_value3-=1;
			total_ticket_num -= 1;
			total_price -= prime_middle_school;
		}else{
			count_value3 =0;
		}
		document.form.ticket3.value=count_value3;
		document.form.ticket3.setAttribute("value",count_value3);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット3 枚数　　"+count_value3);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	reset_btn3.onclick = function(){
		total_price -= prime_middle_school * count_value3;
		total_ticket_num -= count_value3;
		count_value3=0;
		document.form.ticket3.value=count_value3;
		document.form.ticket3.setAttribute("value",count_value3);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット3 枚数　　"+count_value3);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	
	count_up_btn4.onclick = function(){
		count_value4 += 1;
		total_ticket_num += 1;
		document.form.ticket4.value=count_value4;
		document.form.ticket4.setAttribute("value",count_value4);
		total_price += prime_middle_school;
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット4 枚数　　"+count_value4);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	count_down_btn4.onclick = function(){
		if(count_value4 >= 1){
			count_value4-=1;
			total_ticket_num -= 1;
			total_price -= prime_middle_school;
		}else{
			count_value4 =0;
		}
		document.form.ticket4.value=count_value4;
		document.form.ticket4.setAttribute("value",count_value4);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット4 枚数　　"+count_value4);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	reset_btn4.onclick = function(){
		total_price -= prime_middle_school * count_value4;
		total_ticket_num -= count_value4;
		count_value4=0;
		document.form.ticket4.value=count_value4;
		document.form.ticket4.setAttribute("value",count_value4);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット4 枚数　　"+count_value4);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	
	count_up_btn5.onclick = function(){
		count_value5 += 1;
		total_ticket_num += 1;
		document.form.ticket5.value=count_value5;
		document.form.ticket5.setAttribute("value",count_value5);
		total_price += child;
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット5 枚数　　"+count_value5);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	count_down_btn5.onclick = function(){
		if(count_value5 >= 1){
			count_value5-=1;
			total_ticket_num -= 1;
			total_price -= child;
		}else{
			count_value5 = 0;
		}
		document.form.ticket5.value=count_value5;
		document.form.ticket5.setAttribute("value",count_value5);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット5 枚数　　"+count_value5);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
	reset_btn5.onclick = function(){
		total_price -= child * count_value5;
		total_ticket_num -= count_value5;
		count_value5=0;
		document.form.ticket5.value=count_value5;
		document.form.ticket5.setAttribute("value",count_value5);
		total_price_text.innerHTML = `合計金額 : ${total_price}`;
		total_price_id.setAttribute("value",total_price);
		console.log("チケット5 枚数　　"+count_value5);
		console.log("合計金額  　　　　"+total_price);
		console.log("合計枚数  　　　　"+total_ticket_num);
	}
}

function change_css(){
	var parchase_css_style = document.getElementById("purchase_div");
	var seat_css_style = document.getElementById("seat_div");
	if(select_count == 0){
		parchase_css_style.style.pointerEvents = "none";
		parchase_css_style.style.opacity = "0.3";
		seat_css_style.style.opacity = "";
		seat_css_style.style.pointerEvents = "";
		select_count++;
	}else{
		parchase_css_style.style.pointerEvents = "";
		parchase_css_style.style.opacity = "";
		seat_css_style.style.opacity = "0.3";
		seat_css_style.style.pointerEvents = "none";
		console.log("処理実行"+list);
		console.log("処理実行"+list);
		console.log("処理実行"+list);
		for(var i = 0;i < list.length;){
			var str = list[0];
			change_IMG(str);
			console.log(str);
		}
		//console.log("消す前 "+list);
		//list.length=0;
		//console.log("消した後 "+list);
		select_count = 0;
	}
}

function change_css_init(){
    var seat_css_style = document.getElementById("seat_div");
    seat_css_style.style.opacity = "0.3";
    seat_css_style.style.pointerEvents = "none";
}


function change_IMG(x){
    console.log("引数を表示します！"+x);
    var judge = list.indexOf(x);
    if(judge == -1){
        if(seat_list_size >= total_ticket_num){
            console.log("チケット枚数 "+total_ticket_num);
            console.log("選択座席数"+seat_list_size);
        }else{
            list.push(x);
            document.getElementById(x).src=img[1].src;
        }
    }else{
        list.splice(judge,1);
        document.getElementById(x).src=img[0].src;
    }
    document.getElementById("seat_list").setAttribute("value",list);
    seat_list_size = list.length;
    console.log("座席一覧 "+list);
    console.log("選択座席数 "+seat_list_size);
}

function check_seat_func(){
    if(total_ticket_num <=0 ){
        alert("座席を選択して下さい")
        return false;
    }else if(total_ticket_num != seat_list_size){
        alert(`${total_ticket_num}つの座席を選択して下さい`)
        return false;
    }else{
        return true;
    }
}
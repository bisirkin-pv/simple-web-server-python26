/* Заполнение регионами ComboBox */
function loadregion(){
    var region = new XMLHttpRequest();
    var objSel = document.getElementById("region");
    region.open("POST", '/comment/getregion/', true);
        region.onreadystatechange = function () {
        var done = 4;
        var ok = 200;
        if (region.readyState === done && region.status === ok){
        var date = JSON.parse(region.responseText);
            for (var i = 0; i < date.name.length; i++) {
                objSel.options[objSel.options.length] = new Option(date.name[i][1], date.name[i][0]);
            }
        }
        };
    region.send();
}

/* Заполнение городами ComboBox */
function selectcity() {
    var region = document.getElementById("region").value;
    var city_sel = document.getElementById("city");
    if (region == 'not'){
        city_sel.options.length = 0;
        city_sel.options[city_sel.options.length] = new Option('Выберите город', 'not');
    }
    else {
        var city = new XMLHttpRequest();
        city_sel = document.getElementById("city");
        city_sel.options.length = 0;
        city.open("POST", '/comment/getcity/', true);
        city.onreadystatechange = function () {
            var done = 4;
            var ok = 200;
        if (city.readyState === done && city.status === ok){
            var date = JSON.parse(city.responseText);
            for (var i = 0; i < date.name.length; i++) {
                city_sel.options[city_sel.options.length] = new Option(date.name[i][1], date.name[i][0]);
            }
        }
        };
        var body = 'city=' + encodeURIComponent(document.getElementById("region").value);
        city.send(body);
    }
}

/* отправка данных на сервер для сохранения комментрия*/
function save() {
    var surname = document.getElementById("surname"),
    firstName = document.getElementById("firstname"),
    patronymic = document.getElementById("patronymic"),
    email = document.getElementById("email"),
    phone = document.getElementById("phone"),
    comment = document.getElementById("comment"),
    city = document.getElementById("city"),
    empty = [],
    error = [],
    re,
    testResult;
    if (surname.value == ''){
        surname.setAttribute("class", "red");
        empty.push('1')
    }else{
        surname.removeAttribute("class", "red");
    }
    if (firstName.value == ''){
        firstName.setAttribute("class", "red");
        empty.push('1')
    }else{
        firstName.removeAttribute("class", "red");
    }
    if (comment.value == ''){
        comment.setAttribute("class", "red");
        empty.push('1')
    }else{
        comment.removeAttribute("class", "red");
    }

    if (email.value != '') {
        re = /^[_a-zA-Z-\.0-9]+@[\w-]+\.[a-zA_Z]{2,4}$/i;
        testResult = re.test(email.value);
        if (!testResult) {
            email.setAttribute("class", "orange");
            error.push('1')
        }
        else{
            email.removeAttribute("class", "orange")
        }
    }

    if (phone.value != '') {
        re = /^([(][\d]{3,5}[)][\d+]{5,7})/i;
        testResult = re.test(phone.value);
        if (!testResult) {
            phone.setAttribute("class", "orange");
            error.push('1')
        }
        else{
            phone.removeAttribute("class", "orange")
        }
    }

    if (empty.length != 0){
         alert('Заполните выделенные поля.');
    } else
        if(error.length !=0){
            alert('Проверьте правильность заполнения выделенных полей.');
        }
        else{
            save = new XMLHttpRequest();
            save.open('POST', '/comment/save/', true);
            var body = 'surname=' + encodeURIComponent(surname.value)
            + '&firstName=' + encodeURIComponent(firstName.value)
            + '&patronymic=' + encodeURIComponent(patronymic.value)
            + '&email=' + encodeURIComponent(email.value)
            + '&phone=' + encodeURIComponent(phone.value)
            + '&comment=' + encodeURIComponent(comment.value)
            + '&code_city=' + encodeURIComponent(city.value);
            save.onreadystatechange = function() {
            if (save.readyState == 4) {
                if(save.status == 200) {

                    alert(save.responseText);
                    setTimeout(window.location.reload.bind(window.location.href = '/comment/'), 500);
                }
            }

            };
            save.send(body);
        }
}

/* Функция удаления комметрия по id */
function deleteComment(id){
    var del = new XMLHttpRequest(),
	body = 'id=' + encodeURIComponent(id);

    del.open('POST', '/view/delcoment/', true);
	del.onreadystatechange = function() {
		if (del.readyState == 4) {
			if(del.status == 200) {
                window.location.reload();
			}
		}

	};
    del.send(body);
}

/* Наполнение таблицы для просмотра комментариев */
function view(){
     var region = new XMLHttpRequest();
    region.open("POST", '/view/getviewcoment/', true);
        region.onreadystatechange = function () {
        var done = 4;
        var ok = 200;
        if (region.readyState === done && region.status === ok){
            var date = JSON.parse(region.responseText),
                block = document.getElementById('block_table');
                block.innerHTML = date.name;
        }
        };
    region.send();
}

/* Заполенние таблицы регионов с комментариями больше 5 */
function statcomentfive(){
    var region = new XMLHttpRequest();
    region.open("POST", '/stat/statcomentfive/', true);
        region.onreadystatechange = function () {
        var done = 4;
        var ok = 200;
        if (region.readyState === done && region.status === ok){
        var date = JSON.parse(region.responseText);
            var table = document.getElementById('TableStat5');
            for (var i = 0; i < date.name.length; i++) {
                var newRow=table.insertRow(1);
                var newCell = newRow.insertCell(0);
                newCell.innerHTML=date.name[i][0];
                newCell = newRow.insertCell(1);
                newCell.innerHTML=date.name[i][1];
            }
        }
        };
    region.send();
}

/* Заполнение таблицы комментариев по регионам */
function statcomentall(){
        var region = new XMLHttpRequest();
    region.open("POST", '/stat/statcomentall/', true);
        region.onreadystatechange = function () {
        var done = 4;
        var ok = 200;
        if (region.readyState === done && region.status === ok){
        var date = JSON.parse(region.responseText);
            var table = document.getElementById('TableStat');
            for (var i = 0; i < date.name.length; i++) {
                var newRow=table.insertRow(1);
                var newCell = newRow.insertCell(0);
                newCell.innerHTML=date.name[i][1];
                newCell.setAttribute("id", date.name[i][0]);
                newCell.setAttribute("class", "point");
                newCell.addEventListener("click", statcomentcity);
                newCell = newRow.insertCell(1);
                newCell.innerHTML=date.name[i][1];
                newCell.setAttribute("id", date.name[i][0]);
                newCell.setAttribute("class", "point");
                newCell.addEventListener("click", statcomentcity);
                newCell.innerHTML=date.name[i][2];
            }
        }
        };
    region.send();
}

/* Заполнение таблицы комментариев по городам */
function statcomentcity() {
    var region = new XMLHttpRequest();
    var region_id = this.id;
    region.open("POST", '/stat/statcomentcity/', true);
    region.onreadystatechange = function () {
        var done = 4;
        var ok = 200;
        if (region.readyState === done && region.status === ok) {
            var date = JSON.parse(region.responseText);
            var div = document.getElementById("insert");
            while (div.firstChild) {
                div.removeChild(div.firstChild);
            }
            for (var i = 0; i < date.name.length; i++) {
                var span = document.createElement('span');
                span.setAttribute("class", "insert_span");
                span.innerHTML  = "<span id='label_city'>Город:</span> " + date.name[i][0] + "<br> <span id='label_comment'>Количество комментариев: </span>" + date.name[i][1];
                div.appendChild(span);
            }
        }
    };
    var body = 'region_id=' + encodeURIComponent(region_id);
    region.send(body);
}

function setActiveMenu(){
    var urlPage = window.location.pathname,
        nameId = '';
    if(urlPage == '/'){
        nameId = 'menu_home';
    }else{
        nameId = 'menu_' + urlPage.replace('/','').replace('/', '');
    }
    var nav = document.getElementById("nav_ul");
    for (var i=0; i< nav.length; i++) {
        nav[i].removeAttribute('class','active');
        console.log(nav[i]);
    }
    console.log(nameId);
    var elem = document.getElementById(nameId);
    elem.setAttribute("class", "active");
}
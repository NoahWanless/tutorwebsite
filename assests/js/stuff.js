var checkList = document.getElementById('list1');
checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
  console.log("click event")
  if (checkList.classList.contains('visible'))
    checkList.classList.remove('visible');
  else
    checkList.classList.add('visible');
}

var checkList_tue = document.getElementById('list2');
checkList_tue.getElementsByClassName('anchor')[0].onclick = function(evt) {
  console.log("click event")
  if (checkList_tue.classList.contains('visible'))
    checkList_tue.classList.remove('visible');
  else
    checkList_tue.classList.add('visible');
}

var checkList_wed = document.getElementById('list3');
checkList_wed.getElementsByClassName('anchor')[0].onclick = function(evt) {
  console.log("click event")
  if (checkList_wed.classList.contains('visible'))
    checkList_wed.classList.remove('visible');
  else
    checkList_wed.classList.add('visible');
}

var checkList_thr = document.getElementById('list4');
checkList_thr.getElementsByClassName('anchor')[0].onclick = function(evt) {
  console.log("click event")
  if (checkList_thr.classList.contains('visible'))
    checkList_thr.classList.remove('visible');
  else
    checkList_thr.classList.add('visible');
}

var checkList_fri = document.getElementById('list5');
checkList_fri.getElementsByClassName('anchor')[0].onclick = function(evt) {
  console.log("click event")
  if (checkList_fri.classList.contains('visible'))
    checkList_fri.classList.remove('visible');
  else
    checkList_fri.classList.add('visible');
}

var checkList_sat = document.getElementById('list6');
checkList_sat.getElementsByClassName('anchor')[0].onclick = function(evt) {
  console.log("click event")
  if (checkList_sat.classList.contains('visible'))
    checkList_sat.classList.remove('visible');
  else
    checkList_sat.classList.add('visible');
}

var checkList_sun = document.getElementById('list7');
checkList_sun.getElementsByClassName('anchor')[0].onclick = function(evt) {
  console.log("click event")
  if (checkList_sun.classList.contains('visible'))
    checkList_sun.classList.remove('visible');
  else
    checkList_sun.classList.add('visible');
}





var checkbox_mon = document.getElementById('day_monday');
checkbox_mon.onclick = function(evt){ //this is the whether a checkbox has been checked for monday (yes i know thisll need to be repeated 6 more times)
  console.log("click event for the checkbox")
  
  list = document.getElementById('dropdown1_mon')
  console.log(list.classList)
  if(list.classList.contains('d-none'))
    list.classList.remove('d-none')
  else
    list.classList.add('d-none');
}



var checkbox_tue = document.getElementById('day_tuesday');

checkbox_tue.onclick = function(evt){ 
  console.log("click event for the checkbox for tuesday")

  list = document.getElementById('dropdown1_tue')
  console.log(list.classList)
  if(list.classList.contains('d-none'))
    list.classList.remove('d-none')
  else
    list.classList.add('d-none');
}





var checkbox_wed = document.getElementById('day_wednesday');

checkbox_wed.onclick = function(evt){ 
  console.log("click event for the checkbox for we")

  list = document.getElementById('dropdown1_wed')
  console.log(list.classList)
  if(list.classList.contains('d-none'))
    list.classList.remove('d-none')
  else
    list.classList.add('d-none');
}



var checkbox_thr = document.getElementById('day_thursday');

checkbox_thr.onclick = function(evt){ 
  console.log("click event for the checkbox for we")

  list = document.getElementById('dropdown1_thr')
  console.log(list.classList)
  if(list.classList.contains('d-none'))
    list.classList.remove('d-none')
  else
    list.classList.add('d-none');
}


var checkbox_fri = document.getElementById('day_friday');

checkbox_fri.onclick = function(evt){ 
  console.log("click event for the checkbox for we")

  list = document.getElementById('dropdown1_fri')
  console.log(list.classList)
  if(list.classList.contains('d-none'))
    list.classList.remove('d-none')
  else
    list.classList.add('d-none');
}


var checkbox_sat = document.getElementById('day_saturday');

checkbox_sat.onclick = function(evt){ 
  console.log("click event for the checkbox for we")

  list = document.getElementById('dropdown1_sat')
  console.log(list.classList)
  if(list.classList.contains('d-none'))
    list.classList.remove('d-none')
  else
    list.classList.add('d-none');
}


var checkbox_sun = document.getElementById('day_sunday');

checkbox_sun.onclick = function(evt){ 
  console.log("click event for the checkbox for we")

  list = document.getElementById('dropdown1_sun')
  console.log(list.classList)
  if(list.classList.contains('d-none'))
    list.classList.remove('d-none')
  else
    list.classList.add('d-none');
}


// https://stackoverflow.com/questions/19206919/how-to-create-checkbox-inside-dropdown          look at this mabye?
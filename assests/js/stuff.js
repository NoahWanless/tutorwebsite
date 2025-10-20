var checkList = document.getElementById('list1');
checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
  console.log("click event")
  if (checkList.classList.contains('visible'))
    checkList.classList.remove('visible');
  else
    checkList.classList.add('visible');
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





// https://stackoverflow.com/questions/19206919/how-to-create-checkbox-inside-dropdown          look at this mabye?
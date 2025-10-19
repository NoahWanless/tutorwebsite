var checkList = document.getElementById('list1');
checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
  if (checkList.classList.contains('visible'))
    checkList.classList.remove('visible');
  else
    checkList.classList.add('visible');
}



// https://stackoverflow.com/questions/19206919/how-to-create-checkbox-inside-dropdown          look at this mabye?
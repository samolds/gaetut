function toggleCollapse(id) {
  var element = document.getElementById(id);
  if (element.className.indexOf("out") > -1) {
    element.className = "collapse in";
  } else {
    element.className = "collapse out";
  }
}

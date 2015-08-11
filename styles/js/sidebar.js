function toggleCollapse(id) {
  var element = document.getElementById(id);
  if (element.className.indexOf("collapse") > -1 && element.className.indexOf("out") > -1) {
    element.className = element.className.replace("out", "in");
  } else {
    element.className = element.className.replace("in", "out");
  }
}

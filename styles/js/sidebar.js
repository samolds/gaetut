function buildSidebar() {
  document.getElementById("sidebar").insertAdjacentHTML('afterbegin', sidebarHtml);
}

var sidebarHtml = '' +
'<div class="col-sm-3 col-md-2 sidebar">'+
'  <h1 id="site-title">Gate</h1>'+
'  <ul class="nav nav-sidebar">'+
'    <li><a href="/gate">Home</a></li>'+
'    <li><a href="/gate/guide/guide.html">Guide</a></li>'+
'    <li><a href="http://github.com/samolds/gate/tree/master/checkpoints">Checkpoints</a></li>'+
'    <li><a href="#">References</a></li>'+
'    <li><a href="#">External Resources</a></li>'+
'    <li><a href="http://github.com/samolds/gate">GitHub Repository</a></li>'+
'  </ul>'+
'</div>';

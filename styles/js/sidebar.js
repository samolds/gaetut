function buildSidebar() {
  document.getElementById("sidebar").insertAdjacentHTML('afterbegin', sidebarHtml);
}





var sidebarHtml = '' +
'<div class="col-sm-3 col-md-2 sidebar">'+
'  <h1 id="site-title">Gate</h1>'+
'  <ul class="nav nav-sidebar">'+
'    <li class="list-header"><a href="#">Guides</a></li>'+
'    <li class="list-item"><a href="/gate/guides/overview.html">Overview</a></li>'+
'    <li class="list-item"><a href="/gate/guides/getting_started.html">Getting Started</a></li>'+
'    <li class="list-item"><a href="/gate/guides/#">Python and HTML Basics</a></li>'+
'    <li class="list-item"><a href="/gate/guides/#">Hello World</a></li>'+
'    <li class="list-item"><a href="/gate/guides/#">MVC Pattern</a></li>'+
'    <li class="list-item"><a href="/gate/guides/#">Design</a></li>'+
'    <li class="list-item"><a href="/gate/guides/#">Databases</a></li>'+
'    <li class="list-item"><a href="/gate/guides/#">Building Out</a></li>'+
'    <li class="list-item"><a href="/gate/guides/#">Publishing on GAE</a></li>'+

'    <li class="list-header"><a href="http://github.com/samolds/gate/tree/master/checkpoints">Checkpoints</a></li>'+
'    <li class="list-item"><a href="http://github.com/samolds/gate/tree/master/checkpoints/1-barebone">Barebone</a></li>'+
'    <li class="list-item"><a href="http://github.com/samolds/gate/tree/master/checkpoints/2-scaffolded">Scaffolded</a></li>'+
'    <li class="list-item"><a href="http://github.com/samolds/gate/tree/master/checkpoints/3-bootstrapped">Bootstrapped</a></li>'+
'    <li class="list-item"><a href="http://github.com/samolds/gate/tree/master/checkpoints/4-interactive">Interactive</a></li>'+
'    <li class="list-item"><a href="http://github.com/samolds/gate/tree/master/checkpoints/5-admin">Admin</a></li>'+
'    <li class="list-item"><a href="http://github.com/samolds/gate/tree/master/app">Built Out</a></li>'+

'    <li class="list-header"><a href="#">References</a></li>'+
'    <li class="list-item"><a href="/gate/refs/#">Python</a></li>'+
'    <li class="list-item"><a href="/gate/refs/#">HTML</a></li>'+
'    <li class="list-item"><a href="/gate/refs/#">CSS</a></li>'+
'    <li class="list-item"><a href="/gate/refs/#">JavaScript</a></li>'+
'    <li class="list-item"><a href="/gate/refs/#">Vim</a></li>'+
'    <li class="list-item"><a href="/gate/refs/#">Useful Command Line Tools</a></li>'+

'    <li class="list-header"><a href="#">External Resources</a></li>'+
'    <li class="list-item"><a href="http://vim.wikia.com/wiki/Tutorial">Vim Tutorial</a></li>'+
'    <li class="list-item"><a href="http://docs.python.org/2/tutorial">Python 2.7 Tutorial</a></li>'+
'    <li class="list-item"><a href="http://www.codecademy.com/en/tracks/web">HTML Tutorial</a></li>'+
'    <li class="list-item"><a href="http://www.csstutorial.net/css-intro/introductioncss-part1.php">CSS Tutorial</a></li>'+
'    <li class="list-item"><a href="http://www.codecademy.com/en/tracks/javascript">Javascript Tutorial</a></li>'+
'    <li class="list-item"><a href="http://getbootstrap.com/css">Bootstrap Documentat</a></li>'+
'    <li class="list-item"><a href="http://jinja.pocoo.org/docs/dev/templates">Jinja Documentation</a></li>'+

'    <li class="list-header"><a href="#">Other</a></li>'+
'    <li class="list-item"><a href="http://github.com/samolds/gate">GitHub Repository</a></li>'+
'  </ul>'+
'</div>';

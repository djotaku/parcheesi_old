onerror=fallo;
var zabal=ww();
var altu=hh();
var hizk='es';
function fallo(msg,non,num) {
 return(true)
}
function ww() {
 return(600+Math.round(.7*(screen.width-600)))
}
function hh() {
 return(240+Math.round(.75*(screen.height-240)))
}
function ireki(a,w,s) {
 var x
 x=window.open(a,w,s)
 x.focus()
}
function prest() {
 aditu()
}
function ie() {
 return(navigator.appName.indexOf("Microsoft")!=-1)
}
function ie7() {
 return(navigator.appVersion.indexOf("MSIE 7")!=-1)
}
function ttipi() {
 x=window.innerWidth
 y=window.innerHeight
 if (ie()) {
  x=document.body.clientWidth
  y=document.body.clientHeight
 }
 if (x<350 || y<300)
  window.top.resizeBy(Math.max(0,350-x),Math.max(0,300-y))
}
function erdian(ww,hh) {
 return(",width="+ww+",height="+hh+(screen.width?",left="+((screen.width-ww)/2):"")+(screen.height?",top="+((screen.height-hh)/2-40):""))
}
function korri3() {
 document.applets['ikus'].korri(3)
}
function aditu() {
 window.scrollTo(0,0)
 if (document.applets['ikus'].foko()=="B") {
  window.focus();
  document.applets['ikus'].focus();
 }
 z=document.applets['ikus'].zklip()
 if (z!="0")
  irekik("klip?hizk="+document.applets['ikus'].emanHizk()+"&lehia="+z+"&gako="+document.applets['ikus'].emanGako());
 if (document.applets['ikus'].martxanbai()=="B")
  setTimeout("aditu()",2000);
}
function jokatumak(h,m) {
 hizk=h
 onerror=irekierr
 if (document.applets['deika'].deitu()=="bai")
  return;
 if (ie7()) {
  var leh=open('','lehioeki',lehatr())
  if (leh!=null && leh.location.href.indexOf('http')>-1) {
   leh.focus();
   return;
  }
 }
 zabal=document.applets['deika'].ww()
 altu=document.applets['deika'].hh()
 irekizona("bai",m)
}
function bajaRes() {
 return(screen.width<801?"low":"high")
}
function irekierr(msg,non,num) {
 irekizona("bai","huts")
}
function lehatr() {
 return("toolbar=0,scrollbars=0,location=0,menubar=0,resizable=1,status=1,directories=0"+erdian(zabal,altu))
}
function irekizona(jav,m) {
 ireki("fikus?mak="+m+"&java="+jav+"&hizk="+hizk+"&rnd="+((new Date()).getTime()%997),"lehioeki",lehatr())
 return(true)
}
function irekib(s) {
 ireki(s,"_blank","toolbar=0,scrollbars=0,location=0,menubar=0,resizable=0,status=1,directories=0"+(screen.width<801?erdian("720","510"):erdian("980","710")))
}
function irekik(s) {
 ireki(s,"_blank","toolbar=0,scrollbars=1,location=0,menubar=0,resizable=1,status=1,directories=0"+erdian("770","560"))
}
function popup(s,w,h) {
 ireki(s,"_blank","toolbar=0,scrollbars=1,location=0,menubar=0,resizable=1,status=1,directories=0"+erdian(w,h))
}
function ingurune() {
 sep=" ; "
 r=navigator.appCodeName+sep+navigator.appName+sep+navigator.appVersion+sep
 r=r+navigator.platform+sep // navigator.userAgent
 r=r+"java "+(navigator.javaEnabled()?"si":"no")
 for (i=0; i<navigator.plugins.length; i++)
  r=r+(i==0?"<br>Plugins: ":sep)+navigator.plugins[i].name+" "+navigator.plugins[i].description
 return(r)
}
function hizkik(dat,relax) {
 hik="0123456789aA‚‡Â·¬≈¡¿bBcCÁ«dDeEÍÈËÎ… À»fFgGhHiIÔÓÏÌœŒÃÕjJkKlLmMnNÒ—oOÙÚÛ‘“”pPqQrRsStTuU˚˘˙⁄€ŸvVwWxXyY˝›zZ_"
 hikrelax="™∫Ê∆÷ˆƒ‰‹¸"
 d="document.login."+dat+".value"
 s=eval(d)
 r=""
 for (i=0; i<s.length; i++) {
  c=s.charAt(i)
  if (hik.indexOf(c)>-1 || (relax==1 && hikrelax.indexOf(c)>-1))
   r=r+c
 }
 if (r!=s)
  eval(d+"='"+r+"'")
}
function milleko(c1,c2,c3,p,q,z) {
 he=12;
 wi=(z==1000?32:24);
 wi2=(z==1000?16:12);
 document.write("<table cellpadding='1' width='+(wi+2)+' height='"+(he+2)+"' border='0'><tr><td bgcolor='000000'>")
 document.write("<table cellspacing='0' width='+(wi)+' height='"+he+"' cellpadding='0' border='0'><tr>")
 document.write("<td width='"+(c1==c2?wi:wi2)+"' ")
 document.write("style='background-color:"+c1+"; font-size:10px; text-align:"+(c1==c2?"center":"right")+"; color:"+c3+";'>")
 document.write(p+"</td>")
 if (c1!=c2) {
  document.write("<td width='"+wi2+"' ")
  document.write("style='background-color:"+c2+"; font-size:10px; text-align:left; color:"+c3+";'>")
  document.write(q+"</td>")
 }
 document.write("</tr></table></td></tr></table>")
}
function htmlpun(cb,cf,p) {
 document.write("<table cellpadding='1' width='34' height='14' border='0'><tr><td bgcolor='000000'>")
 document.write("<table width='32' height='12' cellspacing='0' cellpadding='0' border='0'><tr>")
 document.write("<td width='32' height='12' style='background-color:#"+cb+"; font-size:9px; text-align:center; color:#"+cf+";'>"+p)
 document.write("</td></tr></table></td></tr></table>")
}
function idatzi(z) {
 document.getElementById('ff').erantzun.value=z
 document.getElementById('ff').nola.value=1
 document.getElementById('ff').submit()
}
function lmsegi(n) {
 document.getElementById('ff').nola.value=n
 document.getElementById('ff').submit()
}
function irakur(z,n) {
 document.getElementById('ff').nola.value=n
 document.getElementById('ff').lehen.value=z
 document.getElementById('ff').submit()
}
/* Para el juego de prioridades */
function trukatu(id1,id2)
{
	/* si el navegador soporta la llamada: .getElementById // W3C DOM code */
	if (document.getElementById)
	{
		txt = document.getElementById(id1).innerHTML;
		document.getElementById(id1).innerHTML = document.getElementById(id2).innerHTML;
		document.getElementById(id2).innerHTML = txt;
	}
	/* si el navegador soporta la llamada: .all // Microsoft DOM code */
	else if (document.all)
	{
		txt = document.all[id1].innerHTML;
		document.all[id1].innerHTML = document.all[id2].innerHTML;
		document.all[id2].innerHTML = txt;
	}
	/* si el navegador soporta la llamada: .layers // Netscape DOM code */
	else if (document.layers)
	{
		x1 = document.layers[id1];
		document.all[id1].innerHTML = document.all[id2].innerHTML;
		document.all[id2].innerHTML = x1;
/*		x = document.layers[id];
		text2 = '<P CLASS="testclass">' + text + '</P>';
		x.document.open();
		x.document.write(text2);
		x.document.close(); */
	}
 temp1 = document.getElementById("v" + id1).value
 document.getElementById("v" + id1).value = document.getElementById("v" + id2).value
 document.getElementById("v" + id2).value = temp1
}


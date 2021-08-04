/* create a function to hide/show all the rectangles including their text ID's. */
function hideRect() {
  // assign variable style by element ID
  var style = document.getElementById("hideRect").style.display;
  // if style display is "none", block the element
  if(style === "none") document.getElementById("hideRect").style.display = "block";
  // otherwise show the element again
  else document.getElementById("hideRect").style.display = "none";

  var style = document.getElementById("hideRectText").style.display;
  if(style === "none") document.getElementById("hideRectText").style.display = "block";
  else document.getElementById("hideRectText").style.display = "none";
}

/* create a function to hide/show all the circles including their text ID's. */
function hideFind() {
  var style = document.getElementById("hideFind").style.display;
  if(style === "none") document.getElementById("hideFind").style.display = "block";
  else document.getElementById("hideFind").style.display = "none";
}
// create a function to hide/show all the compass elements

function hideComp() {
  var style = document.getElementById("hideComp").style.display;
  if(style === "none") document.getElementById("hideComp").style.display = "block";
  else document.getElementById("hideComp").style.display = "none";

}

function show_value_area(x)
{
 document.getElementById("slider_value1").innerHTML=x;
}

function show_value_depth(x)
{
 document.getElementById("slider_value2").innerHTML=x;
}

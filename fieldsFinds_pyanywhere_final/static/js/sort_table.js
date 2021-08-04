function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("sort");
  switching = true;
  // set ascending ordering
  dir = "asc";
  // create a loop
  while (switching) {
    // start by saying: no switching is done
    switching = false;
    rows = table.rows;
    // loop through the table rows (except the header)
    for (i = 1; i < (rows.length - 1); i++) {
      // start by saying there should be no switching
      shouldSwitch = false;
      // get elements to compare
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      // check if switch ascending or descending
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          // if yes, mark as true and break the loop
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          // if yes, mark as true and break the loop
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      // execute the switch
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // increase the count by 1 if switch is done
      switchcount ++;
    } else {
      // if no switch and ascending, run the while loop again
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

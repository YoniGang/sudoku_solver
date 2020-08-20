function createFirstTable() {
	var table = document.getElementById("board_table");

	for (j = 0; j < 3; j++) {
		var tbody = document.createElement('tbody');
		for (y = 0; y < 3; y++){
			var tr = document.createElement('tr');
			console.log(tr);

			for (i = 0; i < 9; i++) {
				var td = document.createElement('td');
				// td.innerText = '';
				tr.appendChild(td);
			}
			tbody.appendChild(tr);
		}
		// console.log(table)
		table.appendChild(tbody);
	}
}


window.onload = createFirstTable
function createFirstTable() {
	var table = document.getElementById("board_table");

	for (j = 0; j < 3; j++) {
		var tbody = document.createElement('tbody');
		for (y = 0; y < 3; y++){
			var tr = document.createElement('tr');
			row = (y+j*3).toString();
			tr.id = 'Table row: ' + row
			console.log(tr);

			for (i = 0; i < 9; i++) {
				var td = document.createElement('td');
				td.id = 'Table cell: ' + i.toString() + ' ' + row;
				var input = document.createElement('input');
				input.id = 'cell_input'
				input.type = 'number'
				td.appendChild(input)
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

function turnTableToJson() {
	var table = {}
	for (row = 0; row < 9; row++){
		rowArr = []
		for (col = 0; col < 9; col++) {
			var input = document.getElementById('Table cell: ' + 
											  col.toString() + ' ' +
											  row.toString()).children[0];
			// console.log(input.value)
			rowArr.push(input.value);
		}
		console.log(rowArr);
	}
}
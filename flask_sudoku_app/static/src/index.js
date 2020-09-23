$(createFirstGrid);

function createFirstGrid() {
	var table = document.getElementById("board_table");

	for (j = 0; j < 3; j++) {
		var tbody = document.createElement('tbody');
		for (y = 0; y < 3; y++){
			var tr = document.createElement('tr');
			row = (y+j*3).toString();
			tr.id = 'Table row: ' + row

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



function turnGridToJson() {
	var table = {}
	for (row = 0; row < 9; row++){
		rowArr = []
		for (col = 0; col < 9; col++) {
			var input = document.getElementById('Table cell: ' + 
											  col.toString() + ' ' +
											  row.toString()).children[0];
			// console.log(input.value)
			rowArr.push(Number(input.value));
		}
		table['r' + (row + 1).toString()] = rowArr;
	}
	return table;
};

function solveGrid() {
	const tableJson = turnGridToJson();
	// console.log(tableJson);
	$.ajax({
		type: 'POST',
		contentType: 'application/json',
		url: '/api/solve_grid',
		data: JSON.stringify(tableJson),
		success: function(data) {
			// console.log(data);
			fillGrid(data)
		},
		error: function(data) {
			console.log('error', data)
		}
	});
};

function fillGrid(data) {
	for (row = 0; row < 9; row++){
		rowArr = []
		for (col = 0; col < 9; col++) {
			var input = document.getElementById('Table cell: ' + 
											  col.toString() + ' ' +
											  row.toString());
			// console.log(input.value)
			input.innerText = data["r" + row][col];
		}
	}
}


function resetGrid() {
	for (row = 0; row < 9; row++){
		rowArr = []
		for (col = 0; col < 9; col++) {
			var td = document.getElementById('Table cell: ' + 
											  col.toString() + ' ' +
											  row.toString());
			td.innerText = '';
			var input = document.createElement('input');
			input.id = 'cell_input';
			input.type = 'number';
			td.appendChild(input);
		}
	}
}
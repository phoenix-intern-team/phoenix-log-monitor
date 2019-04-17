$(document).ready(function() {
    var table = $('#log_table').DataTable( {
        "scrollY": 500,
        "scrollX": true,
        'responsive':true,
        // "serverSide":true,
        "ajax": {
            // "processing": true,
            // "serverSide": true,
            "url": "http://localhost:1000/log",
            "dataSrc": "",
        },
        "columns": [
            // {
            //     "class":'details-control',
            //     "orderable": false,
            //     "data":null,
            //     "defaultContent":''
            // },
            { "data": "timestamp" },
            { "data": "loglevel" },
            { "data": "message"},
            { "data": "source"},
            { "data": "eventID"},
            { "data": "traceID" },
            { "data": "spanID" },
            // { "data": "audit" },
            // { "data": "null"}
            { "data": "stackTrace"}
            ],
        "columnDefs": [ {
            "targets": -1,
            "data": null,
            "defaultContent": "<b style=\"font-family: inherit;\">Null</b>"
        } ],

        "rowCallback": function( row, data ) {
        var obj = eval(data);
        //console.log(objdata);
            if ((obj["loglevel"]=="ERROR")) {
                $(row).css({"background-color":"#F7B8A4"});
            
        }
        if ((obj["loglevel"]=="WARN")) {
                $(row).css({"background-color":"#E9F273"});
            
        }
        if ((obj["loglevel"]=="CRITICAL")) {
                $(row).css({"background-color":"#F74E1B"});
            
        }
        if ((obj["loglevel"]=="DEBUG")) {
                $(row).css({"background-color":"#DFD8D6"});
            
        }
        if ((obj["loglevel"]=="INFO")) {
                $(row).css({"background-color":"#C1F07B"});
            
        }
            return row;
    },
            
    });
    $.fn.dataTableExt.afnFiltering.push(
        function( oSettings, aData, iDataIndex ) {
            var iFini = document.getElementById('from').value;
            var iFfin = document.getElementById('to').value;
            var iStartDateCol = 0;
            var iEndDateCol = 0;

            iFini=iFini.substring(0,4)+iFini.substring(5,7)+iFini.substring(8,10)+ iFini.substring(11,13)+iFini.substring(14,16)+iFini.substring(17,19);
            iFfin=iFfin.substring(0,4) + iFfin.substring(5,7)+ iFfin.substring(8,10)+ iFfin.substring(11,13)+iFfin.substring(14,16)+iFfin.substring(17,19);

            var datofini=aData[iStartDateCol].substring(0,4) + aData[iStartDateCol].substring(5,7)+ aData[iStartDateCol].substring(8,10)+ aData[iStartDateCol].substring(11,13)+ aData[iStartDateCol].substring(14,16)+ aData[iStartDateCol].substring(17,19);
            var datoffin=aData[iEndDateCol].substring(0,4) + aData[iEndDateCol].substring(5,7)+ aData[iEndDateCol].substring(8,10)+ aData[iEndDateCol].substring(11,13)+ aData[iEndDateCol].substring(14,16)+ aData[iEndDateCol].substring(17,19); 

            if ( iFini === "" && iFfin === "" )
            {
                return true;
            }
            else if ( iFini <= datofini && iFfin === "")
            {
                return true;
            }
            else if ( iFfin >= datoffin && iFini === "")
            {
                return true;
            }
            else if (iFini <= datofini && iFfin >= datoffin)
            {
                return true;
            }
            return false;
        }
    );
    $(document).ready(function() {
            var table = $('#log_table').DataTable();
            
            // Add event listeners to the two range filtering inputs
            $('#from').keyup( function() { table.draw(); } );
            $('#to').keyup( function() { table.draw(); } );
        });


        $('#log_table tbody').on('click', function () {
            var tr = $(this).closest('tr');
            var row = table.row( tr );
     
            if ( row.child.isShown() ) {
                // This row is already open - close it
                row.child.hide();
                tr.removeClass('shown');
            }
            else {
                // Open this row
                row.child( format(row.data()) ).show();
                tr.addClass('shown');
            }
        } );
});
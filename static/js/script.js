$(document).ready(function() {
    var table = $('#log_table').DataTable( {
        "scrollY": 500,
        "scrollX": true,
        'responsive':true,
        'deferRender':true,
        'scroller':true,
        "ajax": {
            "url": "http://127.0.0.1:5000/log", // for running on 134 http://161.92.248.134:5000/log
            "dataSrc": ""
        },
        "columns": [
            { "data": "timestamp" },
            { "data": "loglevel" },
            { "data": "message"},
            { "data": "source"},
            { "data": "eventID"},
            { "data": "traceID" },
            { "data": "spanID" },
            { "data": "stackTrace"}
            ],
            "columnDefs": [ {
                "targets": '_all',
                "data": null,
                "defaultContent": "<i style=\"font-family: inherit;\">undefined</i>"
            } ],
        "rowCallback": function( row, data ) {
        var obj = eval(data);
        //console.log(objdata);
            if ((obj["loglevel"]=="ERROR")) {
                $(row).css({"background-color":"rgb(255,190,190)"});
            
        }
        if ((obj["loglevel"]=="WARN")) {
                $(row).css({"background-color":"rgb(255,255,180)"});
            
        }
        if ((obj["loglevel"]=="CRITICAL")) {
                $(row).css({"background-color":"rgb(255,0,0)"});
                $(row).css({"color":"white"});
        }
        if ((obj["loglevel"]=="DEBUG")) {
                $(row).css({"background-color":"rgb(145,145,145)"});
            
        }
        if ((obj["loglevel"]=="INFO")) {
                $(row).css({"background-color":"rgb(200,255,200)"});
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
                row.child.hide();
            }
            else {
                row.child.show();
            }
        } );
});

// function getlivelogs() {
//     window.location = "http://127.0.0.1:9001";
// }
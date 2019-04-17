$(document).ready(function() {
    var table = $('#log_table').DataTable( {
        "scrollY": 500,
        "scrollX": true,
        'responsive':true,
        'deferRender':true,
        'scroller':true,
        // "serverSide":true,
        "ajax": {
            // "processing": true,
            // "serverSide": true,
            "url": "http://localhost:1000/log",
            "dataSrc": "",
        },
        "columns":[ 
            {
                "className":      'details-control',
                "orderable":      false,
                "data":           null,
                "defaultContent": ''
            },
            { "data": "search.mode" },
            {"data":"fullUrl"},
            {"data":"resource.recorded"},
            {"data":"resource.id"},
            {"data":"resource.meta.security.0.code"},
            {"data":"resource.meta.versionId"},
            {"data":"resource.meta.lastUpdated"},
            {"data":"resource.type.code"},
            {"data":"resource.type.system"},
            {"data":"resource.agent.0.userId.value"},
            {"data":"resource.agent.0.requestor"},
            {"data":"resource.action"},
            {"data":"resource.entity.0.type.code"},
            {"data":"resource.entity.0.type.system"},
            {"data":"resource.entity.0.type.display"},
            {"data":"resource.entity.0.identifier.value"},
            {"data":"resource.source.identifier.value"},
            {"data":"resource.outcome"},
            {"data":"resource.resourceType"}
        ],
        "columnDefs": [ {
            "targets": '_all',
            "data": null,       
            "defaultContent": "<i style=\"font-family: inherit;\">Null</i>"
        },
        { "width": "5px", "targets": 0 }
     ],
    });

        $('#log_table tbody').on('click',function () {
            var tr = $(this).closest("tr"),
            row = table.row(tr);
      
          if (row.child.isShown()) {
            tr.next('tr').removeClass('details-row');
            row.child.hide();
            tr.removeClass('shown');
          } else {
            row.child.show();
            tr.next('tr').addClass('details-row');
            tr.addClass('shown');
          }
             });
});
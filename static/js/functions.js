$(document).ready(function() {
    $('#example').DataTable({
        columns: [
            { orderable: false },
            null,
            null,
            null,
            null,
            null,
            { orderable: false }
          ],
        "order":[
            [1,'desc']
          ],
          dom: 'Qlfrtip'
    });
} );
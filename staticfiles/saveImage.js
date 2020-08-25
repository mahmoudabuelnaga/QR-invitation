$(".download").on('click', function() {
  var guest_count=$(this).attr("guest-count");
  if (guest_count==0)
  {
  Snackbar.show({
        text: 'Please add guests to download thier invitations',
        pos: 'top-center',
         actionTextColor: '#fff',
        backgroundColor: '#e7515a'
    });
   }
   else{
  block_page();
  var event_id=$(this).data('id');
  $.ajax({
  url: 'getGuestIDs/',
  data: {'event_id': event_id},
  dataType: 'json',
  success: function(responseData) {
        if(responseData.length==0)
        {
        timeFunction(event_id,50);
        }
        else
        {
        counter=0;
        $.each(responseData, function(i, item) {
         var guest_id = item.guest_id;
         var event_id = item.event_id;
         var guest_state = item.guest_state;
         pixie.loadState(guest_state).then(function() {
         var base64ImageData = pixie.getTool('export').getDataUrl('png');
         pixie.http().post('convert_data_to_image_per_guest/', {event_id:event_id,guest_id:guest_id,name: name, data: base64ImageData})
                .subscribe(function(){
                 counter++;
                 console.log(counter);
                   if(counter==responseData.length){
                    timeFunction(event_id,10000);
                }
                 });
                });

         });
         }
    },
  error: function(){
  alert('Error in Downloading');
  }
});
}
});

function timeFunction(event_id,ms) {
setTimeout(function(){
    var url = 'download_images/' + event_id;
    window.location.href = url
    $.unblockUI({})
    }, ms);
}
function block_page(){
    $.blockUI({
        message: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-loader spin"><line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="18" x2="12" y2="22"></line><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"></line><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"></line><line x1="2" y1="12" x2="6" y2="12"></line><line x1="18" y1="12" x2="22" y2="12"></line><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"></line><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"></line></svg>',
        fadeIn: 800,
       // timeout: 2000,
        overlayCSS: {
            backgroundColor: '#1b2024',
            opacity: 0.8,
            zIndex: 1200,
            cursor: 'wait'
        },
        css: {
            border: 0,
            color: '#fff',
            zIndex: 1201,
            padding: 0,
            backgroundColor: 'transparent'
        }
    });
}
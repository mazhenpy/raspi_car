$(function(){
     $("#forward").click(function(){
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{},
        dataType:"text",
        success: function(data) {
		alert(data)
        }
      });
     })
  });

// W
$(document).keydown(function(e){
    if (e.keyCode == 87) //w
    {
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'w_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

$(document).keyup(function(e){
    if (e.keyCode == 87) //w
    {
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'w_up'},
        dataType:"text",
        success: function(data) {
		alert(data)
        }
      });
    }
});

//A
$(document).keydown(function(e){
    if (e.keyCode == 65) //w
    {
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'a_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

$(document).keyup(function(e){
    if (e.keyCode == 65) //w
    {
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'a_up'},
        dataType:"text",
        success: function(data) {
		alert(data)
        }
      });
    }
});

//S
$(document).keydown(function(e){
    if (e.keyCode == 83) //w
    {
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'s_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

$(document).keyup(function(e){
    if (e.keyCode == 83) //w
    {
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'s_up'},
        dataType:"text",
        success: function(data) {
		alert(data)
        }
      });
    }
});

//D
$(document).keydown(function(e){
    if (e.keyCode == 68) //w
    {
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'d_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

$(document).keyup(function(e){
    if (e.keyCode == 68) //w
    {
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'d_up'},
        dataType:"text",
        success: function(data) {
		alert(data)
        }
      });
    }
});



















 $(document).keydown(function(event){

  alert(event.keyCode);

});
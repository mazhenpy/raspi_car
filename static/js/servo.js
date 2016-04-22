$(function(){
     $("#forward").click(function(){
        $.ajax({
        type:"GET",
        url:"/motor",
        data:{'requ_type':'button_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
     })
  });

// UP
$(document).keydown(function(e){
    if (e.keyCode == 38) //up
    {
        $.ajax({
        type:"GET",
        url:"/servo",
        data:{'requ_type':'up_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

$(document).keyup(function(e){
    if (e.keyCode == 38) //up
    {
        $.ajax({
        type:"GET",
        url:"/servo",
        data:{'requ_type':'up_up'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

//DOWN
$(document).keydown(function(e){
    if (e.keyCode == 40) // down
    {
        $.ajax({
        type:"GET",
        url:"/servo",
        data:{'requ_type':'down_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

$(document).keyup(function(e){
    if (e.keyCode == 40) // down
    {
        $.ajax({
        type:"GET",
        url:"/servo",
        data:{'requ_type':'down_up'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

//LEFT
$(document).keydown(function(e){
    if (e.keyCode == 37) // left
    {
        $.ajax({
        type:"GET",
        url:"/servo",
        data:{'requ_type':'left_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

$(document).keyup(function(e){
    if (e.keyCode == 37) // left
    {
        $.ajax({
        type:"GET",
        url:"/servo",
        data:{'requ_type':'left_up'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

//RIGHT
$(document).keydown(function(e){
    if (e.keyCode == 39) // right
    {
        $.ajax({
        type:"GET",
        url:"/servo",
        data:{'requ_type':'right_down'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

$(document).keyup(function(e){
    if (e.keyCode == 39) // right
    {
        $.ajax({
        type:"GET",
        url:"/servo",
        data:{'requ_type':'right_up'},
        dataType:"text",
        success: function(data) {
		// alert(data)
        }
      });
    }
});

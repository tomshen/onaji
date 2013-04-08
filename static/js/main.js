$('document').ready(function() {
  function subscribe(phone, email, name){
    if(!name){
      name = "No Name"
    }
    console.log(name);

    function validEmail(email) { 
    // http://stackoverflow.com/a/46181/11236
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    }


    if(!validEmail(email) && email.length > 0){
      alert("Please enter a valid email");
      return;
    }
    phone = phone.replace(/[^0-9]/g, '');
    if(phone.length != 10 && phone.length!=0) { 
      alert("Please enter a valid phone number");
      return;
    }

    $.get("/subscribers/new/", {"email": email, "phone":phone, "name": name}, function(data) {
      alert("Subscribed successfully");
    });
    
  }
  
  $("#signup-button").click(function() {
    alert("Enter an email and phone number for automatic event notifications");
    var name = prompt("name:");
    var email = prompt("email:");
    var phone = prompt("phone number:");
    subscribe(phone, email, name);
  });

  var panes = ["#quest-pane", "#notif-pane", "#schedule-pane"];
  var image_classes = ["question-bubble", "contact", "cal"];
  var current_pane = 1;
  var left_pane = 0;
  var right_pane = 2;
  function swapPaneLeft(){
    var p = panes[current_pane];
    var origleft = image_classes[left_pane];
    var origright = image_classes[right_pane];
	
	$(p).fadeOut(200, function(){
      $(panes[current_pane]).fadeIn(200);
    });
	temp = current_pane;
    current_pane = left_pane;
	left_pane = right_pane;
	right_pane = temp;
    
    $("#switch-left").children().first().removeClass(origleft).addClass(image_classes[left_pane]);
    $("#switch-right").children().first().removeClass(origright).addClass(image_classes[right_pane]);
  } 

  function swapPaneRight(){
    var p = panes[current_pane];
    var origleft = image_classes[left_pane];
    var origright = image_classes[right_pane];

	$(p).fadeOut(200, function(){
      $(panes[current_pane]).fadeIn(200);
    });
	temp = current_pane;
    current_pane = right_pane;
	right_pane = left_pane;
	left_pane = temp;
    

    $("#switch-left").children().first().removeClass(origleft).addClass(image_classes[left_pane]);
    $("#switch-right").children().first().removeClass(origright).addClass(image_classes[right_pane]);
  }

  function populateCurrentDiv(){
    if(current_pane == 0){
      if(csrftoken){
        createQAndAFeed(getAllQuestionsBlob());
      }
      else{
        createQAndAFeed(getAnsweredQuestionsBlob());
      }
    }
    if(current_pane == 1){
      addNotifications('#notif-pane');
    }
    if(current_pane == 2){
      addSchedule('#schedule-pane');
    }

    $(".edit.small.icon").click(function(){
      alert("Please go to the admin interface to edit events.");
    });
    $(".delete.small.icon").click(function(){
      alert("Please go to the admin interface to delete events.");
    });
  } 

  populateCurrentDiv();

  $("#switch-left").click(function(){
    swapPaneLeft();
    populateCurrentDiv();
  });

  $("#switch-right").click(function(){
    swapPaneRight();
    populateCurrentDiv();
  });
});
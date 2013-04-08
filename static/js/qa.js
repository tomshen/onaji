function createQAndAFeed(jsonblob){
  $("#quest-pane").html("");
  if(jsonblob && jsonblob.length > 0) {
    jsonblob.reverse();
    for(var i = 0; i<jsonblob.length; i++){
      var n = jsonblob[i];
      insertQuestionNode(n.title, n.text, n.poster, n.post_date, n.answered, n.answer, n.answerer, n.question_id);
    }
    if(!authenticated){
      addQuestionFormNode();
    }
  }
}

function addQANode(element) {
  var qa = '<h1>Ask a Question</h1> \
    <div class="question ask"> \
    <textarea type="text" placeholder="title" class="short-text" id="question-ask-title" ></textarea> \
    <textarea type="text" placeholder="name" class="short-text" id="question-ask-name" ></textarea> \
    <textarea type="text" placeholder="contact email (not required)" class="short-text" id="question-ask-email" ></textarea> \
    <textarea type="text" placeholder="contact phone number (not required)" class="short-text" id="question-ask-phone" ></textarea> \
    <textarea type="text" class="long-text" id="question-ask-body" placeholder="your question"></textarea> \
    <div class="button post" id="qa-button">Post</div> \
    </div>'
  $(element).append(qa)
  $('#qa-button').click(function () {
    postQuestion($('#question-ask-title').val(), $('#question-ask-name').val(), 
           $('#question-ask-body').val(), $('#question-ask-email').val())
  })
}

function getAllQuestionsBlob(){
  var ans;
  jQuery.ajaxSetup({async:false});
  $.get("/questions/all/", function(data) {
    ans = data;
  });
  return ans;
}

function getAnsweredQuestionsBlob(){
  var ans;
  jQuery.ajaxSetup({async:false});
  $.get("/questions/answered/", function(data) {
    ans = data;
  });
  return ans;
}

function postQuestion(title, poster, text, asker_email){
  if(!asker_email){
    asker_email = "";
  }
  var post_date = moment().format();
  $.get("/questions/new/", {"title": title, "poster":poster, "text": text, "asker_email": asker_email }, function(data) {
  });
}

function answerQuestion(answer, answerer, questionID){
  $.post("/questions/update/" + questionID.toString() + "/", { "answer": answer, "answerer":answerer, "answered": true }, function(data) {
    console.log(data);
  });
}

function insertQuestionNode(title, content, poster, post_date, answered, answer, answerer, id){
  var newDiv = $("<div>").addClass("question");
  var h1 = $("<h1>").html(title);
  var h2 = $("<h2>").html(content);
  var h4 = $("<h4>").html(poster);
  var h5 = $("<h5>").html(moment().fromNow(post_date) + ' ago');
  newDiv.append(h1).append(h2).append(h4).append(h5);
  if(!answered && csrftoken){
    newDiv.addClass("answer");
    var adminNameTextField = $("<textarea>").addClass("short-text").attr('placeholder', "Your name").attr('type', "text").attr('id', "admin_name_"+id);
    var answerArea = $("<textarea>").addClass("long-text").attr('placeholder', "Answer the question here").attr('type', "text").attr('id', "answer_"+id);
    var postbutton = $("<div>").addClass('button').addClass('post').html("Post");
    postbutton.click(function(){
      var answer_text = $("#answer_" + id).val();
      var answerer_name = $("#admin_name_" + id).val();
      answerQuestion(answer_text, answerer_name, id);
      alert("Question answered");
      createQAndAFeed(getAllQuestionsBlob());
    });

    newDiv.append(adminNameTextField).append(answerArea).append(postbutton);
  }
  else{
    var h3 = $("<h3>").html(answer);
    var adminName = $("<h4>").html(answerer);
    newDiv.append(h3).append(adminName);
  }

  $('document').ready(function(){
    $("#quest-pane").append(newDiv);
  });
}

function addQuestionFormNode() {
  var qnode = '<div class="question ask">'+
    '<textarea type="text" placeholder="title" class="short-text" id="question-ask-title" ></textarea>'+
    '<textarea type="text" placeholder="name" class="short-text" id="question-ask-name" ></textarea>'+
    '<textarea type="text" placeholder="contact email (not required)" class="short-text" id="question-ask-email" ></textarea>'+
    '<textarea type="text" class="long-text" id="question-ask-body" placeholder="your question"></textarea>'+
    '<div class="button post" id = "post-question">Post</div>'+
    '</div>';

  $("#quest-pane").prepend(qnode);

  $("#post-question").click(function(){
    var qtitle = $("#question-ask-title").val();
    var qposter = $("#question-ask-name").val();
    var qemail = $("#question-ask-email").val();
    var qtext  = $("#question-ask-body").val();
    postQuestion(qtitle, qposter, qtext, qemail);
    alert("Success! You should get an answer very soon.")
    createQAndAFeed(getAnsweredQuestionsBlob());

  });

}
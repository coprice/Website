function submitClicked() {
  nameInput = document.getElementById('nameInput');
  emailInput = document.getElementById('emailInput');
  subjectInput = document.getElementById('subjectInput');
  messageInput = document.getElementById('messageInput');
  messageDiv = document.getElementById('messageDiv');

  if (nameInput.value == "") {
    messageDiv.innerHTML = '<div class="ui red message">Please enter your name.</div><br>'
    return false;
  }

  if (emailInput.value == "") {
    messageDiv.innerHTML = '<div class="ui red message">Please enter your email.</div><br>'
    return false;
  }

  if (messageInput.value == "") {
    messageDiv.innerHTML = '<div class="ui red message">Please enter a message.</div><br>'
    return false;
  }

  return true;
}

$(document).ready(function() {

  /* Form validation */
  $('.ui.form').form({});

	$(".project-card").click(function() {
    	page_url        = $(this).attr("href");
    	window.location = page_url
    });

  $(".ui.video").video();

	/* Grid animations */

	$("#articles-grid").appear();

	$.each($(".project-card"), function(key, value) {
		$(value).hide();
    $(value).delay(key * 100 + 500).fadeIn();
	});

	/* Text animations */

	$("h1").hide();
    $("p").hide();
    $("ul").hide();

    $("h1").transition("fade up", '500ms');
    $("p").delay(500).transition('fade up', '500ms');
    $("ul").delay(500).transition('fade up', '500ms');

    if ($(window).width() > 1100) {
    	$("#home-button").addClass("stuck");
    }

});

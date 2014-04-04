function responsivize () {
  $ ('.responsive')
  		.css({
  		  height: $(window).height() + 'px',
  		  width: $(window).width() + 'px',
  		  });
}

$(document).ready(function() {

	$('.featured-image').imgLiquid();
	responsivize();
	$(window).on('resize', responsivize);

	$("div.featured-image").click(function() {
		$("html, body").animate({
			"scrollTop": $('#about').offset().top-100
		});
		$("nav").css({
			display: "inline"
		});
		responsivize();
	});
});


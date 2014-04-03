function responsivize () {
  $ ('.featured-image')
  		.css({
  		  height: $(window).height() + 'px',
  		  width: $(window).width() + 'px',
  		  });
}

$(document).ready(function() {

	$('.featured-image').imgLiquid();
	responsivize();
	$(window).on('resize', responsivize);
});
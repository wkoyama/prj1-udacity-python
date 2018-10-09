

// Pause the video when the modal is closed
// $(document).on('click', '.hanging-close, .modal-backdrop, .movie-trailer', function (event) {
//     // Remove the src so the player itself gets removed, as this is the only
//     // reliable way to ensure the video stops playing in IE
//     var dataMovieId = $(this).attr('data-movie-id')
//     $("#trailer-video-container-" + dataMovieId).empty();
// });
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var dataMovieId = $(this).attr('data-movie-id')
    
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=0&html5=1';
    $("#trailer-video-container-" + dataMovieId).empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});

// Animate in the movies when the page loads
$(document).ready(function () {
  $('.movie-tile').show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });
});


/* Open */
/* Open when someone clicks on the span element */
function openMovieContent(id) {
    var body = document.body,
    overlay = document.getElementById("movie-content-" + id);

    document.getElementById("movie-content-" + id).style.width = "100%";
    
    overlay.setAttribute('aria-hidden', false);
    body.classList.toggle('noscroll', true);

    /* On some mobile browser when the overlay was previously
    opened and scrolled, if you open it again it doesn't 
    reset its scrollTop property after the fadeout */
     setTimeout(function() {
    overlay.scrollTop = 0;              }, 1000);

}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeMovieContent(id) {

    var body = document.body,
    overlay = document.getElementById("movie-content-" + id);
    
    document.getElementById("movie-content-" + id).style.width = "0%";
    $("#trailer-video-container-" + id).empty();
    
    overlay.setAttribute('aria-hidden', true);
    body.classList.toggle('noscroll', false);

    /* On some mobile browser when the overlay was previously
    opened and scrolled, if you open it again it doesn't 
    reset its scrollTop property after the fadeout */
    setTimeout(function() {
    overlay.scrollTop = 0;              }, 1000);
    
}
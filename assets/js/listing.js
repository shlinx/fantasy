/**
 * Created by xlin on 6/12/16.
 */
import '../scss/listing.scss';

$('.slick').slick({
    dots: true,
    infinite: true,
    slidesToShow: 1,
    autoplay: true,
    fade: true,
    pauseOnHover: false,
    pauseOnFocus: false,
    speed: 2000,
    autoplaySpeed: 2000,
    arrows: false
});

(function initMap() {
    let $map = $('#map'),
        position = {
            lat: $map.data('latitude'),
            lng: $map.data('longitude')
        },
        map = new google.maps.Map(document.getElementById('map'), {
            zoom: 15,
            center: position
        }),
        marker = new google.maps.Marker({
            position: position,
            map: map
        });
})();

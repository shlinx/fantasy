/**
 * Created by xlin on 6/12/16.
 */
import '../scss/main.scss';

$('#search-tab').easyResponsiveTabs({
    type: 'default',
    width: 'auto',
    fit: true,
    closed: true
});

let $grid = $('.grid').masonry({
    itemSelector: '.grid-item',
    columnWidth: '.grid-sizer',
    gutter: '.gutter-sizer',
    percentPosition: true
});

$grid.imagesLoaded().progress(() => {
    $grid.mansonry('layout');
});
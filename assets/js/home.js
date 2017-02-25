/**
 * Created by xlin on 6/12/16.
 */
import '../scss/home.scss';

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

function closestEdge(x,y,w,h) {
        let topEdgeDist = distMetric(x,y,w/2,0);
        let bottomEdgeDist = distMetric(x,y,w/2,h);
        let leftEdgeDist = distMetric(x,y,0,h/2);
        let rightEdgeDist = distMetric(x,y,w,h/2);
        let min = Math.min(topEdgeDist, bottomEdgeDist, leftEdgeDist, rightEdgeDist);

        switch (min) {
            case leftEdgeDist:
                return "left";
            case rightEdgeDist:
                return "right";
            case topEdgeDist:
                return "top";
            case bottomEdgeDist:
                return "bottom";
        }
}

function distMetric(x,y,x2,y2) {
    let xDiff = x - x2;
    let yDiff = y - y2;
    return (xDiff * xDiff) + (yDiff * yDiff);
}

const transitionTime = '.7s';

$('.grid-item').hover(function(e) {
        let el_pos = $(this).offset(),
            edge = closestEdge(e.pageX - el_pos.left, e.pageY - el_pos.top, $(this).width(), $(this).height()),
            $grid = $(this),
            gridWidth = $grid.width(),
            gridHeight = $grid.height(),
            $summary = $(this).find('.summary');

        $summary.css('transition', 'none');
        switch(edge) {
            case 'left':
                $summary.css('transform', `translateX(-${gridWidth}px)`);
                $summary.css('transform');
                $summary.css('transition', transitionTime);
                $summary.css('transform', 'translateX(0)');
                break;
            case 'right':
                $summary.css('transform', `translateX(${gridWidth}px)`);
                $summary.css('transform');
                $summary.css('transition', transitionTime);
                $summary.css('transform', 'translateX(0)');
                break;
            case 'top':
                $summary.css('transform', `translateY(-${gridHeight}px)`);
                $summary.css('transform');
                $summary.css('transition', transitionTime);
                $summary.css('transform', 'translateY(0)');
                break;
            case 'bottom':
                $summary.css('transform', `translateY(100%)`);
                $summary.css('transform');
                $summary.css('transition', transitionTime);
                $summary.css('transform', 'translateY(0)');
                break;
        }
    }, function(e) {
        let el_pos = $(this).offset(),
            edge = closestEdge(e.pageX - el_pos.left, e.pageY - el_pos.top, $(this).width(), $(this).height()),
            $grid = $(this),
            gridWidth = $grid.width(),
            gridHeight = $grid.height(),
            $summary = $(this).find('.summary');

        switch(edge) {
            case 'left':
                $summary.css('transform', `translateX(-${gridWidth}px)`);
                break;
            case 'right':
                $summary.css('transform', `translateX(${gridWidth}px)`);
                break;
            case 'top':
                $summary.css('transform', `translateY(-${gridHeight}px)`);
                break;
            case 'bottom':
                $summary.css('transform', `translateY(100%)`);
                break;
        }
});

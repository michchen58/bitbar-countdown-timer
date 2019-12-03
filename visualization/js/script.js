// TODO
// merge consecutive duplicates
// highlight empty time longer than x mins
// past midnight??

document.write(`<script src="../countdown_timer/logs/${VIEW_YEAR}/${VIEW_MONTH}/${VIEW_DATE}.js" type="text/javascript"></script>`);

function processIntervals(curEventObj, nextEventObj) {
    // duration as defined by the cur object
    let duration = calculateMinutes(curEventObj.duration);

    if (!nextEventObj) {
        // or maybe if timer ongoing (e.g. data.txt exists) then don't display the last item
        return duration;
    } else {
        // minutes between cur and next
        let timeDiff = Math.round((nextEventObj.time - curEventObj.time) / 1000 / 60);
        if (timeDiff < duration) {
            return roundDuration(timeDiff);
        } else {
            return roundDuration(duration);
        }
    }
}

function updateDate() {
    if (!VIEW_STR) {
        VIEW_STR = document.location.hash.replace(/[^\d]/g,'');
    }
    VIEW_YEAR = VIEW_STR.substr(0,4);
    VIEW_MONTH = VIEW_STR.substr(4,2);
    VIEW_DATE = VIEW_STR.substr(6,2);

    let cur_date = new Date(VIEW_YEAR, VIEW_MONTH - 1, VIEW_DATE);

    var tomorrow = new Date(cur_date);
    tomorrow.setDate(cur_date.getDate()+1);
    var yesterday = new Date(cur_date);
    yesterday.setDate(cur_date.getDate()-1);

    let next_disabled = (VIEW_STR === dateId(new Date())) ? 'disabled' : '';
    let prev_disabled = (VIEW_STR === dateId(FIRST_DATE)) ? 'disabled' : '';
    let today_disabled = (VIEW_STR === dateId(new Date())) ? 'disabled' : '';

    $('#nav').html(`
        <a class="nav ${prev_disabled}" id="nav_prevDay" href="#${dateId(yesterday)}">prev</a>
        <a class="nav ${next_disabled}" id="nav_nextDay" href="#${dateId(tomorrow)}">next</a>
        <a class="nav ${today_disabled}" id="nav_today" href="#${dateId(new Date())}">today</a>
    `);

    $('body').keydown(e => {
        if (e.which === 37 && !prev_disabled) {
            window.location.hash = dateId(yesterday);
        } else if (e.which === 39 && !next_disabled) {
            window.location.hash = dateId(tomorrow);
        } else if (e.which === 84) {
            window.location.hash = dateId(new Date());
        }

    });

    let cur_day = cur_date.getDay();
    $('#title').html(`${DAY_NAMES[cur_day]} ${MONTH_NAMES[parseInt(VIEW_MONTH) - 1]} ${VIEW_DATE}, ${VIEW_YEAR}`)
               .click(e => {
                   let copyText = document.getElementById('copy');
                   copyText.select();
                   document.execCommand("copy");
                   copyText.blur();
               });
    $('#copy').val(`/Users/chenm/Applications/BitBar/plugins/countdown_timer/logs/${VIEW_YEAR}/${VIEW_MONTH}/${VIEW_DATE}.js`);
}

function eventElt(eventObj, index) {
    let objTime = eventObj.time;
    let objTask = eventObj.task;
    let objDuration = eventObj.duration;
    if (objTask === '' || objTask === '[no name]') {
        objTask = '';
    }

    let objDurationMinutes = processIntervals(data[index], data[index + 1]);

    if (objDurationMinutes) {
        return `<div class="event">
            <span class="eventDuration disabled">${objDurationMinutes}</span>
            <span class="eventName">${objTask}</span>
            <span class="eventTime disabled">${render_time(objTime)}</span>
        </div>`;
    }
}

$(document).ready(() => {
    if (typeof data !== 'undefined') {
        data.forEach((eventObj, i) => {
            $(`#${viewerID}`).append(eventElt(eventObj, i));
        });
        $('.event').hover(
            function() {$(this).addClass("eventHover")},
            function() {$(this).removeClass("eventHover")}
        );
    } else {
        $('#taskList').html('<span class="disabled">No tasks for this date</span>')
    }
    updateDate();
})

window.onhashchange = function() {
    location.reload();
    updateDate();
}

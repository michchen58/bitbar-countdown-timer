// TODO: merge intervals if two consecutive tasks have the same name
// TODO: specify project'
    // have another input for project name
    // prepopulate it with contents of lastProject file
    // use that to add divders to visualization
// TODO: see true duration on hover
// TODO: if cancel

var VIEW_STR = document.location.hash.replace(/[^\d]/g,'');

if (!VIEW_STR) {
    VIEW_STR = dateId(new Date())
}

var VIEW_YEAR = VIEW_STR.substr(0,4);
var VIEW_MONTH = VIEW_STR.substr(4,2);
var VIEW_DATE = VIEW_STR.substr(6,2);
const MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const DAY_NAMES = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
const FIRST_DATE = new Date(2019, 7 - 1, 12);
const viewerID = 'taskList';

function calculateMinutes(duration) { // will be useful when hours and seconds come into the equation
    let matches = duration.match(/(\d+)m/);
    return parseInt(matches[1]) || 0;
}

function dateId(dateObj) {
    let today = new Date();
    let month = dateObj.getMonth() + 1;
    let date = dateObj.getDate();
    return `${dateObj.getFullYear()}${month < 10 ? '0' + month : month}${date < 10 ? '0' + date : date}`
}

function render_time(timestamp) {
    let dateObj = new Date(timestamp);
    let minutes = dateObj.getMinutes();
    let hours = dateObj.getHours();
    let ampm = hours > 12 ? 'pm' : 'am';

    hours = hours % 12;
    hours = hours || 12;
    minutes = minutes < 10 ? '0' + minutes : minutes;

    return `${hours}:${minutes} ${ampm}`
}

function roundDuration(minutes) {
    if (minutes < 20) {
        return ((Math.round(minutes / 10 * 2) / 2) * 10) || 0;
    } else {
        return Math.round(minutes / 10) * 10;
    }
}

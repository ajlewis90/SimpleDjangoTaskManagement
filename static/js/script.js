// Small bits of front end behavior for the Task Manager app.
// Nothing fancy here, just a couple of quality of life touches
// that do not need a JS framework to pull off.

document.addEventListener('DOMContentLoaded', function () {
    // Auto dismiss flash messages after a few seconds so they do not
    // sit on the page forever after the user has already read them.
    var messages = document.querySelectorAll('.message');
    messages.forEach(function (message) {
        setTimeout(function () {
            message.style.transition = 'opacity 0.4s ease';
            message.style.opacity = '0';
            setTimeout(function () {
                message.remove();
            }, 400);
        }, 4000);
    });

    // Extra confirmation on any delete link, just in case someone
    // clicks it by accident from the task list table.
    var deleteLinks = document.querySelectorAll('.danger-link');
    deleteLinks.forEach(function (link) {
        link.addEventListener('click', function (event) {
            var confirmed = window.confirm('Delete this task? This cannot be undone.');
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});

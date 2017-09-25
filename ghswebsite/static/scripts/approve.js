let createCard = (el, data) => {
    template = Handlebars.compile(el.innerHTML);
    html = template(data);
    return html;
};

let populate = (el, data) => {
    let template = document.querySelector('#template');
    el.empty();
    for (var i = 0, len = data.length; i < len; i++) {
        el.append(createCard(template, data[i]));
    }
};

window.onload = () => {
    var csrftoken = jQuery('[name=csrfmiddlewaretoken]').val();
    var container = $('.hour-container');
    populate(container, hours);
    container.on('click', '.approve', function (e) {
        e.preventDefault();
        let pk = $(this).data('pk');
        $.post(approveEndpoint, {
                'pk': pk,
                'action': 'approve',
                'csrfmiddlewaretoken': csrftoken
            },
            function (data) {
                if (data.error) {
                    console.log(data.error);
                } else {
                    populate(container, data);
                }
            });
    });
    container.on('click', '.reject', function (e) {
        e.preventDefault();
        let pk = $(this).data('pk');
        $.post(approveEndpoint, {
                'pk': pk,
                'action': 'reject',
                'csrfmiddlewaretoken': csrftoken
            },
            function (data) {
                if (data.error) {
                    console.log(data.error);
                } else {
                    populate(container, data);
                }
            });
    });
};

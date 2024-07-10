$(document).ready(function() {
    function toggleHijosFields() {
        if ($('#id_tiene_hijos').val() === 'si') {
            $('#hijos_formset').show();
        } else {
            $('#hijos_formset').hide();
        }
    }

    toggleHijosFields();

    $('#id_tiene_hijos').change(function() {
        toggleHijosFields();
    });

    $('#add_hijo').click(function() {
        const formIdx = $('#hijos_formset .formset-form').length;
        const newForm = $('#hijos_formset .empty-form').html().replace(/__prefix__/g, formIdx);
        $('#hijos_formset').append(newForm);
    });
});

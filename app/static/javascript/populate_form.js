function populate_form(form){
    for (i = 0; i < pub_review_fields.length; i++) {
        if (document.getElementById(pub_review_fields[i])) {
            if (dropdown_controls.includes(pub_review_fields[i])) {
                var dropdown_str = String(pub_review[0][pub_review_fields[i]]['0']).toUpperCase() + String(pub_review[0][pub_review_fields[i]]).substring(1)
                document.getElementById(pub_review_fields[i]).value = dropdown_str
            } else {
                document.getElementById(pub_review_fields[i]).value = pub_review[0][pub_review_fields[i]];
            }
        } else {
            continue;
        }
    }
    slider = []
    output = []
    for (let i = 0; i < slider_controls.length; i++) {
        slider[i] = document.getElementById(slider_controls[i]);
        output[i] = document.getElementById("value_" + slider_controls[i]);
        output[i].innerHTML = slider[i].value;
        if (form == 'edit' || form == 'add') {
            slider[i].oninput = function() {
                output[i].innerHTML = document.getElementById(slider_controls[i]).value;
                sum_score()
            }
        }
    }
    sum_score()
}

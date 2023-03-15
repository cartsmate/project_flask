function insert_line(which_list, toggle, name, type, list_required, input_controls, dropdown_controls, slider_controls){
    var actual_width = window.innerWidth;
    if(actual_width < 480) {
        var slider_col = "col-sm-6"
    } else {
        var slider_col = "col-sm-6"
    }
    const form_node = document.createElement("div");
    form_node.setAttribute("class", "form-group row");
    id_row = "row_" + name
    form_node.setAttribute("id", id_row);
    document.getElementById(which_list).appendChild(form_node);
    const label_node = document.createElement("label");
    label_node.setAttribute("class", "col-sm-3 col-form-label");
    label_node.setAttribute("for", name);
    if (type != "hidden") {
        label_node.setAttribute("style", "margin: auto; visibility: visible; display: block;");
    } else {
        label_node.setAttribute("style", "margin: auto; display: none;");
    }
    const textnode = document.createTextNode(name);
    label_node.appendChild(textnode);
    document.getElementById(id_row).appendChild(label_node);
    if (dropdown_controls.includes(name) && (toggle == 'add' || toggle == 'edit')) {
        const div_node = document.createElement("div");
        div_node.setAttribute("class", "col-sm-9");
        id_div = "div_" + name
        div_node.setAttribute("id", id_div);
        document.getElementById(id_row).appendChild(div_node);
        const select_node = document.createElement("select");
        select_node.setAttribute("class", "form-control");
        select_node.setAttribute("id", name);
        select_node.setAttribute("name", name);
        document.getElementById(id_div).appendChild(select_node);
        var option = document.createElement("option");
        option.value = "";
        switch(name) {
            case 'category':
                var options = ['Bar', 'Restaurant', 'Other']
                option.text = "select category";
                break;
            case 'star':
                var options = ['Atmosphere', 'Cleanliness', 'Clientele', 'Decor', 'Entertainment', 'Food', 'Friendliness', 'Opening', 'Price', 'Selection']
                option.text = "select venue star quality";
                break;
            case 'reviewer':
                var options = ['ANDY', 'AVNI', 'BOTH', 'OTHER']
                option.text = "select reviewer";
                break;
            default:
                var options = ['1', '2', '3', '4']
                option.text = ".... error ....";
        }
        select_node.appendChild(option);
        for (var i = 0; i < options.length; i++) {
            var option = document.createElement("option");
            option.value = options[i];
            option.text = options[i];
            select_node.appendChild(option);
        }
    } else if (slider_controls.includes(name)) {
        const div_node = document.createElement("div");
        div_node.setAttribute("class", slider_col);
        id_div = "div_" + name
        div_node.setAttribute("id", id_div);
        div_node.setAttribute("style", "margin: auto;");
        document.getElementById(id_row).appendChild(div_node);
        const slide_node = document.createElement("div")
        slide_node.setAttribute("class", "slidecontainer");
        slide_node.setAttribute("style", "margin: auto; width: 100%");
        id_slider = "slider_div_" + name
        slide_node.setAttribute("id", id_slider);
        document.getElementById(id_div).appendChild(slide_node);
        const input_node = document.createElement("input");
        input_node.setAttribute("type", "range");
        input_node.setAttribute("min", "0");
        if (name == 'score') {
            input_node.setAttribute("max", "100");
        } else {
            input_node.setAttribute("max", "10");
        }
        input_node.setAttribute("value", "0");
        input_node.setAttribute("class", "slider");
        input_node.setAttribute("id", name);
        input_node.setAttribute("name", name);
        input_node.setAttribute("style", "width: 100%");
        if (toggle == 'read' || name == 'score') {
            input_node.setAttribute("disabled", "true");
        }
        document.getElementById(id_slider).appendChild(input_node);
        const value_div_node = document.createElement("div");
        value_div_node.setAttribute("class", "col");
        id_value_div = "value_div_" + name
        value_div_node.setAttribute("id", id_value_div);
        document.getElementById(id_row).appendChild(value_div_node);
        const value_node = document.createElement("div")
        value_node.setAttribute("class", "col score");
        value_node.setAttribute("style", "font-family:copperplate; font-size:40px; margin: auto");
        value_node.setAttribute("id", "value_" + name);
        document.getElementById(id_value_div).appendChild(value_node);
    } else {
        const div_node = document.createElement("div");
        div_node.setAttribute("class", "col-sm-9");
        id_div = "div_" + name
        div_node.setAttribute("id", id_div);
        if (type != "hidden") {
            div_node.setAttribute("style", "visibility: visible; display: block;");
        } else {
            div_node.setAttribute("style", "display: none;");
        }
        document.getElementById(id_row).appendChild(div_node);
        const input_node = document.createElement("input");
        input_node.setAttribute("type", type);
        input_node.setAttribute("name", name);
        input_node.setAttribute("class", "form-control");
        input_node.setAttribute("id", name);
        if (type != "hidden") {
            input_node.setAttribute("style", "visibility: visible; display: block;");
        } else {
            input_node.setAttribute("style", "display: none;");
        }
        document.getElementById(id_div).appendChild(input_node);
        if (list_required.includes(name)) {
            document.getElementById(name).required = true;
        }
    }
    if (toggle == 'readonly') {
        document.getElementById(name).readOnly = true;
    }
}
